# API

## TRANQUILIZER
Deploy a REST API with one line by decorating your functions.
https://github.com/ContinuumIO/tranquilizer
The tranquilized API is documented with Swagger and is accessible in your web browser at http://localhost:8086.
Tranquilizer can be used with either Jupyter Notebooks (.ipynb) or Python script files (.py).

> conda install -c conda-forge tranquilizer

from tranquilizer import tranquilize

```python
@tranquilize()
def order(cheese):
    '''I'd like to buy some cheese!'''
    return "I'm afraid we're fresh out of {}, Sir.".format(cheese)
```
    
> curl -G http://localhost:8086/order --data-urlencode "cheese=Red Leicester"
"I'm afraid we're fresh out of Red Leicester, Sir."    