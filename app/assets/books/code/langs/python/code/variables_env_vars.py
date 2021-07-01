# Environment Variables in Python

Set your application secrets, load, and retrieve them easily

1.  Current bash session
Access all the variables you’ve set through your code until you’re using the terminal without closing
>export AWS_USER_ID="joeid"
⚠ No spaces in between the equals sign on either side and your secret key within double quotes.

2.  .env file with your app

AWS_DB_URL="my_db_url"
AWS_USER_ID="joeid"
AWS_USER_PWD="1234"

add this filename in your .gitignore file, in order to protect it from your all-knowing version control system

```python
import os
db_url = os.environ.get('AWS_DB_URL', 'sqlite:////')   # default value is ‘sqlite:////’ (return None if not present and no var set)
```

3. dotenv package

>pip install python-dotenv
```python
from dotenv import load_dotenv
load_dotenv() # read all vars from .env
db_url = os.environ.get('AWS_DB_URL', 'sqlite:////')   # default value is ‘sqlite:////’ (return None if not present and no var set)
```
