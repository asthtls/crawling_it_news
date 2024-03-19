import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ItNewsItem


class NewsSpider(CrawlSpider):
    name = "news"
    allowed_domains = ["news.daum.net","v.daum.net"]
    # start_urls = ["https://news.daum.net/breakingnews/digital"]
    start_urls = [
        "https://news.daum.net/breakingnews/digital"
    ]

    # 링크 크롤링 규칙(정규표현식 사용 추천)
    # rules = [
    #     # page=\d$ or page=\d+$ : 2자리수 페이지 크롤링
    #     Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse_headline'),
    # ]
    rules = [
        Rule(
            LinkExtractor(
                allow=r'/breakingnews/digital\?page=\d+'
            ),
            callback='parent_parse',
            follow=True,
        ),
    ]

    def parent_parse(self, response):
        # 부모 URL 로깅 
        self.logger.info('Parent Response URL : %s' %response.url)
        
        for url  in response.css('ul.list_news2.list_allnews > li > div.cont_thumb'):
            # 기사 URL 
            article_url = url.css('strong.tit_thumb > a::attr(href)').get().strip()
            # 요청 
            yield scrapy.Request(article_url, self.parse_child, meta={'parent_url' : response.url})
    
    def parse_child(self, response):
        self.logger.info('------------------------')
        self.logger.info('Resonse From Parent URL : %s' %response.meta['parent_url'])
        self.logger.info('Child Response Status : %s ' %response.status)
        self.logger.info('Child Response URL : %s ' %response.url)

        headline = response.css('h3.tit_view::text').get().strip()

        # 본문
        c_list = response.css('div.article_view p::text').getall()  
        contents = ' '.join([paragraph.strip() for paragraph in c_list])  # 각 paragraph를 strip하고 공백으로 join


        yield ItNewsItem(headline=headline, contents=contents, parent_link=response.meta['parent_url'], article_link=response.url)
        