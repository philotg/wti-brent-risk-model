#!/usr/bin/env python3
"""
WTI Front-Month Futures Ingestion via yfinance

Fetches the continuous front-month WTI crude oil futures contract ("CL=F")
from Yahoo Finance using the yfinance library.
"""

import os
import sys
import argparse

import pandas as pd
import yfinance as yf


def fetch_wti_front_month(start_date: str = None,
                          end_date: str = None,
                          period: str = None,
                          interval: str = "1d") -> pd.DataFrame:
    """
    Fetches front-month WTI futures from Yahoo Finance.

    You can either specify start/end dates, or a period (e.g. "1y", "6mo").

    Parameters
    ----------
    start_date : str, optional
        Earliest date to retrieve, in 'YYYY-MM-DD' format.
    end_date : str, optional
        Latest date to retrieve, in 'YYYY-MM-DD' format.
    period : str, optional
        Data period (e.g. '1y', '6mo', 'max'). Overrides start/end if given.
    interval : str, default '1d'
        Data interval (e.g. '1d', '1h', '1m').

    Returns
    -------
    pd.DataFrame
        A DataFrame indexed by Date, with columns
        ['Open','High','Low','Close','Adj Close','Volume'].
    """
    ticker = yf.Ticker("CL=F")

    if period:
        hist = ticker.history(period=period, interval=interval)
    else:
        hist = ticker.history(start=start_date, end=end_date, interval=interval)

    # yfinance returns a DatetimeIndex already
    return hist


def main():
    p = argparse.ArgumentParser(
        description="Download WTI front-month futures from Yahoo Finance"
    )
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--period",
        help="data period (e.g. '1y', '6mo', 'max')"
        )
    group.add_argument("--range",
                       nargs=2, metavar=('START','END'),
                       help="start and end dates (YYYY-MM-DD YYYY-MM-DD)")
    p.add_argument("--interval",
                   help="data interval (e.g. '1d', '1h')", default="1d")
    p.add_argument("--output",
                        help="output CSV file name", default="brent_crude_data.csv")
    args = p.parse_args()

    if args.period:
        df = fetch_wti_front_month(period=args.period, interval=args.interval)
    else:
        start, end = args.range
        df = fetch_wti_front_month(start_date=start,
                                   end_date=end,
                                   interval=args.interval)

    print(df.head())

    output_file = args.output
    df.to_csv(output_file)
    print(f"Data successfully saved to {output_file}")


if __name__ == "__main__":
    main()
