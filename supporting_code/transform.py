import pandas as pd


# simple function to transform data into required from
def transform(warps):
    warps['warp time'] = pd.to_datetime(warps['warp time'], format='%Y-%m-%d %H:%M:%S')
    warps['month'] = pd.DatetimeIndex(warps['warp time']).month
    warps['year'] = pd.DatetimeIndex(warps['warp time']).year
    warps['year month'] = warps['warp time'].dt.to_period('M')
    warps['year month'] = warps['year month'].astype(str)
    return warps
