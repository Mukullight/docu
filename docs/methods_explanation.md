Linear Interpolation:

Use Case: When the data changes smoothly between points and a simple approximation is sufficient.
#### Advantages
+ Easy to implement and less computational requirements
+ Quick to compute and effective for larger data sets with loads of missing values
+ have more local control, less sensitive to outliers, works well with noisy data, handles discontinous data well
#### Disadvantages
> not good for complex patterns, sharp corners, poor performance for smooth functions, requires higher order derivatives 



## Linear Interpolation

Linear interpolation is a method used to estimate the value of a function or a set of data points within the range of known values. It is particularly useful for filling in gaps in data or for making predictions about unknown values based on a linear relationship between known points. The concept is straightforward and involves drawing a straight line between two known points and using this line to estimate intermediate values.

### How Linear Interpolation Works

1. **Identify Known Points**: Start with two known data points, \((x_1, y_1)\) and \((x_2, y_2)\), where \(x_1\) and \(x_2\) are the x-values, and \(y_1\) and \(y_2\) are the corresponding y-values.

2. **Target Point**: Determine the x-value (\(x\)) at which you want to estimate the y-value (\(y\)).

3. **Formula**: Use the linear interpolation formula to find the estimated y-value:
   $$ y = y_1 + \frac{(x - x_1) (y_2 - y_1)}{(x_2 - x_1)} $$

   This formula is derived from the slope of the line between the two known points and the concept that the change in y should be proportional to the change in x.

4. **Calculate**: Substitute the known values into the formula and solve for \(y\).





## Lagrange interpolation

Lagrange interpolation is a method for constructing a polynomial that passes through a given set of points. If you have a set of \(n + 1\) data points \((x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n)\), the Lagrange interpolating polynomial \(P(x)\) is given by:

$$
P(x) = \sum_{i=0}^{n} y_i \ell_i(x)
$$

where \(\ell_i(x)\) are the Lagrange basis polynomials defined as:

$$
\ell_i(x) = \prod_{\substack{0 \leq j \leq n \\ j \neq i}} \frac{x - x_j}{x_i - x_j}
$$

## Steps to Construct the Lagrange Interpolating Polynomial

1. **Identify the Data Points:**

   Given points \((x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n)\).

2. **Construct the Basis Polynomials:**

   For each \(i = 0, 1, \ldots, n\):

   $$
   \ell_i(x) = \prod_{\substack{0 \leq j \leq n \\ j \neq i}} \frac{x - x_j}{x_i - x_j}
   $$

3. **Form the Interpolating Polynomial:**

   Combine the basis polynomials \(\ell_i(x)\) with the corresponding \(y_i\) values:

   $$
   P(x) = \sum_{i=0}^{n} y_i \ell_i(x)
   $$


## Advantages
+ Straight forward, tries to give the best fit
+ works for equidistant and the non equidistant points, no need to solve linear systems
#### Disadvantages 
> **Runge's phenomenon** for higher degree and the widely spaced points --> oscillations occur at edges of intervals leading to poor approximation
> higher computational costs and does not work for dynamic dataset, higher storage requirements

## Polynomial Interpolation

Polynomial interpolation is a method of estimating values between known data points by constructing a polynomial that passes through all the given points.
#### Advantages 
+ gives the exact fit, provides analytical expression for further theoretical analysis 
+ allows for flexibility in choosing the base polynomial 
#### Disadvantages 
> same as those of lagrange 
### General Polynomial Interpolation

Given a set of \(n + 1\) data points \((x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n)\), we seek a polynomial \(P(x)\) of degree at most \(n\) such that:

$$
P(x_i) = y_i \quad \text{for} \quad i = 0, 1, \ldots, n
$$

A general polynomial of degree \(n\) can be written as:

$$
P(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n
$$
--------------------------------------------------------------------------------------------------------------------------------------
The coefficients 
$$  a_0 , a_1, \ldots, a_n $$
are determined by solving a system of linear equations that arise from substituting the given points into the polynomial equation.



## Cubic Spline Interpolation

Cubic spline interpolation is the most widely used spline interpolation method. It fits a cubic polynomial between each pair of data points and ensures smooth transitions by matching the first and second derivatives at the data points.


#### Advantages
+ gives more local control by breaking down the domain into smaller fragments, more precise interpolation
+ smoother interpolation and reduces oscillations, differentiable, piecewise continous

#### Disadvantages 
> More computataional effort, hard to choose appropriate boundaries, could lead to overfitting, takes significant resources, higher memory usage, beyond range interpolation

### Formulation

Given \(n + 1\) data points \((x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n)\), the cubic spline interpolation constructs \(n\) cubic polynomials \(S_i(x)\) for \(i = 0, 1, \ldots, n-1\), such that:

$$
S_i(x) = a_i + b_i (x - x_i) + c_i (x - x_i)^2 + d_i (x - x_i)^3
$$

### Conditions

1. **Interpolation Condition:**

   The spline must pass through all data points:

   $$
   S_i(x_i) = y_i \quad \text{and} \quad S_i(x_{i+1}) = y_{i+1} \quad \text{for} \quad i = 0, 1, \ldots, n-1
   $$

2. **Continuity Condition:**

   The spline must be continuous at each interior data point:

   $$
   S_i(x_{i+1}) = S_{i+1}(x_{i+1}) \quad \text{for} \quad i = 0, 1, \ldots, n-2
   $$

3. **Smoothness Condition:**

   The first and second derivatives must be continuous at each interior data point:

   $$
   S_i'(x_{i+1}) = S_{i+1}'(x_{i+1}) \quad \text{and} \quad S_i''(x_{i+1}) = S_{i+1}''(x_{i+1}) \quad \text{for} \quad i = 0, 1, \ldots, n-2
   $$

4. **Boundary Conditions:**

   There are different types of boundary conditions that can be applied:
   - **Natural spline:** The second derivative at the endpoints is zero:
     $$
     S_0''(x_0) = 0 \quad \text{and} \quad S_{n-1}''(x_n) = 0
     $$
   - **Clamped spline:** The first derivative at the endpoints is specified:
     $$
     S_0'(x_0) = f'(x_0) \quad \text{and} \quad S_{n-1}'(x_n) = f'(x_n)
     $$

