# -*- coding: utf-8 -*-


import scrapy
import datetime
from loginform import fill_login_form
from scrapy.http import FormRequest
from scrapy.selector import HtmlXPathSelector
from bondi.items import BondiItem
from scrapy.spiders import Spider


class RedbusSpider(Spider):
    name = 'redbus'
    login_user = "user"
    login_pass = "somepass"
    allowed_domains = ["some_domain"]
    start_urls = ["http://some_url/login"]

    def parse(self, response):
        args, url, method = fill_login_form(response.url, response.body, self.login_user, self.login_pass)
        return FormRequest(url, method=method, formdata=args, callback=self.after_login)


    def after_login(self, response):
        # you are logged in here, in this case use dia_hoy and dia_ayer to delimitate the period
        dia_hoy = datetime.date.fromordinal(datetime.date.today().toordinal()-1).strftime("%d/%m/%Y").replace("/","%2F")
        dia_ayer = datetime.date.fromordinal(datetime.date.today().toordinal()-8).strftime("%d/%m/%Y").replace("/","%2F")
        yield FormRequest(url="http://some_url/lista?op_from=1&op_to=8&dni_chofer=&fecha_desde="+dia_ayer+
                              "&fecha_hasta="+dia_hoy+,callback=self.after_consulta)

    def after_consulta(self, response):

        hxs = HtmlXPathSelector(response)
        sites = hxs.select('/html/body//text()').extract()
        items = []
        for site in sites:
            item = BondiItem()
            string = site
	    item['desc'] = string
            items.append(item)
        return items
