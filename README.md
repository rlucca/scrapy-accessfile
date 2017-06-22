Description
===========

Scrapy extension to do a access file log.

Configure scrapy project:
-------------------------

Set `ACCESSFILE_PATH` in your scrapy project `settings.py` to indicate where the access file will be saved as follows

```python
ACCESSFILE_PATH = 'access.log'
```

You can set up a filter in your scrapy project `settings.py` to not show some response status as follows

```python
ACCESSFILE_PATH = 'access.log'
ACCESSFILE_STATUS_FILTERS = [200]
```
