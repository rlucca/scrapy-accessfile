#!/usr/bin/python
# -*-coding:utf-8-*-
""" Scrapy Middleware to write in a file all results of every Request.

Downloader Middleware which writes to a file the result of each request.
A result may not be written if it is filtered.
"""
from scrapy.exceptions import NotConfigured
from time import time

__author__ = 'Ricardo Rodrigues Lucca'
__credits__ = ['Ricardo Rodrigues Lucca']
__license__ = 'free'
__version__ = '0.1'
__maintainer__ = 'Ricardo Rodrigues Lucca'
__email__ = 'rlucca@gmail.com'
__status__ = 'Development'
__original_source__ = 'https://raw.githubusercontent.com/rlucca/scrapy-accessfile/master/scrapy-accessfile.py'


class AccessFileStats(object):

    def __init__(self, stats, filters, filename):
        self.stats = stats
        self.filtered_status = filters
        self.filename = filename
        self.line = '%d,{},{}\n' % int(time())

    @classmethod
    def from_crawler(cls, crawler):
        path = crawler.settings.get('ACCESSFILE_PATH')
        if not path:
            raise NotConfigured
        key = 'ACCESSFILE_STATUS_FILTERS'
        filters = crawler.settings.getlist(key, [])
        return cls(crawler.stats, filters, path)

    def process_response(self, request, response, spider):
        if response.status not in self.filtered_status:
            with open(self.filename, 'a') as fd:
                fd.write(self.line.format(response.status, request.url))
        return response

    def process_exception(self, request, exception, spider):
        with open(self.filename, 'a') as fd:
            fd.write(self.line.format('999', request.url))
