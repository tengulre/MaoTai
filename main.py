#-*-conding:utf-8-*-
#YiTeng, MaoTai .
#Create : 2020-04-28
#Author : tengulre@qq.com 
#  

import requests
import ssl
import csv
import json
import time
import os
import urllib3
import argparse
from requests.auth import HTTPBasicAuth
from threading import Thread




#封装一个类
class YiTeng_MaoTai:
    def __init__(self,username,password,storeid):
        self.username = username
        self.password = password
        self.storeid = storeid
        self.running = False
        self.cookies_server_id = None   # 登陆后的Cookies
        self.threadid

    #线程开始的地方
    def start(self):
        self.threadid = Thread(target=self.run, args=()).start()
    
    def stop(self):
        self.running = False
    
    def join(self):
        self.threadid.join()
    # 执行积分兑换；
    def doPointsChange(self):
        url = 'https://crm.iy-cd.com/wns-ciycrmapp/appHomeController/doPointsChange'
        
        #茅台酒的POST请求结构
        '''
        postData = {
            'changeCount': 1,   #抢购数量;
            'recordid':'218',   # 
            'goodsId':'467',    # 商品ID
            'storeId':self.storeid, # 门店ID
            'eid':'544',  
            #'pikeId':'',
            #'isspike': 2,       #查询接口返回的数据;
            #'validate':'',
            'memberid': self.memberId,
            'memberId': self.memberId,
            'mobile': self.username,
            'token': self.token,
            'language':'zh',
            'store':self.storeid
        }
        '''
        #手帕POST请求参数;
        postData = {
            'changeCount': 1,   #抢购数量;
            'recordid':'228',   # 
            'goodsId':'556',    # 商品ID
            'storeId':self.storeid, # 门店ID
            'eid':'642',  
            'pikeId':'',
            'isspike': 0,       #查询接口返回的数据;
            'validate':'',
            'memberid': self.memberId,
            'memberId': self.memberId,
            'mobile': self.username,
            'token': self.token,
            'language':'zh',
            'store':self.storeid
        }
        '''
        #茅台请求头信息
       
        Headers = {
            "Host": "crm.iy-cd.com",
            "Connection": "keep-alive",
            "Accept" : "application/json, text/javascript, */*; q=0.01",
            "Origin" : "https://crm.iy-cd.com",
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Fetch-Dest": "empty",
            "User-Agent" : "Mozilla/5.0 (Linux; Android 9; MIX 2 Build/PKQ1.190118.001; wv) \
                 AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/27.636364)",
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
            "Sec-Fetch-Site" : "same-origin",
            "Sec-Fetch-Mode" : "cors",
            "Referer" : "https://crm.iy-cd.com/wns-ciycrmapp/pages/ciycrm/app/home/pt0102.ftl?recordid=218&store=%E5%8F%8C%E6%A5%A0%E5%BA%97&storeId="+self.storeid+"&level=3&goodsId=467&eid=544",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        '''

        #手帕卷请求头
        Headers = {
            "Host": "crm.iy-cd.com",
            "Connection": "keep-alive",
            "Accept" : "application/json, text/javascript, */*; q=0.01",
            "Origin" : "https://crm.iy-cd.com",
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Fetch-Dest": "empty",
            "User-Agent" : "Mozilla/5.0 (Linux; Android 9; MIX 2 Build/PKQ1.190118.001; wv) \
                 AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/27.636364)",
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
            "Sec-Fetch-Site" : "same-origin",
            "Sec-Fetch-Mode" : "cors",
            "Referer" : "https://crm.iy-cd.com/wns-ciycrmapp/pages/ciycrm/app/home/pt0102.ftl?recordid=288&store=%E5%8F%8C%E6%A5%A0%E5%BA%97&storeId="+self.storeid+"&level=3&goodsId=556&eid=642&pikeId=&isspike=0",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookies": self.cookies_server_id
        }
        
        requests.packages.urllib3.disable_warnings()
        cookies = dict(SERVER_ID=self.cookies_server_id)
        res = requests.post(url, data=postData, headers=Headers,cookies=cookies, verify=False,timeout=(3,7))
        return res

    def run(self):
        self.login()
        time.sleep(3)
        i = 0
        filename = open('./'+self.username+'.txt','a+')
        while self.running:
            try:
                res = self.doPointsChange()
                filename.writelines(res.text+'\n')
                filename.flush()
                print('Mobile : ' + self.username + ' is actived , try it on times( '+str(i)+' )')
                i = i + 1
                time.sleep(0.1)
            except requests.Timeout:
                print('Expression: mobile->'+self.username)
                self.proxyflag = True
                pass
            except requests.ConnectionError:
                pass
        filename.close()

            
    #用户登陆，获取会员ID
    def login(self):
        url = 'https://crm.iy-cd.com/wns-ciycrmapp/appLoginController/passwordLogin'
        postData = {
            'phoneNumber': self.username,
            'password': self.password
        }

        Headers = {
            "Host": "crm.iy-cd.com",
            "Connection": "keep-alive",
            "Accept" : "application/json, text/javascript, */*; q=0.01",
            "Origin" : "https://crm.iy-cd.com",
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Fetch-Dest": "empty",
            "User-Agent" : "Mozilla/5.0 (Linux; Android 9; MIX 2 Build/PKQ1.190118.001; wv) \
                 AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/27.636364)",
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
            "Sec-Fetch-Site" : "same-origin",
            "Sec-Fetch-Mode" : "cors",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        ## 屏蔽SSL警告信息
        requests.packages.urllib3.disable_warnings()
        try:
            res = requests.post(url, data= postData, headers=Headers, verify=False,timeout=(3,7))
            self.cookies_server_id = res.cookies['SERVER_ID']
            print(res.cookies['SERVER_ID'])
            flag = json.loads(res.text).get('flag')
            if flag == True:
                print('Mobile '+self.username + ' is login successful.')
                self.token = json.loads(res.text).get('result').get('token')
                self.memberId = json.loads(res.text).get('result').get('memberid')
                self.running = True
                return True
            else:
                print('Mobile ('+self.username+') was login failed.')
                self.running = False
                return False
        except requests.Timeout:
            print('Login as ' + self.username+'Timeout')
            pass
        except requests.ConnectionError:
            pass


    #构造Header里的BasicAuth认证信息;
    def base_code(self,username, password):
        str = '%s:%s' % (username, password)
        encodestr = base64.b64encode(str.encode('utf-8'))
        return '%s' % encodestr.decode() 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-pro','--proxy',dest='proxy',action='store',type=str,default=None)
     
    args = parser.parse_args()

    print('Loading users and passwords messages...')
    thread_lst = []

    with open('./users.lst','r',encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            t = YiTeng_MaoTai(row[0],row[1],row[2])
            thread_lst.append(t)
        for t in thread_lst:
            t.start()
    
    try:
        while True:
            pass
            time.sleep(2)
    except KeyboardInterrupt:
        pass
    for t in thread_lst:
        t.stop()
    exit()
    
    print('Finished')
