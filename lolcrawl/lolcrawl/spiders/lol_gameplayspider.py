import scrapy
import csv

class LolSpider(scrapy.Spider):
    name = "gameplay_data"
    
    def start_requests(self):

        start_url = 'http://www.leagueofgraphs.com/champions/stats'

        with open('champs.csv', 'r') as f:
            reader = csv.reader(f)
            champs = list(reader)    
        champsf = [val.lower() for sublist in champs for val in sublist]
        
        for champ in champsf:
            champ_url = start_url + '/' + champ + '/lcs'
            yield scrapy.Request(url=champ_url, callback=self.parse)

    def parse(self, response):
        champ_name = response.url.split('/')[-2]

        #popularity
        d_pop = response.xpath('.//*[@id="mainContent"]/div[2]/div[1]/div[1]/script').extract()

        #win rate
        d_wr = response.xpath('.//*[@id="mainContent"]/div[2]/div[1]/div[2]/script').extract()

        #ban rate
        d_br = response.xpath('.//*[@id="mainContent"]/div[2]/div[1]/div[3]/script').extract()

        #date released
        d_release = response.xpath('.//*[@id="mainContent"]/div[1]/div[4]/div/div[1]/text()').extract()

        filename = 'lcs_raw.txt'

        with open(filename, 'a') as f:
            s = champ_name + '\n^' + d_pop[0] + '\n^' + d_wr[0] + '\n^' + \
                d_br[0] + '\n^' + d_release[0] + \
                '\n|'
            f.write(s)
        self.log('Saved file %s' % filename)

