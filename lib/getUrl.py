import re 
import urllib.parse as urlparse
from urllib.parse import parse_qs

  
def findUrl(sentense): 
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,sentense)       
    return [x[0] for x in url] 

# Driver Code 
# string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org/'
# print("Urls: ", findUrl(string)) 

# parse url argument
url = 'http://foo.appspot.com/abc?def=ghi'
parsed = urlparse.urlparse(url)
print(parsed.query)