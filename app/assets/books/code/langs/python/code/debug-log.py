# LOG

- https://realpython.com/python-logging/


# urlcaller.py
import sys
import requests
response = requests.get(sys.argv[1])
print(response.status_code, response.content)


# urlcaller.py
import logging
import sys
import requests

logger = logging.getLogger(__name__)

try:
    response = requests.get(sys.argv[1])
except requests.exceptions.ConnectionError as e:
    logger.exception()
    print(-1, 'Connection Error')
else:
    print(response.status_code, response.content)

> python urlcaller.py http://thisurlprobablydoesntexist.com
'''
  File "/path/to/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7faf9d671860>: Failed to establish a new connection: [Errno -2] Name or service not known',))
-1 Connection Error
'''

# By default, Python will send log messages to standard error (stderr). 
# Redirecting stderr

>python urlcaller.py http://thisurlprobablydoesntexist.com 2> my-logs.log