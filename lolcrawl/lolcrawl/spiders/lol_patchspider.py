import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LolSpider(CrawlSpider):
    name = "patch_data"
    allowed_domains = ['nerfplz.com']
    # start_urls = ['http://www.nerfplz.com/search/label/Patch Notes?max-results=50']
    start_urls = ['http://www.nerfplz.com/search/label/Patch Notes?max-results=5']
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//span[@class="rmlink"]'),
             callback='parse_patch'),
        Rule(LinkExtractor(restrict_xpaths='//span[@id="blog-pager-older-link"]'))
    )

    def parse_patch(self, response):
        date = response.xpath('//span[@class="post-timestamp"]/text()').extract()
        change_type = response.xpath('//div[@class="post-body entry-content"]//b//text()').extract()
        champs = response.xpath('//div[@class="post-body entry-content"]//b//following-sibling::text()').extract()

        
        
        # # popularity
        # d_pop = response.xpath(
        #     './/*[@id="mainContent"]/div[2]/div[1]/div[1]/script').extract()

        # # win rate
        # d_wr = response.xpath(
        #     './/*[@id="mainContent"]/div[2]/div[1]/div[2]/script').extract()

        # # ban rate
        # d_br = response.xpath(
        #     './/*[@id="mainContent"]/div[2]/div[1]/div[3]/script').extract()

        # # date released
        # d_release = response.xpath(
        #     './/*[@id="mainContent"]/div[1]/div[4]/div/div[1]/text()'
        # ).extract()

        # filename = 'diamond_raw.txt'

        # with open(filename, 'a') as f:
        #     s = champ_name + '\n^' + d_pop[0] + '\n^' + d_wr[0] + '\n^' + \
        #         d_br[0] + '\n^' + d_release[0] + \
        #         '\n|'
        #     f.write(s)
        # self.log('Saved file %s' % filename)
