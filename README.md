## About MadGenius-Trading
The mission of this repository is to build experimental classfication and regression algorithms for Forex Trading. Most of these algorithms will be using 2D Time-Series data 

We do this by converting tabular data into chart data, then labeling **buy, sell, hold** signals based on the movement of the currency pair 

### Downloading Data
The very first thing you will want to do is run both notebooks:

**DataPrep-Train.ipynb** 
**DataPrep-Valid.ipynb**

*Update* 
If you check *oandahist.py* you will notice that when running the oanda script via terminal (or jupyter notebook), you will now have to place in granularity as a parameter 

Here is a quick dictionary explaining each value and what they represent

```python
granularity = {
    'S5': '5 seconds',
    'S10': '10 seconds',
    'S15': '15 seconds',
    'S30': '30 seconds',
    'M1': '1 minute',
    'M2': '2 minutes',
    'M3': '3 minutes',
    'M4': '4 minutes',
    'M5': '5 minutes',
    'M10': '10 minutes',
    'M15': '15 minutes',
    'M30': '30 minutes',
    'H1': '1 hour',
    'H2': '2 hours',
    'H3': '3 hours',
    'H4': '4 hours',
    'H6': '6 hours',
    'H8': '8 hours',
    'H12': '12 hours',
    'D': '1 day',
    'W': '1 week',
    'M': '1 month'
}
```
Thus when running:

```
!python {working_directory}/mining-scripts/oandahist.py 2018-01-01T00:00:00Z 2018-04-01T00:00:00Z H4 GBP_USD
```

will **now** have to be:

```
!python {working_directory}/mining-scripts/oandahist.py granularity 2018-01-01T00:00:00Z 2018-04-01T00:00:00Z H4 GBP_USD
```

Keep in mind *working_directory** is not a local variable within the notebook, in fact it shows my 'at the time' current working directory, so you will need to change that 

To find your current working directory just run:

```
!pwd
```
in a jupyter cell and it should output your current working directory

### Time Frame
As shown in this repository, I have only experimented with a few months of data. There is no restrictions on the timeframe, just keep in mind the file size in the end as everything will be converted to images 

### Indicators
My suggestion is that you experiment with indicators of your own. You will notivce we use **Moving Average 50** and **Bollinger Bands** but *as of 1/30/19* there seems to be a bug not displaying the indicators when converted to chart, eventually image 

