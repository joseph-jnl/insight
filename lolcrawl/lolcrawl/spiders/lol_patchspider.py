import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
import time
import re


class LolSpider(CrawlSpider):
    name = "patch_data"
    allowed_domains = ['nerfplz.com']
    start_urls = ['http://www.nerfplz.com/search/label/Patch Notes?max-results=40']
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//span[@class="rmlink"]'),
             callback='parse_patch'),
        Rule(LinkExtractor(restrict_xpaths='//span[@id="blog-pager-older-link"]'))
     )

    def parse_patch(self, response):

        patch = response.xpath('//h1[@class="post-title entry-title"]/text()').extract()
        patch = re.findall(r"[-+]?\d*\.\d+|\d+", patch[0])

        # Patch date
        date = response.xpath(
            '//span[@class="post-timestamp"]/text()').extract()
        dt = datetime.strptime(
            date[0].replace('\n', ' '), ' %b %d, %Y %I:%M %p ')
        release_date = time.mktime(dt.timetuple())

        # Champ list
        champs = response.xpath('//div[@class="post-body entry-content"]//b//following-sibling::text()').extract()
        while '\n' in champs: champs.remove('\n')
        champs = [x.replace(' ', '').replace("'", '').replace("'", '').lower() for x in champs]


        filename = 'patchnotes.txt'

        # Save changes
        with open(filename, 'a') as f:
            s = str(patch[0]) + '|'
            f.write(s)

        with open(filename, 'a') as f:
            s = str(release_date)
            f.write(s)

        changes = response.xpath(
            '//div[@class="post-body entry-content"]//b//text()').extract()
        change_track = 0

        if any("buffs" in s.lower() for s in changes):
            # Buffs
            with open(filename, 'a') as f:
                s = '|' + 'buffs:' + champs[0]
                f.write(s)
                change_track += 1
        else:
            with open(filename, 'a') as f:
                s = '|'
                f.write(s)
                change_track += 1

        if any("nerfs" in s.lower() for s in changes):
            # Nerfs
            with open(filename, 'a') as f:
                s = '|' + 'nerfs:' + champs[change_track]
                f.write(s)
        else:
            with open(filename, 'a') as f:
                s = '|'
                f.write(s)
                change_track += 1
                
        with open(filename, 'a') as f:
            s = '\n'
            f.write(s)
        self.log('Saved file %s' % filename)
        print(str(patch[0]))