"""
Check existing parser_config or template.
Creating if not exist for config_manager.
"""
import os
import json

from app_config.app_notices import ERROR, WARNING, SUCCESS
from template import Template

class ConfigChecker(Template):

    @staticmethod
    def file_exist(file: str) -> bool:
        return os.path.isfile(f'app_config\site_parser_config\{file}')

    def create_template(self) -> str:
        """
        Create template.json if not exist.
        """  
        with open(r'app_config\site_parser_config\template.json', 'w', encoding='utf-8')  as template_file:
            json.dump(self.template, template_file)
        return f'[{SUCCESS}] Template created!'
        
    def overwrite_template(self, is_valid):
        if not self.file_exist:
            return self.create_template()
    
    def create_parser_config(self) -> str:
        """
        Create parser_config.json if not exist.
        """
        with open(r'app_config\site_parser_config\parser_config.json', 'w', encoding='utf-8')  as config_file:
            json.dump(self.template, config_file)
        return f'[{SUCCESS}] Config file created!'


if __name__ == '__main__':
    checker = ConfigChecker()

    print(checker.template)
    print(checker.file_exist('template.json'))
