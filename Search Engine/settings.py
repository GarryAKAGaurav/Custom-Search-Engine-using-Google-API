SEARCH_KEY = " YOUR OWN KEY PUBLISHED FROM GOOGLE SEARCH ENGINE API "
SEARCH_ID = "c27ab142bcd024db3"
COUNTRY = "in"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT = 20

import os
if os.path.exists("private.py"):
    from private import *
