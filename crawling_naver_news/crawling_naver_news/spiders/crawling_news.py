import scrapy
import json
import time
from ..items import CrawlingNaverNewsItem  # 필요한 Item import 확인


class CrawlingNewsSpider(scrapy.Spider):
    name = "crawling_news"
    allowed_domains = ["news.naver.com", "n.news.naver.com"]
    start_urls = ["https://news.naver.com/section/105"]

    def parse(self, response):
        # 페이지에 있는 기사 항목들을 선택
        articles = response.css('li.sa_item')
        for article in articles:
            # 각 기사의 제목과 링크 추출
            title = article.css('.sa_text_title .sa_text_strong::text').get()
            link = article.css('.sa_text_title::attr(href)').get()
            
            # 제목이나 링크가 None인 경우를 처리
            if title is None or link is None:
                self.logger.info(f"누락된 데이터를 발견했습니다. 제목: {title}, 링크: {link}")
                continue
            
            # 추출된 데이터 저장
            item = CrawlingNaverNewsItem(headline=title, article_link=link)
            yield item
        
        # '기사 더 보기' 버튼에 해당하는 AJAX 요청의 예시 URL(실제 사이트에서 확인 필요)
        ajax_url = 'https://news.naver.com/section/moreArticles/ajax'
        yield scrapy.Request(url=ajax_url, callback=self.parse_ajax, meta={'page': 2})  # 시작 페이지 번호를 메타 데이터로 전달

    def parse_ajax(self, response):
        page = response.meta.get('page', 2)
        # AJAX 응답에서 다음 페이지 기사 데이터 추출 로직 구현
        
        # 다음 페이지 기사 목록 추출 로직 (예제 코드는 실제 AJAX 응답 구조에 따라 작성되어야 합니다.)
        
        next_page = page + 1
        # 실제 '기사 더 보기' 버튼의 요청을 처리하는 AJAX URL 구성
        next_ajax_url = f'https://news.naver.com/section/moreArticles/ajax?page={next_page}'
        # 조건에 따라 재귀적으로 다음 페이지 요청
        yield scrapy.Request(url=next_ajax_url, callback=self.parse_ajax, meta={'page': next_page})





    # # 링크 크롤링 규칙(정규표현식 사용 추천)
    # # rules = [
    # #     # page=\d$ or page=\d+$ : 2자리수 페이지 크롤링
    # #     Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse_headline'),
    # # ]
    # rules = [
    #     Rule(
    #         LinkExtractor(
    #             allow=r'/breakingnews/digital\?page=\d+'
    #         ),
    #         callback='parent_parse',
    #         follow=True,
    #     ),
    # ]

    # def parent_parse(self, response):
    #     # 부모 URL 로깅 
    #     self.logger.info('Parent Response URL : %s' %response.url)
        
    #     for url  in response.css('ul.list_news2.list_allnews > li > div.cont_thumb'):
    #         # 기사 URL 
    #         article_url = url.css('strong.tit_thumb > a::attr(href)').get().strip()
    #         # 요청 
    #         yield scrapy.Request(article_url, self.parse_child, meta={'parent_url' : response.url})
    
    # def parse_child(self, response):
    #     self.logger.info('------------------------')
    #     self.logger.info('Resonse From Parent URL : %s' %response.meta['parent_url'])
    #     self.logger.info('Child Response Status : %s ' %response.status)
    #     self.logger.info('Child Response URL : %s ' %response.url)

    #     headline = response.css('h3.tit_view::text').get().strip()

    #     # 본문
    #     c_list = response.css('div.article_view p::text').getall()  
    #     contents = ' '.join([paragraph.strip() for paragraph in c_list])  # 각 paragraph를 strip하고 공백으로 join


    #     yield ItNewsItem(headline=headline, contents=contents, parent_link=response.meta['parent_url'], article_link=response.url)
        