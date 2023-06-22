import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025))
        & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(15, 5))
  ax.plot(df.index, df['value'], color='red')
  ax.set(xlabel='Date',
         ylabel='Page Views',
         title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.groupby([(df.index.year), (df.index.month)]).mean()
  df_bar = df_bar.unstack()

  fig, ax = plt.subplots(figsize=(15, 10))
  df_bar.plot(kind='bar', ax=ax)
  ax.set_xlabel('Years')
  ax.set_ylabel('Average Page Views')
  ax.legend(title='Months', labels=[f'Month {i}' for i in range(1, 13)])
  ax.set_title('Average Daily Page Views for Each Month (2016-2019)')
  # Draw bar plot

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  fig, axs = plt.subplots(ncols=2, figsize=(20, 8))
  sns.boxplot(x='year', y='value', data=df_box, ax=axs[0])
  sns.boxplot(x='month',
              y='value',
              data=df_box,
              ax=axs[1],
              order=[
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                'Oct', 'Nov', 'Dec'
              ])
  axs[0].set_xlabel('Year')
  axs[0].set_ylabel('Page Views')
  axs[0].set_title('Year-wise Box Plot (Trend)')
  axs[1].set_xlabel('Month')
  axs[1].set_ylabel('Page Views')
  axs[1].set_title('Month-wise Box Plot (Seasonality)')

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
