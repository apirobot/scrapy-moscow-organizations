import scrapy
from scrapy_splash import SplashRequest

from organizations.items import OrganizationItem


class OrganizationsSpider(scrapy.Spider):
    name = 'organizations'
    delay = 2  # seconds

    def _get_request(self, url, callback, **kwargs):
        return SplashRequest(
            url=url,
            callback=callback,
            args={
                'wait': self.delay
            })

    def start_requests(self):
        yield self._get_request(
            url='http://rubrikator.org/russia/moscow',
            callback=self.parse)

    def parse(self, response):
        for organization in response.css('.category-row'):
            # follow to the organization detail page
            yield self._get_request(
                url=organization.css('.four-fifths a::attr("href")').extract_first(),
                callback=self.parse_organization)

        next_page = response.xpath('//a[text()="Следующая"]//@href').extract_first()
        if next_page is not None:
            # follow to the next page
            yield self._get_request(
                url=response.urljoin(next_page),
                callback=self.parse)

    def parse_organization(self, response):
        yield OrganizationItem({
            'name': response.css('h1::text').extract_first(),
            'phone': response.css('#phone-0::text').extract_first(),
            'address': response.css('#address-0::text').extract_first(),
            'rating': response.css('#org-ratings meta::attr("content")').extract_first()
        })
