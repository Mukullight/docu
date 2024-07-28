# Nulls and outs

The function identifies the location of the null values and the outliers and returns the indexes of the values


Finds the locations of null values and outliers in a DataFrame, and drops columns with categorical variables.

Parameters:
df (pd.DataFrame): The input DataFrame.

q1 (float): The lower quartile value. Default is 0.25.

q3 (float): The upper quartile value. Default is 0.75.


Returns:
dict: A dictionary with two keys 'nulls' and 'outliers', each containing the locations of null values and outliers respectively.


pd.DataFrame: The DataFrame after dropping categorical columns.

``` python

def nulls_and_outs(df, q1=0.05, q3=0.95):
    # Drop categorical columns
    df = df.select_dtypes(exclude=["object", "category"])

    null_locations = {}
    outlier_indices = {}

    # Identify null values
    nulls = df.isnull()
    for col in df.columns:
        null_indices = nulls.index[nulls[col]].tolist()
        if null_indices:
            null_locations[col] = null_indices

    # Iterate over numeric columns
    for col in df.select_dtypes(include="number").columns:
        # Calculate quartiles and IQR
        Q1 = df[col].quantile(q1)
        Q3 = df[col].quantile(q3)
        IQR = Q3 - Q1

        # Define outlier boundaries
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Find indices of outliers
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)].index.tolist()

        # Store outliers in dictionary
        outlier_indices[col] = outliers

    return {
        "upper": upper_bound,
        "lower": lower_bound,
        "nulls": null_locations,
        "outliers": outlier_indices,
    }, df



```




