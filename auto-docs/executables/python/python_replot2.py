import plotly.plotly as py
py.sign_in('TestBot', 'r1neazxo9w')

fig = py.get_figure("PlotBot", 5)

plot_url = py.plot(fig, filename="python-replot2")
