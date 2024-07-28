# Usage examples

The examples below illustrate the usage of the modules the stock data is downloaded using the y finance module 

+ importing the required modules 
```python 
import plotly.graph_objs as go
import yfinance as yf
import pandas as pd
``` 


downloading the stock data 


```python 
ftse_100_tickers = ["AAL.L", "ABF.L", "ADM.L", "AHT.L", "ANTO.L"]
start_date = "2023-01-01"
end_date = "2023-12-31"
stock_data_dict = {}
for ticker in ftse_100_tickers:
    print(f"Fetching data for {ticker}")
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data_dict[ticker] = stock_data

``` 
+ adding null values of the data to simulate bad data 

```python 

# adding nullvalues 
for ticker, stock_data in stock_data_dict.items():
    stock_data['Close'] = stock_data['Close'].sample(frac=0.9)
``` 
+ plotting the null values using the plotly modules 



```python 

# plotting the null values 

fig = go.Figure()
for ticker, stock_data in stock_data_dict.items():
    fig.add_trace(
        go.Scatter(x=stock_data.index, y=stock_data['Close'], name=ticker)
    )
fig.update_layout(
    title="Stock Data",
    xaxis_title="Date",
    yaxis_title="Close Price (GBP)",
    legend_title="Company",
    plot_bgcolor='black',   # Set the background color of the plot
    paper_bgcolor='black',  # Set the background color of the paper
    xaxis=dict(showgrid=False), # Remove x-axis grid lines
    yaxis=dict(showgrid=False),  # Remove y-axis grid lines
    font=dict(color='white')
)
plt.show()
``` 
+ importing the required functions from the nullval module 

```python 

# plotting the null values 
# replacing the nullvalues using linear interpolation
# from nullval import linear_interpolation

from nullval.loader import load_to_df
from nullval.loader import nulls_and_outs
from nullval import linear_interpolation
from nullval import polynomial_interpolation
from nullval import lagrange_interpolation
from nullval import spline_interpolation

```


+ new plots are made from the replaced indexes using lagrange method

```python 

"""


the methods is imported from the module and utilised


"""


for ticker, stock_data in stock_data_dict.items():
    # Get the index of non-null values
    valid_indices = stock_data['Close'].notna()

    # Interpolate the 'Close' values
    stock_data['Close'] = lagrange_interpolation.lagrange_interpolation(
        stock_data.index[valid_indices],
        stock_data['Close'][valid_indices],
        stock_data.index
    )

# Create a plotly figure
fig = go.Figure()

# Add a line for each stock to the figure
for ticker, stock_data in stock_data_dict.items():
    fig.add_trace(
        go.Scatter(x=stock_data.index, y=stock_data['Close'], name=ticker)
    )

# Update layout
fig.update_layout(
    title="Stock Data",
    xaxis_title="Date",
    yaxis_title="Close Price (GBP)",
    legend_title="Company",
    plot_bgcolor='black',   # Set the background color of the plot
    paper_bgcolor='black',  # Set the background color of the paper
    xaxis=dict(showgrid=False), # Remove x-axis grid lines
    yaxis=dict(showgrid=False),  # Remove y-axis grid lines
    font=dict(color='white') # Set the font color to white for better visibility
)

# Show plot
fig.show()


``` 
