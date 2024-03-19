# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import datetime 
import sqlite3

from scrapy.exceptions import DropItem

class ItNewsPipeline:
    def __init__(self):
        self.conn = sqlite3.connect('D:/github/crawling/database_db.db', isolation_level=None)
        self.c = self.conn.cursor()

    # 최초 1회 실행 
    def open_spider(self, spider):
        spider.logger.info('Spider Pipeline Started')
        self.c.execute("CREATE TABLE IF NOT EXISTS IT_NEWS_DATA(id INTEGER PRIMARY KEY AUTOINCREMENT, headline text, contents text, parent_link text, article_link text, crawled_time text)")

    # ITEM 건수별 실행
    def process_item(self, item, spider):
        if not item.get('contents') is None:
            crwaled_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # 크롤링 시간 필드 추가 
            item['crawled_time'] = crwaled_time

            # 데이터 -> DB 삽입
            self.c.execute('INSERT INTO IT_NEWS_DATA(headline, contents, parent_link, article_link, crawled_time) VALUES(?, ?, ?, ?, ?);', tuple(item[data] for data in item.keys()))

            # 로그 
            spider.logger.info('Item to DB inserted.')
        
            return item
        else:
            raise DropItem('Dropped Item. Because This Contents is Empty')
        
    # 마지막 1회 실행 
    def close_spider(self, spider):
        spider.logger.info('Spider Pipeline Stopped')
        self.conn.commit()
        self.conn.close()
