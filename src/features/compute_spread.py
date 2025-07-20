import pandas as pd

def compute_spread(wti, brent):
    spread = wti['Close'] - brent['Close']
    spread_df = pd.DataFrame({'Date': wti.index, 'Spread': spread})
    spread_df.set_index('Date', inplace=True)
    return spread_df

# import pandas as pd

# def compute_spread(wti, brent):
#     # Ensure the index is datetime for both DataFrames
#     wti.index = pd.to_datetime(wti.index)
#     brent.index = pd.to_datetime(brent.index)
    
#     # Compute the spread
#     spread = wti['Close'] - brent['Close']
    
#     # Create a DataFrame with the spread and use the datetime index
#     spread_df = pd.DataFrame({'Spread': spread}, index=wti.index)
#     return spread_df