#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chart Generator - Generate chart configurations for Chart.js and React (Recharts):
line, bar, pie, doughnut, area, radar, scatter, polarArea
Cyber-Rage Design Intelligence Engine

Usage: python chart_generator.py --chart line --labels "Jan,Feb,Mar,Apr" --data "10,20,15,30"
       python chart_generator.py --chart pie --labels "SaaS,B2B,E-commerce,Other" --data "40,30,20,10" --framework recharts
       python chart_generator.py --chart bar --labels "Q1,Q2,Q3,Q4" --data "25,40,35,50" --colors "#2563EB,#F97316"
"""

import argparse
import json
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


DEFAULT_COLORS = ["#2563EB", "#F97316", "#10B981", "#F59E0B", "#EF4444", "#8B5CF6", "#EC4899", "#14B8A6"]


def split_csv(value):
    return [item.strip() for item in value.split(",") if item.strip()]


def chartjs_chart(chart_type, labels, datasets, colors, options=None):
    datasets_json = []
    for i, data in enumerate(datasets):
        color = colors[i % len(colors)]
        ds = {"label": f"Series {i + 1}", "data": data}
        if chart_type in ("line", "area", "scatter"):
            ds["borderColor"] = color
            ds["backgroundColor"] = color
            ds["borderWidth"] = 2
            ds["tension"] = 0.3
            if chart_type == "area":
                ds["fill"] = True
                ds["backgroundColor"] = f"{color}33"
        elif chart_type == "bar":
            ds["backgroundColor"] = color
            ds["borderRadius"] = 6
        elif chart_type in ("pie", "doughnut", "polarArea", "radar"):
            ds["backgroundColor"] = colors[: max(len(data), len(labels))]
            ds["borderColor"] = "#fff"
            ds["borderWidth"] = 2
        datasets_json.append(ds)

    chart_cfg = {
        # Chart.js has no "area" controller - area charts are line charts
        # with fill: true (emitting "type": "area" throws at runtime).
        "type": "line" if chart_type == "area" else chart_type,
        "data": {"labels": labels, "datasets": datasets_json},
        "options": options or {
            "responsive": True,
            "maintainAspectRatio": True,
            "plugins": {
                "legend": {"position": "bottom"},
                "tooltip": {"enabled": True},
            },
        },
    }
    pretty = json.dumps(chart_cfg, indent=2)
    return f"""<!-- Chart.js - {chart_type} chart -->
<canvas id="chart" aria-label="Chart" role="img"></canvas>
<script>
const ctx = document.getElementById('chart');
new Chart(ctx, {pretty});
</script>"""


def recharts_chart(chart_type, labels, datasets, colors):
    components = {
        "line": "LineChart",
        "bar": "BarChart",
        "area": "AreaChart",
        "radar": "RadarChart",
        "scatter": "ScatterChart",
    }
    if chart_type not in components:
        return None
    comp = components[chart_type]

    series = "\n".join(
        f"""      <{comp.split("Chart")[0]} dataKey="v{i}" name="Series {i + 1}" stroke="{colors[i % len(colors)]}" fill="{colors[i % len(colors)]}" />"""
        for i in range(len(datasets))
    )
    # Only iterate as far as the SHORTEST dataset reaches - a longer
    # labels list than the data previously raised IndexError here.
    row_count = min([len(labels)] + [len(d) for d in datasets]) if datasets else 0
    data_rows = "".join(
        f"    {{ name: '{labels[i]}', " + ", ".join(f"v{j}: {datasets[j][i]}" for j in range(len(datasets))) + " },"
        for i in range(row_count)
    )

    # Radar needs polar axes instead of Cartesian, and scatter uses ZAxis.
    if chart_type == "radar":
        axes = ["PolarAngleAxis", "PolarRadiusAxis"]
        axes_markup = '      <PolarAngleAxis dataKey="name" />\n      <PolarRadiusAxis />'
    elif chart_type == "scatter":
        axes = ["XAxis", "YAxis", "ZAxis"]
        axes_markup = '      <XAxis dataKey="x" type="number" />\n      <YAxis dataKey="y" type="number" />'
    else:
        axes = ["CartesianGrid", "XAxis", "YAxis"]
        axes_markup = '      <CartesianGrid strokeDasharray="3 3" />\n      <XAxis dataKey="name" />\n      <YAxis />'

    # Build the import list without empty slots - "import { RadarChart, ,
    # XAxis ... }" is a syntax error the file would never survive.
    imports = [comp] + axes + ["Tooltip", "Legend", "ResponsiveContainer"]
    import_line = ", ".join(dict.fromkeys(imports))

    return f"""// React + Recharts - {chart_type} chart
import {{ {import_line} }} from 'recharts';

const data = [
{data_rows}
];

const Chart = () => (
  <ResponsiveContainer width="100%" height={300}>
    <{comp} data={{data}}>
{axes_markup}
      <Tooltip />
      <Legend />
{series}
    </{comp}>
  </ResponsiveContainer>
);

export default Chart;"""


def print_chartjs_templates():
    print("""/* ===== Chart.js Templates ===== */

<!-- 1. Line Chart -->
<canvas id="lineChart"></canvas>
<script>
new Chart(document.getElementById('lineChart'), {
  type: 'line',
  data: { labels: ['Jan','Feb','Mar'], datasets: [{ label: 'Users', data: [10, 20, 15], borderColor: '#2563EB', tension: 0.3 }] },
  options: { responsive: true }
});
</script>

<!-- 2. Bar Chart -->
<canvas id="barChart"></canvas>
<script>
new Chart(document.getElementById('barChart'), {
  type: 'bar',
  data: { labels: ['Q1','Q2','Q3'], datasets: [{ label: 'Revenue', data: [25, 40, 35], backgroundColor: '#F97316', borderRadius: 6 }] },
  options: { responsive: true }
});
</script>

<!-- 3. Pie Chart -->
<canvas id="pieChart"></canvas>
<script>
new Chart(document.getElementById('pieChart'), {
  type: 'doughnut',
  data: { labels: ['SaaS','B2B','Other'], datasets: [{ data: [40, 35, 25], backgroundColor: ['#2563EB','#F97316','#10B981'] }] },
  options: { responsive: true, plugins: { legend: { position: 'bottom' } } }
});
</script>""")


def print_recharts_templates():
    print("""/* ===== Recharts Templates (React) ===== */

// 1. Line Chart
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
const data = [{ name: 'Jan', users: 10 }, { name: 'Feb', users: 20 }, { name: 'Mar', users: 15 }];
const App = () => (
  <ResponsiveContainer width="100%" height={300}>
    <LineChart data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="users" stroke="#2563EB" />
    </LineChart>
  </ResponsiveContainer>
);

// 2. Bar Chart
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
const data = [{ name: 'Q1', revenue: 25 }, { name: 'Q2', revenue: 40 }];
const App = () => (
  <ResponsiveContainer width="100%" height={300}>
    <BarChart data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="revenue" fill="#F97316" radius={[6, 6, 0, 0]} />
    </BarChart>
  </ResponsiveContainer>
);

// 3. Pie Chart
import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from 'recharts';
const data = [{ name: 'SaaS', value: 40 }, { name: 'B2B', value: 35 }, { name: 'Other', value: 25 }];
const COLORS = ['#2563EB', '#F97316', '#10B981'];
const App = () => (
  <ResponsiveContainer width="100%" height={300}>
    <PieChart>
      <Pie data={data} dataKey="value" nameKey="name" outerRadius={100}>
        {data.map((_, i) => <Cell key={i} fill={COLORS[i % COLORS.length]} />)}
      </Pie>
      <Tooltip />
      <Legend />
    </PieChart>
  </ResponsiveContainer>
);""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chart Generator - Cyber-Rage")
    parser.add_argument("--chart", help="Chart type (line, bar, pie, doughnut, area, radar, scatter, polarArea)")
    parser.add_argument("--labels", help="Comma-separated labels (e.g. 'Jan,Feb,Mar')")
    parser.add_argument("--data", help="Comma-separated data values (e.g. '10,20,15'). Use ; for multiple datasets")
    parser.add_argument("--framework", default="chartjs", help="Framework: chartjs or recharts (default: chartjs)")
    parser.add_argument("--colors", help="Comma-separated colors (e.g. '#2563EB,#F97316')")
    parser.add_argument("--templates", help="Print templates (chartjs or recharts)")

    args = parser.parse_args()

    if args.templates:
        if args.templates == "chartjs":
            print_chartjs_templates()
        elif args.templates == "recharts":
            print_recharts_templates()
        else:
            print("Unknown templates: chartjs or recharts")
        sys.exit(0)

    if not args.chart:
        print("Specify --chart (line, bar, pie, doughnut, area, radar, scatter, polarArea) or --templates")
        sys.exit(1)

    valid = ["line", "bar", "pie", "doughnut", "area", "radar", "scatter", "polarArea"]
    if args.chart not in valid:
        print(f"Unknown chart: '{args.chart}'. Available: {', '.join(valid)}")
        sys.exit(1)

    if not args.labels or not args.data:
        print("--labels and --data are required")
        sys.exit(1)

    labels = split_csv(args.labels)
    raw_sets = [split_csv(d) for d in args.data.split(";")]
    datasets = [[float(v) for v in s] for s in raw_sets]
    if not any(datasets):
        print("No data provided", file=sys.stderr)
        sys.exit(1)

    colors = split_csv(args.colors) if args.colors else DEFAULT_COLORS

    if args.framework == "recharts":
        output = recharts_chart(args.chart, labels, datasets, colors)
        if output is None:
            print(f"Recharts does not support '{args.chart}' in this generator. Use chartjs.")
            sys.exit(1)
        print(output)
    else:
        print(chartjs_chart(args.chart, labels, datasets, colors))
