"""
!!! - IN PROGRESS - !!!
Add new configs in the site_parser_settings file.
!!! - IN PROGRESS - !!!
"""
# from app_config.site_parser_settings import $some params$ .JSON
from app_config.site_parser_settings import SITE_PARSER_SETTINGS


class ParserSitesManager:

    some_params = SITE_PARSER_SETTINGS

    def check_in_dict(self, some: str) -> bool:
        """
        Checking site in parsing sites dict.
        """
        return some in self.some_params.keys()

    @staticmethod
    def get_domain(url: str) -> str:
        """
        Return the site domain.
        """
        return url[url.find('/') + 2:url.find('/', 8)]
    
    @staticmethod
    def check_secure(url: str) -> bool:
        """
        Return secure site status.
        """
        return 's' in url[:url.find(':')]

    def reader(self):
        """
        Read ?.JSON? file to get site parameters.
        """


if __name__ == '__main__':
    site_adder = ParserSitesManager()
    # print(site_adder.check_secure('http://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=32312848009&morp'))
    print(site_adder.check_in_dict("some"))
