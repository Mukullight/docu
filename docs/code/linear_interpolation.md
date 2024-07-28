# Linear interpolation

The following libraries are imported for the calculation 


``` python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import plotly.graph_objs as go
from plotly.subplots import make_subplots

``` 


python code for calculation of the new coordinates of the missing or the null values 

Perform linear interpolation on a set of data points.

Parameters:
x_points (array-like): Known x-values of the data points.
y_points (array-like): Known y-values of the data points.
x_new (array-like): New x-values at which to interpolate the y-values.
Returns:
array-like: Interpolated y-values at x_new points.



```python

def li_int(x_points, y_points, x_new):
    
    # Input validation
    if len(x_points) != len(y_points):
        raise ValueError("x_points and y_points must have the same length")
    if not (np.all(np.diff(x_points) > 0) or np.all(np.diff(x_points) < 0)):
        raise ValueError(
            "x_points must be strictly monotonic (either increasing or decreasing)"
        )

    # Perform linear interpolation
    interpolator = interp1d(x_points, y_points, kind="linear")
    y_new = interpolator(x_new)

    return y_new


```




