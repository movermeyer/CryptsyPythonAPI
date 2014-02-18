CryptsyPythonAPI
================

API for Cryptsy.com Exchange utilizing completely built-in functions and utilities of Python 2.7.

Note: the next version of this API wrapper will introduce A LOT of API changes
so be warned, here be dragons.

Author's Note
-------------
This API wrapper is a fork of [ScriptProdigy's CryptsyPythonAPI](https://github.com/ScriptProdigy/CryptsyPythonAPI).

Example Usage
-------------
Create buy order for dgc, market id 26, then cancels all orders you have for dgc
```python
from Cryptsy import API
exchange = API('KEY HERE', 'SECRET HERE')
print(exchange.create_order(26, "Buy", 100, 0.00000001))       # Buy 100 dgc at .00000001 each
print(exchange.cancel_all_market_orders(26))                   # Cancels all orders in market 26, dgc
```

Running the tests
-----------------
If you want to run the tests, first create a virtualenv and install all
requirements.

    virtualenv .env
    . .env/bin/activate
    pip install -r requirements.txt

Then, using pytest, run the tests:

    py.test test_cryptsy.py

Development
----------
Development is done in the obviously named develop branch. If you want to
contribute, please do your commits in that branch so merging them isn't a
pain.

Donate
------
Support development by tipping me a beer (because programming with beer is
inherently better than programming without)!

[![Support via Gittip](https://rawgithub.com/chris---/Donation-Badges/master/gittip.jpeg)](https://www.gittip.com/jaapz)


License
-------
This piece of software is licensed under the GPL2 license, see `license`.
