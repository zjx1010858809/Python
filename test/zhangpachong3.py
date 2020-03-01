import mpl_finance as mpf
import matplotlib as mpl
import matplotlib.pyplot as plt
import tushare as ts
import datetime
from matplotlib.pylab import date2num

start = '2019-01-01'
end = '2020-02-27'
k_d = ts.get_k_data('600588', start, end, ktype='D')
k_d.head()
k_d.date = k_d.date.map(lambda x: date2num(datetime.datetime.strptime(x, '%Y-%m-%d')))
quotes = k_d.values

fig, ax = plt.subplots(figsize=(8,5))
fig.subplots_adjust(bottom=0.2)
mpf.candlestick_ochl(ax, quotes, width=0.6, colorup='r', colordown='g', alpha=0.8)
#ax, quotes, width=0.6, colorrup='r', colordown='g', alpha=0.8
plt.grid(True)
ax.xaxis_date()

ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=30)
plt.show()