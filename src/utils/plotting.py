import matplotlib.pyplot as plt


def plot_rolling_statistics(series, window=30):
    rolling_mean = series.rolling(window=window).mean()
    rolling_std = series.rolling(window=window).std()

    plt.figure(figsize=(12, 6))
    plt.plot(series.index, series, label='Original Series', color='green')
    plt.plot(series.index, rolling_mean, label=f'Rolling Mean ({window} days)', color='blue')
    plt.plot(series.index, rolling_std, label=f'Rolling Std Dev ({window} days)', color='orange')
    plt.title('Rolling Mean and Standard Deviation')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()