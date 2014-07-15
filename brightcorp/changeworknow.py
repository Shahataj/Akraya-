"""This file is a Changeworknow spider created on top of the ATSSpider
scrapy crawl changeworknow url="http://isw.changeworknow.co.uk/dixons_retail/vms/e/vacancies/search/new"

sample url:
    http://isw.changeworknow.co.uk/wagamama/vms/e/wagamama/search/new
    http://isw.changeworknow.co.uk/gordonramsay/vms/e/gordonramsay/search/new
"""
import re
import urllib
import json

from urlparse import urljoin, urlparse
from datetime import datetime

from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

from brightcorp.base.atsspiders import ATSSpider
from brightcorp.items import BrightcorpItemLoader

class Changeworknow(ATSSpider):

    name = 'changeworknow'

    def parse(self, response):
        ## parse initial page
        pass
        
    def parse_page(self, response):
        ## parse jobs listings page
        pass

    def parse_job(self, response):
        ## parse each job page
        pass
