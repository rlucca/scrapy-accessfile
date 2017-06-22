from scrapy.exceptions import NotConfigured
from time import time


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
