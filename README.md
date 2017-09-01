## Description

Get data about Moscow organizations from http://rubrikator.org/russia/moscow by scraping pages.

## How to run

Pull the splash docker image:

```bash
$ sudo docker pull scrapinghub/splash
```

Start the container:

```bash
docker run -p 8050:8050 scrapinghub/splash
```

Install dependencies after configuring your virtualenv:

```bash
$ pip install -r requirements.txt
```

Start crawling:

```bash
$ scrapy crawl organizations
```

By default, all data will be saved inside `output` folder. One file for each organization.
