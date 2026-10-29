from src.data_loader import load_data
from src.analysis import analyze_missing, handle_missing, compute_correlations
from src.charts import groupby_stats, plot_histograms, plot_boxplots, plot_bars,  plot_heatmap, plot_scatter

def run_eda(name):
    data = load_data(name)
    print(data)

    analyze_missing(tips)

    handle_missing(tips)

    compute_correlations(tips, [('total_bill', 'tip'), ('total_bill', 'size'), ('size', 'tip')])

    print(groupby_stats(tips, ['day', 'time'], ['tip', 'tip_pct']))

    plot_histograms(tips, ['total_bill', 'tip'])

    plot_boxplots(tips, [('day', 'tip'), ('time', 'total_bill')])
    plot_bars(tips, 'day', 'tip')
    plot_bars(tips, 'smoker', 'tip')

    plot_heatmap(tips)

    plot_scatter(tips, 'total_bill', 'tip', 'smoker')
    plot_scatter(tips, 'total_bill', 'tip', 'time')