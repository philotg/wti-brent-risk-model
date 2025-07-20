from statsmodels.tsa.stattools import adfuller, kpss

def adf_test(series):
    result = adfuller(series)
    return {'statistic': result[0], 'p_value': result[1], 'critical_values': result[4]}

def kpss_test(series):
    result = kpss(series, regression='c')
    return {'statistic': result[0], 'p_value': result[1], 'critical_values': result[3]}