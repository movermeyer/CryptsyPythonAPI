CryptsyPythonAPI
================

API for Cryptsy.com Exchange utilizing completely built-in functions and utilities of Python 2.7.

Author's Note
-------------
This API wrapper is a fork of [ScriptProdigy's CryptsyPythonAPI](https://github.com/ScriptProdigy/CryptsyPythonAPI).

Example Usage
-------------
Create buy order for dgc, market id 26, then cancels all orders you have for dgc
```python
import Cryptsy
Exchange = Cryptsy.Cryptsy('KEY HERE', 'SECRET HERE')
print(Exchange.createOrder(26, "Buy", 100, 0.00000001))       # Buy 100 dgc at .00000001 each
print(Exchange.cancelMarketOrders(26))                        # Cancels all orders in market 26, dgc
```

License
-------
This piece of software is licensed under the GPL2 license, see license.txt.
