"""
Check existing parser_config or template.
Creating if not exist for config_manager.
"""
import os
import json
from dotenv import load_dotenv
from pathlib import Path

from app_config.app_notices import ERROR, WARNING, SUCCESS
from modules.parser_manager.template import Template


load_dotenv(Path('app_config\site_parser_config\.env'))

class FileManager(Template):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_site_name = os.getenv('SITE_NAME')
    
    @staticmethod
    def file_exist() -> bool:
        return os.path.isfile(f'app_config\site_parser_config\parser_config.json')
    
    @staticmethod
    def overwrite_env(site_name: str) -> None:
        with open(r'app_config\site_parser_config\.env', 'w', encoding='utf-8') as env_file:
            env_file.write(f"""SITE_NAME='{site_name}'""")

    def load_config(self, add_site=False):
        if self.file_exist():
            with open(r'app_config\site_parser_config\parser_config.json', 'r', encoding='utf-8') as config_file:
                config = json.load(config_file)
                if add_site:
                    return config
                return config[self.default_site_name]
        return f'[{ERROR}] File not exist!'

    def save_config(self, config_data):
        with open(r'app_config\site_parser_config\parser_config.json', 'w', encoding='utf-8') as config_file:
            return json.dump(config_data, config_file)
        
    def create_config(self) -> str:
        if self.file_exist:
            return f'[{ERROR}] File exist!'
        with open(r'app_config\site_parser_config\parser_config.json', 'w', encoding='utf-8') as template_file:
            json.dump(self.template, template_file)
        return f'[{SUCCESS}] Config created!'
        
    # def overwrite_template(self, is_valid):
    #     if not self.file_exist:
    #         return self.create_template()
    
    def create_parser_config(self) -> str:
        with open(r'app_config\site_parser_config\parser_config.json', 'w', encoding='utf-8')  as config_file:
            json.dump(self.template, config_file)
        return f'[{SUCCESS}] Config file created!'


if __name__ == '__main__':
    checker = FileManager()
    
    # print(checker.name)
    name = "dfg"
    checker.overwrite_env(name)
    # print(checker.template)
    # print(checker.file_exist('template.json'))
