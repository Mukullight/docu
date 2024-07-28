# Lagrange interpolation

The following libraries are imported for the calculation 


``` python
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
``` 


python code for calculation of the new coordinates of the missing or the null values 


```python

def lagrange_interpolation(x_points, y_points, x_new):
    """
    Perform Lagrange interpolation on a set of data points.

    Parameters:
    x_points (array-like): Known x-values of the data points.
    y_points (array-like): Known y-values of the data points.
    x_new (array-like): New x-values at which to interpolate the y-values.

    Returns:
    array-like: Interpolated y-values at x_new points.
    """
    if len(x_points) != len(y_points):
        raise ValueError("x_points and y_points must have the same length")

    def lagrange_basis(j, x_point):
        basis = [
            (x_point - x_points[m]) / (x_points[j] - x_points[m])
            for m in range(len(x_points))
            if m != j
        ]
        return np.prod(basis)

    y_new = np.array(
        [
            sum(y_points[j] * lagrange_basis(j, xi) for j in range(len(x_points)))
            for xi in x_new
        ]
    )
    return y_new

```




