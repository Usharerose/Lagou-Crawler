import lagou_crawler, lagou_config, time, os
from multiprocessing.dummy import Pool
from threading import Lock

class main_program(object):
    def __init__(self):
        self.crawler = lagou_crawler.Lagou_crawler()
        self.social = lagou_config.SOCIALorNOT
        self.keyword = lagou_config.KEYWORD
        self.city = lagou_config.CITY

    def get_page_information(self, pagenum):
        page_content = self.crawler.get_position(socialORnot=self.social, keyword=self.keyword, pagenum=pagenum, city=self.city)
        if pagenum == '1':
            page_nums = self.crawler.parse_pagenums(page_content)
        else:
            page_nums = None
        job_list = self.crawler.parse_json(page_content)
        return page_nums, job_list


def main():
    total_list = []
    
    def crawl_by_multi(page):
        page_content = get_information.get_page_information(page)[1]
        Lock().acquire()
        total_list.extend(page_content)
        print('Page %s has been crawled.' %page)
        Lock().release()

    start = time.time()
    
    get_information = main_program()
    page_nums, first_page_content = get_information.get_page_information(pagenum='1')
    total_list.extend(first_page_content)
    print('Page 1 has been crawled.')
    page_num_list = [str(x) for x in range(2, page_nums+1)]

    pool = Pool(os.cpu_count()*2)
    result = pool.map_async(func=crawl_by_multi, iterable=page_num_list)
    pool.close()
    pool.join()
    end = time.time()
    print('爬虫用时%s秒。' %(end-start))
    
    countA = 0
    countB = 1
    for content in total_list:
        lagou_crawler.Lagou_crawler().store_userdata_to_mongo(content)
        countA = countA + 1
        if (countA == 15)|(content == total_list[-1]):
            print('Page %d has been saved.' %countB)
            countA = 0
            countB = countB + 1


if __name__ == '__main__':
    main()
