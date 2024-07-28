# Polynomial interpolation

The following libraries are imported for the calculation 


```python
import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
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

def polynomial_interpolation(x, y, degree, x_new):
    # Fit polynomial to data
    coefficients = np.polyfit(x, y, degree)
    polynomial = np.poly1d(coefficients)

    # Compute interpolated y-values for new x-coordinates
    y_new = polynomial(x_new)

    # Calculate mean squared error (MSE)
    y_pred = polynomial(x)
    mse = np.mean((y - y_pred) ** 2)

    return y_new

```




