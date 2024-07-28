# Use case 

This section contains some of the basic terminologies associated with the library and the importance of the library

## Definition
## Null values
Null values refer to missing or undefined entries in a dataset. In financial data, these can manifest as missing stock prices, transaction amounts, or other key metrics.

Problems with Null Values:

+ Inaccurate Analysis: Null values can skew statistical analyses and models, leading to incorrect conclusions about financial trends, risks, and opportunities.
+ Reduced Data Quality: Missing data reduces the completeness of the dataset, which can undermine the reliability of financial reports and forecasts.
+ Complicated Calculations: Financial computations often require complete datasets. Null values necessitate complex imputation methods or lead to exclusion of valuable data points, impacting the integrity of financial analysis.
+ Decision-Making Issues: Incomplete data can lead to poor decision-making by providing an incomplete picture of financial health or market conditions.



```plotly
--8<-- "assets/null.json"
```
## Outlier values
Outliers are data points that significantly deviate from the rest of the data. In financial datasets, these might be unusually high or low values for stock prices, trading volumes, or revenue figures.

Problems with Outlier Values:

+ Misleading Statistics: Outliers can distort statistical measures such as mean, variance, and correlations, leading to misleading insights and forecasts.
+ Model Performance Issues: Financial models and algorithms may be skewed by outliers, reducing their accuracy and reliability. For instance, predictive models might overfit to these anomalies, resulting in poor performance on new data.
+ Risk Management Challenges: Outliers can represent extreme events or anomalies that are not indicative of normal market conditions. Ignoring or misinterpreting these can lead to inadequate risk management and financial planning.
+ Operational Disruptions: In the context of transactions, outliers may signal fraudulent activities or errors that require investigation. Failure to address these can lead to operational inefficiencies or financial losses.

```plotly
--8<-- "assets/outlier.json"
```

-------------------