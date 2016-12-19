<!-- # Dictionaries shared among unit tests -->
<!-- Published: 2016-12-06 -->

I was recently writing some unit tests for some data serializer methods for a third party market data API in Django and one of my tests used a dictionary to mock a JSON response from an API.
I wanted to be ["DRY"](https://en.wikipedia.org/wiki/Don't_repeat_yourself) so I reused the same dictionary and using a few class properties, I modified the values to represent different scenarios where the data might be invalid (this API is not very stable).

Ex:

```python
from django.test import TestCase


class MarketIndexTestCase(TestCase):

    self.market_response = {
        "indexes": [
            {
                "id": "a023f176-328c-40eb-99a5-fe18c0b4eb32",
                "name": "Dow Jones Industrial Average",
                "is_data_only": True,
                "symbol": "INDU"
                "value": "19,237.25",
                "last_trade_time": "2016-12-06T17:48:40.000000Z"
            },
            {
                "id": "ae0fb991-5f6f-4e05-9a19-a50d040576ba",
                "name": "Nasdaq Composite Index",
                "symbol": "COMP"
                "value": "5,250.17",
                "last_trade_time": "2016-12-06T17:48:40.000000Z"
            },
            {
                "id": "ae0fb991-5f6f-4e05-9a19-a50d040576ba",
                "name": "S&P 500 Index",
                "symbol": "INX"
                "value": "2,208.81",
                "last_trade_time": "2016-12-06T17:48:40.000000Z"
            }
        ]
    }

    @property
    def mock_invalid_change_in_value(self):
        # Simulate an unexpected change in value
        data = self.market_response
        data['indexes'][0]['value'] = 'N/A'
        return data

    ... (some tests) ...
```

## The issue

The problem with the above code is that it is mutating the dictionary `self.market_response` and any tests that require the original `self.market_response` data will not be able to use it.

## The solution

Since dictionaries in python are mutable, we should expect that any change to the dictionary (see `mock_invalid_change_in_value`) will change the original dictionary. And because unit tests should be isolated, we should instead opt to use a copy of the dictionary in the `mock_invalid_change_in_value` `property` as such:

```python
import copy

@property
def mock_invalid_change_in_value(self):
    # Simulate an unexpected change in value
    data = copy.deepcopy(self.market_response)
    data['indexes'][0]['value'] = 'N/A'
    return data
```

doing so would create a copy, leaving the original dictionary untouched.
