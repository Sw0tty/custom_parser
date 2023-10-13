"""
!!! - IN PROGRESS - !!!
Add new configs in the site_parser_settings file.
!!! - IN PROGRESS - !!!
"""


class ParserSitesManager:
    
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
        if 's' in url[:url.find(':')]:
            return True
        return False


if __name__ == '__main__':
    site_adder = ParserSitesManager()
    print(site_adder.check_secure('http://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=32312848009&morp'))


