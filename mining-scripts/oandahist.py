import sys
import json

from oandapyV20.contrib.factories import InstrumentsCandlesFactory
from oandapyV20 import API

access_token = "5cc68709f7b53e5ef9679be1e57d47a9-eb33c86e95b956c7e60088ca17242855"

client = API(access_token=access_token)

_from = sys.argv[1]
_to = sys.argv[2]
gran = sys.argv[3]
instr = sys.argv[4]

params = {
    "granularity": 'M1',
    "from": _from,
    "to": _to
#     "count": 5000
}

def cnv(r, h):
    for candle in r.get('candles'):
        ctime = candle.get('time')[0:19]
        try:
            rec = "{time},{complete},{o},{h},{l},{c},{v}".format(
                time=ctime,
                complete=candle['complete'],
                o=candle['mid']['o'],
                h=candle['mid']['h'],
                l=candle['mid']['l'],
                c=candle['mid']['c'],
                v=candle['volume'],
            )
        except Exception as e:
            print(e, r)
        else:
            h.write(rec+"\n")

# with open("/tmp/{}.{}.out".format(instr, gran), "w") as O:
#     for r in InstrumentsCandlesFactory(instrument=instr, params=params):
#         print("REQUEST: {} {} {}".format(r, r.__class__.__name__, r.params))
#         rv = client.request(r)
#         cnv(r.response, O)

with open("/Users/diegomedina-bernal/Desktop/MadGeniusAlgorithmic/mining-scripts{}.{}.csv".format(instr, gran), "w") as O:
    for r in InstrumentsCandlesFactory(instrument=instr, params=params):
        print("REQUEST: {} {} {}".format(r, r.__class__.__name__, r.params))
        rv = client.request(r)
        cnv(r.response, O)






