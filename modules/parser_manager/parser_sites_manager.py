"""
!!! - NOT ACTUAL- !!!
-- Add new configs in the site_parser_settings file. --
!!! - NOT ACTUAL - !!!
"""
import os
import json

# from app_config.site_parser_settings import $some params$ .JSON
from app_config.site_parser_settings import SITE_PARSER_SETTINGS
from app_config.app_notices import ERROR, WARNING, SUCCESS


class ParserSitesManager:

    some_params = SITE_PARSER_SETTINGS

    @classmethod
    def __create_template(self):
        """
        Create template.json if not exist.
        """
        with open(r'app_config\site_parser_config\template.json', 'w', encoding='utf-8')  as template_file:
            template = {
                "SECURE_CONNECTION": "",
                "PARSING_PAGES":
                    {
                        "page_name":
                            {   
                                "PAGE_URL": "",
                                "MAIN_PARSE_INFO_BLOCK": "",
                                "INFO_BLOCKS":
                                    [   
                                        ["", "", ""]
                                    ],
                                "CUSTOM_FIELDS": []
                            }
                    },
                "PAGINATOR_CLASS_NAME": "",
                "EXPORT": {
                    "EXCEL": {
                        "EXCEL_COLUMNS_TITLE": [],
                        "ROW_COMMON_TITLES": []
                    },
                    "JSON": ""
                }
            }
            json.dump(template, template_file)

    @staticmethod
    def json_reader() -> dict:
        """
        """
        with open(r'app_config\site_parser_congif\parser_config.json', 'r', encoding='utf-8') as file:
            data = json.loads(file.read())
        return data
    
    @staticmethod
    def json_writer(data: dict) -> str:
        """
        Overwrite parser_config.json
        """
        with open(r'app_config\site_parser_congif\parser_config.json', 'w', encoding='utf-8')  as file:
            json.dump(data, file)
        return f'[{SUCCESS}] File update.'

    @staticmethod
    def file_exist(file: str) -> bool:
        return os.path.isfile(f'app_config\site_parser_congif\{file}.json')

    @staticmethod
    def load_template() -> dict:
        """
        Load and return template to site parser.
        """       
        with open(r'app_config\site_parser_congif\template.json', 'r', encoding='utf-8') as file:
            template = json.loads(file.read())
        return template
    
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
    

    def check_in_dict(self, some: str) -> bool:
        """
        Checking site in parsing sites dict.
        """
        return some in self.some_params.keys()
    
    def reader(self):
        """
        Read ?.JSON? file to get site parameters.
        """
    
    def add_site_template(self):
        """
        """
        # sites_dict = self.json_reader()

        if not self.file_exist('template'):
            self.__create_template()
            print(f'[{WARNING}] File not be found. Creating new file...')
        # template = self.load_template()

        # sites_dict[f"site_{len(sites_dict)}"] = template
        # return self.json_writer(sites_dict)


if __name__ == '__main__':
    site_adder = ParserSitesManager()
    # print(site_adder.check_secure('http://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=32312848009&morp'))
    # print(site_adder.check_in_dict("some"))
    # data = site_adder.json_reader()
    # print(data)
    # site_adder.json_writer(data)
    # d = { 'test': {'123': '22333'}}
    # d['test2'] = d.pop('test')
    # print(d)
    # site_adder.add_as_template()
    # tem = site_adder.load_template()
    site_adder.add_site_template()
    some = 1
    strt = "dfg{}dfgfvbcvvb{}dfbbb{}"
    print(strt.format(some, some, some))
