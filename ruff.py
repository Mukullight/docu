import nullval 
import plotly.graph_objs as go
import yfinance as yf
import pandas as pd

from nullval.loader import load_to_df
from nullval.loader import nulls_and_outs
from nullval import linear_interpolation
from nullval import polynomial_interpolation
from nullval import lagrange_interpolation
from nullval import spline_interpolation

# Define the tickers and date range
ftse_100_tickers = ["AAL.L", "ABF.L", "ADM.L", "AHT.L", "ANTO.L"]
start_date = "2023-01-01"
end_date = "2023-12-31"
stock_data_dict = {}

# Fetch stock data for each ticker
for ticker in ftse_100_tickers:
    print(f"Fetching data for {ticker}")
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data_dict[ticker] = stock_data

# Introduce null values by randomly setting 10% of 'Close' values to NaN
for ticker, stock_data in stock_data_dict.items():
    stock_data['Close'] = stock_data['Close'].sample(frac=0.9)

# Create a plotly figure for the original data with null values
fig_original = go.Figure()
for ticker, stock_data in stock_data_dict.items():
    fig_original.add_trace(
        go.Scatter(x=stock_data.index, y=stock_data['Close'], name=f"{ticker} Original")
    )

fig_original.update_layout(
    title="Stock Data with Null Values",
    xaxis_title="Date",
    yaxis_title="Close Price (GBP)",
    legend_title="Company",
    plot_bgcolor='black',
    paper_bgcolor='black',
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    font=dict(color='white')
)

# Interpolate the null values using lagrange interpolation
for ticker, stock_data in stock_data_dict.items():
    valid_indices = stock_data['Close'].notna()
    stock_data['Close'] = lagrange_interpolation.lagrange_interpolation(
        stock_data.index[valid_indices],
        stock_data['Close'][valid_indices],
        stock_data.index
    )

# Create a plotly figure for the interpolated data
fig_interpolated = go.Figure()
for ticker, stock_data in stock_data_dict.items():
    fig_interpolated.add_trace(
        go.Scatter(x=stock_data.index, y=stock_data['Close'], name=f"{ticker} Interpolated")
    )

fig_interpolated.update_layout(
    title="Stock Data after Lagrange Interpolation",
    xaxis_title="Date",
    yaxis_title="Close Price (GBP)",
    legend_title="Company",
    plot_bgcolor='black',
    paper_bgcolor='black',
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    font=dict(color='white')
)

# Merge the original and interpolated plots together
fig_merged = go.Figure()

# Add the original data traces
for ticker, stock_data in stock_data_dict.items():
    fig_merged.add_trace(
        go.Scatter(x=stock_data.index, y=stock_data['Close'], name=f"{ticker} Original")
    )

# Add the interpolated data traces
for ticker, stock_data in stock_data_dict.items():
    fig_merged.add_trace(
        go.Scatter(x=stock_data.index, y=stock_data['Close'], name=f"{ticker} Interpolated", line=dict(dash='dot'))
    )

# Update the layout for the merged figure
fig_merged.update_layout(
    title="Original and Interpolated Stock Data",
    xaxis_title="Date",
    yaxis_title="Close Price (GBP)",
    legend_title="Company",
    plot_bgcolor='black',
    paper_bgcolor='black',
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    font=dict(color='white')
)

# Show the merged plot
fig_merged.show()
