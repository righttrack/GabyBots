__author__ = 'jeffmay'

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from django.db.utils import IntegrityError
from scrapy import log
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime

class DjangoWriterPipeline(object):
    def process_item(self, item, spider):
        try:
            # This name must match Article's source
            item['source'] = spider.ref_object

            checker_rt = SchedulerRuntime(runtime_type='C')
            checker_rt.save()
            item['checker_runtime'] = checker_rt

            item.save()
            spider.action_successful = True
            spider.log("Item saved.", log.INFO)

        except IntegrityError, e:
            spider.log(str(e), log.ERROR)
            raise DropItem("Missing attribute.")

        return item

