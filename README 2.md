### 1、登陆接口

- 请求的URL地址

POST https://crm.iy-cd.com/wns-ciycrmapp/appLoginController/passwordLogin

- 参数
phoneNumber=18280055584&password=dCfjzCJyUsnNzUWH8kBxEQ%3D%3D&memberid=&memberId=&mobile=&token=&language=zh&store=002

- 返回
{
    "flag": true,
    "message":"操作成功",
    "result":{
        "phoneNumber":"18280055584"
        "memberid": "9518097003664",
        "token": "999a1315112512412412412"
    },
    "count":0
}

- 密码验证
  
  1、AES加密  字符集:utf8(unicode), 填充： （Pkcs5Padding), 密码: winnersoftiyccrm,
  模式: ECB， 编码: Base64
  
  2、在线密码 ：https://www.ssleye.com/aes_cipher.html
  

### 2、部分内容定义

- {"flag":true,"message":"操作成功!","result":{"storem":[{"text":"春熙店","value":"001"},{"text":"双楠店","value":"002"},{"text":"锦华店","value":"003"},{"text":"建设路店","value":"004"},{"text":"高新店","value":"005"},{"text":"温江店","value":"006"},{"text":"眉山店","value":"007"},{"text":"绿地店","value":"008"},{"text":"华府大道店","value":"101"}]},"count":0}



### 3、积分查询接口

- 请求的URL地址

POST https://crm.iy-cd.com/wns-ciycrmapp/appHomeController/getPointsChangeDetail 


- (1)、茅台查询接口和参数

 recordid=218&level=3&storeId=002&goodsId=467&eid=544&pikeId=&isspike=2&memberid=9518097003664&memberId=9518097003664&mobile=18280055584&token=266696171F3478083C0C12B4F37FFCC2&language=zh&store=002

 - (1)、返回内容
 "flag":true,"result":{"systemDate":"2020-04-24 21:54:19","getPointsChangeDetail":{"recordid":"218","goodsName":"飞天53%vol 500ml贵州茅台酒带杯1499元/瓶购买名额","pointsChange":"3000.00","goodsPreview":"https://truecrm.iy-cd.com:443null","goodsShow":"/data/uploads/2020/03/26/1585209777860F224.jpeg|/data/uploads/2020/03/18/1584532564748F695.jpeg|/data/uploads/2020/03/18/1584532564767F939.jpeg|/data/uploads/2020/03/26/1585209796422F846.jpeg|/data/uploads/2020/03/18/1584532564821F920.jpeg","goodsIntroduce":"/data/uploads/2020/03/26/1585209814191F685.jpeg","goodsBuy":"积分兑换购买名额：3000积分预约购买1瓶/人，6000积分预约购买2瓶/人。预约成功后，将扣除伊＋会员积分，扣除积分不能撤销，不能退回。每位会员每自然月内仅可预购一次，每自然季度仅可预购二次，每次预购不超过2瓶。","startTime":"2020-1-21 00:00:00","endTime":"2020-12-31 00:00:00","goodsCount":"0","changeCount":"0","changeLimit":"28","userLevel1":"3","userLevelName1":"白金卡","url":"https://truecrm.iy-cd.com:443","limitednum":"2","isEnable":"1","isspike":"2"}},"count":0}
 

- (2)、手帕查询参数
recordid=288&level=3&storeId=002&goodsId=556&eid=642&pikeId=&isspike=0&memberid=9518097003664&memberId=9518097003664&mobile=18280055584&token=266696171F3478083C0C12B4F37FFCC2&language=zh&store=002

- (2)、返回内容

{"flag":true,"result":{"systemDate":"2020-04-24 21:44:53","getPointsChangeDetail":{"recordid":"288","goodsName":"伊藤洋华堂订制手帕","pointsChange":"200.00","goodsPreview":"https://truecrm.iy-cd.com:443null","goodsShow":"/data/uploads/2020/04/07/1586242317352F399.jpeg|/data/uploads/2020/04/07/1586242317369F926.jpeg|/data/uploads/2020/04/07/1586242317393F921.jpeg|/data/uploads/2020/04/07/1586242317410F322.jpeg|/data/uploads/2020/04/07/1586242317429F243.jpeg","goodsIntroduce":"/data/uploads/2020/04/07/1586242317445F734.jpeg","goodsBuy":"每位会员凭效验码至所报名预约店铺会员中心核销领取，每个ID号限领一份，数量有限领完即止。","startTime":"2020-4-13 00:00:00","endTime":"2020-5-31 00:00:00","goodsCount":"199","changeCount":"199","changeLimit":"540","userLevel1":"3","userLevelName1":"白金卡","url":"https://truecrm.iy-cd.com:443","limitednum":"1","exchangeStartTime":"2020-4-13 00:00:00","exchangeEndTime":"2020-5-31 00:00:00","isEnable":"1","isspike":"0"}},"count":0}


### 4、兑换接口

- 请求URL地址

POST https://crm.iy-cd.com/wns-ciycrmapp/appHomeController/doPointsChange HTTP/1.1

-  参数

changeCount=1&recordid=288&goodsId=556&storeId=002&eid=642&pikeId=&isspike=0&validate=&memberid=9518097003664&memberId=9518097003664&mobile=18280055584&token=266696171F3478083C0C12B4F37FFCC2&language=zh&store=002

- 返回

{"flag":true,"message":"兑换成功","result":true,"count":0}



### 5、临时比较

- https://crm.iy-cd.com/wns-ciycrmapp/appHomeController/doPointsChange?changeCount=1&recordid=288&goodsId=556&storeId=002&eid=642&pikeId=&isspike=0&validate=&memberid=9518097003664&memberId=9518097003664&mobile=18280055584&token=D0E91E315A7ACE2B99233CCA5DC5881C&language=zh&store=002

changeCount=1&recordid=288&goodsId=556&storeId=002&eid=642&pikeId=&isspike=0&validate=&memberid=9518097003664&memberId=9518097003664&mobile=18280055584&token=17787459E5F799CDE6B6BEAA1C6B6BDA&language=zh&store=002
changeCount=1&recordid=288&goodsId=556&storeId=002&eid=642&pikeId=&isspike=0&validate=&memberid=9518097003664&memberId=9518097003664&mobile=18280055584&token=D0E91E315A7ACE2B99233CCA5DC5881C&language=zh&store=002




### 6、Header 头里的Referer参数

- 兑换手绢:Referer:
https://crm.iy-cd.com/wns-ciycrmapp/pages/ciycrm/app/home/pt0102.ftl?recordid=288&store=&storeId=002&level=3&goodsId=556&eid=642&pikeId=&isspike=0

- 兑换茅台 Referer:
https://crm.iy-cd.com/wns-ciycrmapp/pages/ciycrm/app/home/pt0102.ftl?recordid=218&store=%E5%8F%8C%E6%A5%A0%E5%BA%97&storeId=002&level=3&goodsId=467&eid=544&pikeId=&isspike=0
