import urllib.request
import lxml.html

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

req = urllib.request.Request(r'https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?ssoauth=1&loadingjs=1&o=dwebmge&cache=1595693886342')
f = urllib.request.urlopen(req)
page = f.read()

tree = lxml.html.fromstring(page)
imgurl = "https://ndltd.ncl.edu.tw" + \
      tree.xpath(".//img")[0].get('src')

print(imgurl)

req = urllib.request.Request("https://ndltd.ncl.edu.tw/gs32/images/random_validationimgs/XF.l4v_1595691820.jpg?v=1595691820")
f = urllib.request.urlopen(req)
img = f.read()

open('out.jpg', 'wb').write(img)
        

   
        



