import requests
# from bs4 import BeautifulSoup
# import urllib.request
import shutil
import eventlet
eventlet.monkey_patch()
from IPython.display import display, clear_output
import requests as rq
from bs4 import BeautifulSoup
import datetime
import sched
import time
import json

stock_list = ['0056']

def download_pic(num, pic_url):
    with eventlet.Timeout(10):
        # pic_num = './doc/pic/'+ str(num) + '.jpg'
        img_data = requests.get(pic_url, headers = header)
        if img_data.status_code == 200:
            print(img_data.text)
            # with open(pic_num, 'wb') as handler:
            #     handler.write(img_data)

def stock_crawler(targets):#每日股價資料
    clear_output(wait = True)
    stock_list = '|'.join('tse_{}.tw'.format(target) for target in targets)
    site = "http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=" + stock_list
    response = rq.get(site)
    data = json.loads(response.text)
    print(data)

        
if __name__ == '__main__':
    # download_pic(1,url)
    stock_crawler(stock_list)
    
   
        



