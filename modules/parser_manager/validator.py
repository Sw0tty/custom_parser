"""
Validate parser_config before save or use.
"""
import requests

from app_config.settings import PARSER_HEADERS
from modules.parser_manager.template import Template
from app_config.app_notices import SUCCESS, ERROR, WARNING


class Validator(Template):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.problems = []
    # @staticmethod
    # def validate_template(load_template, template) -> bool:
    #     if load_template() == template:
    #         return True
    #     return False

    @staticmethod
    def validate_url(url: str):
        try:
            response = requests.get(url, headers=PARSER_HEADERS)
        except ConnectionError:
            return False
        return response.status_code == 200
        
    @staticmethod
    def validate_secure_connection(connection) -> bool:
        return isinstance(connection, bool)

    @staticmethod
    def validate_name(name) -> bool:
        return isinstance(name, str)
    
    @staticmethod
    def validate_unique_site(site_name, sites):
        return True if site_name in sites else False
    
    def validate_config(self, config_file: dict):
        
        if self.count_main_keys != len(config_file.keys()):
            self.problems.append(f'{self.count_main_keys} != {len(config_file.keys())}', 'Count of main keys not equal.')
        for key in config_file.keys():
            if key not in self.template.keys():
                self.problems.append(tuple(key, 'Invalid key.'))

    def validate_config_data(self, config_file):
        if not self.validate_secure_connection(config_file['SECURE_CONNECTION']):
            self.problems.append(tuple(config_file['SECURE_CONNECTION'], 'Invalid type.'))


if __name__ == '__main__':
    validator = Validator()
    print(validator.validate_config({'df': 1}))

