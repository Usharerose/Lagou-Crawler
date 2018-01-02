#生成User-Agent
from fake_useragent import UserAgent

import requests

#MongoDB数据库
HOST = 'localhost'
PORT = 27017
DATABASE = 'Lagou'

#搜索用信息
KEYWORD = '爬虫'
CITY = '北京'
SOCIAL = '0'
SCHOOL = '1'
SOCIALorNOT = SCHOOL

'''
职位搜索API
SOCIAL_POSITION_SEARCH = "https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionResult={}&isSchoolJob={}".format(CITY, "true", SOCIAL)
SCHOOL_POSITION_SEARCH = "https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionResult={}&isSchoolJob={}".format(CITY, "true", SCHOOL)
公司搜索API
SOCIAL_COMPANY_SEARCH = "https://www.lagou.com/jobs/companyAjax.json?city={}&needAddtionResult={}&isSchoolJob={}".format(CITY, "true", SOCIAL)
SCHOOL_COMPANY_SEARCH = "https://www.lagou.com/jobs/companyAjax.json?city={}&needAddtionResult={}&isSchoolJob={}".format(CITY, "true", SCHOOL)
API_Referer
SOCIAL_REFERER = "https://www.lagou.com/jobs/list_{}?labelWords=&fromSearch=true&suginput".format(KEYWORD)
SCHOOL_REFERER = "https://www.lagou.com/jobs/list_{}?isSchoolJob=1".format(KEYWORD)
'''

#请求头
HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 请手动使用浏览器访问拉勾网后提取
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'RA-Sid': 's_10944_r2x9ak474125_202',
    'RA-Ver': '3.2.9',
    'User-Agent': UserAgent().random,
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'
}

#首次向拉勾网请求返回的请求头中的'Set-Cookie'无效，仅能爬取前几页内容
'''
r = requests.get('https://www.lagou.com', headers=HEADERS)
cookies = r.headers['Set-Cookie']
HEADERS['Cookie'] = cookies
'''
