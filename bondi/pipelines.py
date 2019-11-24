# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import re


#class BondiPipeline(object):
    #def process_item(self, item, spider):
        #return item


#class DropIfEmptyFieldPipeline(object):

    # case-insensitive search for string "nurse"
 #   REGEX_NURSE = re.compile(r'.aaData.', re.IGNORECASE)

  #  def process_item(self, item, spider):
        # user .search() and not .match() to test for substring match
   #     if not(self.REGEX_NURSE.search(item["desc"])):
    #        raise DropItem()
     #   else:
      #      return item
