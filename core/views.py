import random 
import string

def _gref(string_length) :
    assembly = string.hexdigits
    return ''.join(random.choice(assembly) for i in range(string_length))

def _vemail(email):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def _vurl(url):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def _vphone(phone):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))
