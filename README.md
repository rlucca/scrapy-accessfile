Description
===========

Scrapy extension to do a access file log.

Configure scrapy project:
-------------------------

Set `ACCESSFILE_PATH` in your scrapy project `settings.py` to indicate where the access file will be saved as follows

```python
ACCESSFILE_PATH = 'access.log'
```

Add the new extension to `DOWNLOADER_MIDDLEWARES` in your scrapy project `settings.py` as follows

```python
DOWNLOADER_MIDDLEWARES = {
    'project.scrapy-accessfile.AccessFileStats': 545,
}
```

You can set up a filter in your scrapy project `settings.py` to not show some response status as follows

```python
ACCESSFILE_PATH = 'access.log'
ACCESSFILE_STATUS_FILTERS = [200]
```

Follows all configuration needed to best copy-and-paste

```python
ACCESSFILE_PATH = 'access.log'
#ACCESSFILE_STATUS_FILTERS = [200]
DOWNLOADER_MIDDLEWARES = {
    'project.scrapy-accessfile.AccessFileStats': 545, # TODO change project to your project name
}
```

License
-------

License free to use.
