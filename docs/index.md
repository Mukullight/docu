# Nullval

## Requirement analysis

Why is null val created ?


Nullval is a package created as a wrapper library with the collection of several numerical techniques spread across libraries 

+ The primary objective of the package is to help data scientists/ Quantitative developers and analysts to check and replace the missing/null values and outliers in api calls made for extracting financial data 
  
It is often the case when financial data is extracted using yahoo or bloomberg api calls the data is often unclean and requires a significant amount of developer hours spent on cleaning and formatting the data. To avoid this nullval is created




```plotly
--8<-- "assets/scatter.json"
```
### Directory structure

``` { .sh .no-copy }
.
├─ Home
│  |─Getting started/
|  |   |___ [installation] 
|  |   |___Creating a python virtual environment
|  |   |__ Installation Guide
│  |   
|  |_Demo.md
|  |   |__Null values
|  |   |__Outliers
|  |_General functions.md
|  |   |__load_to_df
|  |   |_nulls_and_outs
|  |   
|  |_lagrange_interpolation
|  |_polynomial_interpolation
|  |_spline_interpolation
|  |_linear_interpolation    
└─ mkdocs.yml
```



# Index

1. [installation] 
[installation]:getting-started.md
2. [why-nullval] 
[why-nullval]:explain.md
3. [Nulls_and_outs]
[Nulls_and_outs]:common-functions.md
4. [Theoretical-analysis]
[Theoretical-analysis]:methods_explanation.md
5. [license]
[license]:license.md
6. [tutorials]
[tutorials]:Blogs
