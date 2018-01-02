import requests, lagou_config, lagou_db, time,json
from lxml import html

class Lagou_crawler(object):
    def __init__(self):
        self.s = requests.session()
        self.headers = lagou_config.HEADERS


    def get_position(self, socialORnot, keyword, pagenum, city='全国'):
        headers = self.headers
        if str(socialORnot) == '0':
            headers['Referer'] =  'https://www.lagou.com/jobs/list_{}?city={}&cl=false&fromSearch=true&labelWords=&suginput='.format(keyword.encode('utf-8','strict'), city.encode('utf-8','strict'))
            API = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionResult={}&isSchoolJob={}'.format(city, 'true', '0')
        else:
            headers['Referer'] = 'https://www.lagou.com/jobs/list_{}?city={}isSchoolJob=1'.format(keyword.encode('utf-8','strict'), city.encode('utf-8','strict'))
            API = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionResult={}&isSchoolJob={}'.format(city, 'true', '1')
        if pagenum == '1':
            firstORnot = 'true'
        else:
            firstORnot = 'false'
        data = {
            'first': firstORnot,
            'pn': pagenum,
            'kd': keyword
        }
        time.sleep(3)
        r = self.s.post(API, headers=headers, data=data)
        return r

    '''
    def get_company(self, socialORnot, keyword, firstORnot, pagenum, city='全国'):
        headers = self.headers
        if str(socialORnot) == '0':
            headers['Referer'] =  'https://www.lagou.com/jobs/list_{}?city={}&cl=false&fromSearch=true&labelWords=&suginput='.format(keyword, city)
            API = 'https://www.lagou.com/jobs/companyAjax.json?city={}&needAddtionResult={}&isSchoolJob={}'.format(city, 'true', '0')
        else:
            headers['Referer'] = 'https://www.lagou.com/jobs/list_{}?city={}isSchoolJob=1'.format(keyword, city)
            API = 'https://www.lagou.com/jobs/companyAjax.json?city={}&needAddtionResult={}&isSchoolJob={}'.format(city, 'true', '1')
        data = {
            'first': firstORnot,
            'pn': pagenum,
            'kd': keyword
        }
        r = self.s.post(API, headers=headers, data=data)
        return r
    '''

    def parse_pagenums(self, response):
        json_data = json.loads(response.content)
        page_size = len(json_data['content']['positionResult']['result'])
        total_count = int(json_data['content']['positionResult']['totalCount'])
        page_numbers = total_count // page_size + 1
        if total_count % page_size == 0:
            page_numbers = page_numbers - 1
        if page_numbers>30:
            page_numbers = 30
        return page_numbers


    def parse_json(self, response):
        json_data = json.loads(response.content)
        if json_data['success'] is True:
            job_information = []
            page_size = len(json_data['content']['positionResult']['result'])
            for i in range(page_size):
                cell_information = []
                positionId = json_data['content']['positionResult']['result'][i]['positionId']
                positionName = json_data['content']['positionResult']['result'][i]['positionName']
                companyId = json_data['content']['positionResult']['result'][i]['companyId']
                companyFullName = json_data['content']['positionResult']['result'][i]['companyFullName']
                city = json_data['content']['positionResult']['result'][i]['city']
                district = json_data['content']['positionResult']['result'][i]['district']
                jobNature = json_data['content']['positionResult']['result'][i]['jobNature']
                industryField = json_data['content']['positionResult']['result'][i]['industryField']
                salary = json_data['content']['positionResult']['result'][i]['salary']
                cell_information.append(str(positionId))
                cell_information.append(str(positionName))
                cell_information.append(str(companyId))
                cell_information.append(str(companyFullName))
                cell_information.append(str(city))
                cell_information.append(str(district))
                cell_information.append(str(jobNature))
                cell_information.append(str(industryField))
                cell_information.append(str(salary))
                job_information.append(cell_information)
            return job_information
        else:
            return None

    def store_userdata_to_mongo(self, list):
        new_profile = lagou_db.Lagou_Position(
            positionId = list[0],
            positionName = list[1],
            companyId = list[2],
            companyFullName = list[3],
            city = list[4],
            district = list[5],
            jobNature = list[6],
            industryField = list[7],
            salary = list[8],
        )
        new_profile.save()
        print('Position(ID:%s) has saved.' % list[0])
