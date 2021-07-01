# TSDB - Time Series Database

- https://pub.towardsai.net/understand-time-series-components-with-python-4bc3e2ba1189 ** toadd


A database is a collection of data that is organized and stored in a correlated manner.
TSDB is a database designed and optimized to register and store data that is always associated with a specific point in time or that uses a timestamp. This structure makes it easy to analyze events chronologically over time from any data source. Not only that, a TSDB can receive concurrent inputs, allowing us to analyze and store several streams of data simultaneously and even analyze them combined.

Otimized to write data fast, have a superior compression algorithm, and have a considerably faster query engine. 
Since all records are timestamped, the ledger of the data points is natively organized. These databases are configured to efficiently deliver the data to several processing engines, simulating the original data stream. 

Uses:
- Historical reference point for any type of data stream.
- Performs complex data analysis and predictive modeling. 
- predictive models for sales, demands, trends, cycles, and analyzing rapidly changing prices in financial markets.
- in medical operations by storing and streaming information from inserted or wearable devices. 

Can track a massive amount of real-time data with almost instant speed and storage efficiency. This proposal sounds especially appealing for industrial applications.


![](assets/books/data/time_series_db/time_series_terms.png)
## Time series data
A time series is a series of data points indexed in time. Usually, a time series is a sequence taken at successive, equally spaced points in time: a sequence of discrete-time data. Examples of time series are heights of ocean tides, counts of sunspots, and the daily closing value of the Dow Jones Industrial Average.

## Popular TSDM Systems

TSDB database management system

download.page(data/time_series_db/infludb.md)
download.page(data/time_series_db/prometheus.md)
download.page(data/time_series_db/kdb+.md)


- https://medium.com/@satyam-kumar/train-multiple-time-series-forecasting-models-in-one-line-of-python-code-615f2253b67a
- https://www.codeproject.com/Articles/5281930/An-Ultrafast-Light-Timeseries-Storage-Engine-LMDB
- https://pub.towardsai.net/understand-time-series-components-with-python-4bc3e2ba1189 ** toadd
