# PLUMIFY

An app for visualizing plumes on a map. Just enter the co-ordinates, upload a plume and presto!

![](docs/images/show.png)

## Getting Started

If you want to use this app, you can easily get it running with Docker, just run

```
TODO
```

## Development

To develop this app you need to first install [pipenv](https://pipenv.kennethreitz.org/en/latest/)

Next you can install all the python packages and setup a virtual env automatically with:

```python
pipenv install --dev
```

Next you will need to set up the database. You can do that with:

```
scripts/migrate
```

Then you can start the development server with

```
scripts/server
```

(just an alias for `python manage.pry runserver`)


### Testing

You can run the tests with

```shell
script/tests
```

which is just an alias for `python manage.py test`