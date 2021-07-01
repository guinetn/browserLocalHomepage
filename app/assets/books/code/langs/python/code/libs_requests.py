'''
requests

Makes web requests really simple
Building on the most downloaded Python library in the world, urllib3. It 
https://pypi.org/project/requests
https://requests.readthedocs.io/en/master/
'''


# urlcaller.py
import sys
import requests
response = requests.get(sys.argv[1])
print(response.status_code, response.content)


>python urlcaller.py https://httpbin.org/status/200

>python urlcaller.py https://httpbin.org/status/500




# urlcaller.py
...
try:
    response = requests.get(sys.argv[1])
except requests.exceptions.ConnectionError:
    print(-1, 'Connection Error')
else:
    print(response.status_code, response.content)


# urlcaller.py
import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
# 200
r.headers['content-type']
# 'application/json; charset=utf8'
r.encoding
# 'utf-8'
r.text
# u'{"type":"User"...'
r.json()
# {u'disk_usage': 368627, u'private_gists': 484, ...}


# urlcaller.py
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
    
By default, Python will send log messages to standard error (stderr).    
redirecting stderr:
>python urlcaller.py http://thisurlprobablydoesntexist.com 2> my-logs.log