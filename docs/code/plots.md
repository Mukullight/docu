# Plotting Linear Interpolation
``` python


def plot_li_int(x_points, y_points, x_new, y_new):
    """
    Plot the original data points and the interpolated values using Plotly.

    Parameters:
    x_points (array-like): Known x-values of the data points.
    y_points (array-like): Known y-values of the data points.
    x_new (array-like): New x-values at which y-values were interpolated.
    y_new (array-like): Interpolated y-values at x_new points.
    """
    fig = make_subplots(rows=1, cols=1)

    # Scatter plot of original data points
    fig.add_trace(
        go.Scatter(
            x=x_points,
            y=y_points,
            mode="markers",
            name="Data Points",
            marker=dict(color="black"),
        ),
        row=1,
        col=1,
    )

    # Line plot of interpolated values
    fig.add_trace(
        go.Scatter(
            x=x_new,
            y=y_new,
            mode="lines",
            name="Linear Interpolation",
            line=dict(color="red", dash="dash"),
        ),
        row=1,
        col=1,
    )

    # Update layout
    fig.update_layout(
        title="Linear Interpolation",
        xaxis_title="x",
        yaxis_title="y",
        showlegend=True,
        legend=dict(x=0.7, y=1.1),
        template="plotly_white",
    )

    # Show plot
    fig.show()


```
# Plotting lagrange interpolation
``` python

def plot_lagrange_interpolation(x_points, y_points, x_new, y_new):
    """
    Plot the Lagrange interpolation results using Plotly.

    Parameters:
    x_points (array-like): Known x-values of the data points.
    y_points (array-like): Known y-values of the data points.
    x_new (array-like): New x-values at which the y-values were interpolated.
    y_new (array-like): Interpolated y-values at x_new points.
    """
    data_points = go.Scatter(x=x_points, y=y_points, mode="markers", name="Data points")
    lagrange_curve = go.Scatter(
        x=x_new, y=y_new, mode="lines", name="Lagrange interpolation"
    )

    layout = go.Layout(
        title="Lagrange Interpolation", xaxis=dict(title="x"), yaxis=dict(title="y")
    )

    fig = go.Figure(data=[data_points, lagrange_curve], layout=layout)
    pio.show(fig)



```
# plotting polynomial interpolation
``` python

def plot_polynomial_interpolation(x, y, degree, x_new):
    """
    Performs polynomial interpolation, computes interpolated y values, and plots the results using Plotly.

    Parameters:
    x (array-like): x-coordinates of the data points.
    y (array-like): y-coordinates of the data points.
    degree (int): Degree of the polynomial to fit.
    x_new (array-like): New x-coordinates for which to compute interpolated y values.
    """
    # Perform polynomial interpolation and compute y values
    y_new = polynomial_interpolation(x, y, degree, x_new)

    # Plotting using Plotly
    fig = make_subplots(rows=1, cols=1)

    # Scatter plot of original data points
    fig.add_trace(
        go.Scatter(x=x, y=y, mode="markers", name="Data Points"), row=1, col=1
    )

    # Line plot of interpolated data
    fig.add_trace(
        go.Scatter(
            x=x_new,
            y=y_new,
            mode="lines",
            name=f"Polynomial Interpolation (Degree {degree})",
        ),
        row=1,
        col=1,
    )

    # Update layout
    fig.update_layout(
        title=f"Polynomial Interpolation (Degree {degree})",
        xaxis_title="x",
        yaxis_title="y",
        showlegend=True,
        legend=dict(x=0.7, y=1.1),
        template="plotly_white",
    )

    # Show plot
    fig.show()




```
# plotting splines interpolation
``` python

def plot_cubic_spline_multi(x, y, x_new_sets, y_new_sets):
    """
    Plots the original data points and multiple cubic spline interpolations using Plotly.

    Parameters:
    x (array-like): x-coordinates of the original data points.
    y (array-like): y-coordinates of the original data points.
    x_new_sets (list of array-like): Multiple sets of new x-coordinates for the spline curves.
    y_new_sets (list of np.ndarray): Corresponding y-coordinates for the spline curves.
    """
    fig = go.Figure()

    # Add the original data points
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="markers",
            name="Data points",
            marker=dict(color="blue", size=8),
        )
    )

    # Add the spline interpolations
    for i, (x_new, y_new) in enumerate(zip(x_new_sets, y_new_sets)):
        fig.add_trace(
            go.Scatter(
                x=x_new,
                y=y_new,
                mode="lines",
                name=f"Cubic spline interpolation {i + 1}",
                line=dict(width=2),
            )
        )

    # Update the layout
    fig.update_layout(
        title="Cubic Spline Interpolation",
        xaxis_title="x",
        yaxis_title="y",
        legend=dict(x=0, y=1),
        plot_bgcolor="black",
    )

    # Show the plot
    fig.show()



```
