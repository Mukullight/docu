# Splines interpolation

The following libraries are imported for the calculation 


```python
import numpy as np
from scipy.interpolate import CubicSpline
import plotly.graph_objs as go
``` 


python code for calculation of the new coordinates of the missing or the null values 


Performs polynomial interpolation of given degree for the given data points and x_new,
and calculates the error rate.


Parameters:
x (array-like): x-coordinates of the data points.
y (array-like): y-coordinates of the data points.
degree (int): Degree of the polynomial to fit.
x_new (array-like): New x-coordinates for which to compute interpolated y values.


Returns:
tuple: Interpolated y-values corresponding to x_new, Mean Squared Error (MSE).

```python
def compute_cubic_spline_multi(x, y, x_new_sets):
    """
    Computes cubic spline interpolation for multiple sets of new x-coordinates.

    Parameters:
    x (array-like): x-coordinates of the data points.
    y (array-like): y-coordinates of the data points.
    x_new_sets (array-like or list of array-like): Multiple sets of new x-coordinates for the spline curves.

    Returns:
    list of np.ndarray: Corresponding y-coordinates for the spline curves.
    """
    if len(x) != len(y):
        raise ValueError("The input arrays x and y must have the same length.")
    if len(x) < 2:
        raise ValueError(
            "At least two data points are required for spline interpolation."
        )

    # Create a cubic spline interpolation
    cs = CubicSpline(x, y, bc_type="natural")

    y_new_sets = []
    for x_new in x_new_sets:
        y_new_sets.append(cs(x_new))

    return y_new_sets

```




