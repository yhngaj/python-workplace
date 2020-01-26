import scrapy
from hsi.items import Hsi_tr_Item, w_Date_summary

class CBBCSpider(scrapy.Spider):
    name = 'hsi_cbbc_outstanding_boc'

    #allowed_domains = ['example.com']

    start_urls = [
        'http://www.bocifp.com/en/cbbc/cbbc-hsi-os'
    ]

    def parse(self, response):

        #date_and_close = Date_summary(busiDate = response.css("#date_list option::text").get(), dayClose = response.css(".msg_table span::text").get())
        #yield date_and_close
        inputDate = True

        for r in response.xpath('//div[@class="chart_tooltip"]'):

            #["\r\n\t\t\t\t\tCall Level:29,900-29,999\r\n\t\t\t\t\t", " Outstanding:73.36\r\n\t\t\t\t\t", " Related Futures Quantity:106.96\r\n\t\t\t\t  "]
            trString = r.xpath('./text()').getall()

            if inputDate:

                w_date_and_close = w_Date_summary(BusiDate = response.css("#date_list option::text").get(), DayClose = response.css(".msg_table span::text").get(), Ranging = trString[0].strip().split(":")[1], futuresQuan = trString[2].strip().split(":")[1])
                yield w_date_and_close
                inputDate = False
            else:

                outputTr = Hsi_tr_Item(Ranging = trString[0].strip().split(":")[1], futuresQuan = trString[2].strip().split(":")[1])
                yield outputTr

