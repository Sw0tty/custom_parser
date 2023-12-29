"""
Working with .env, parser_manager files.
Allowed methods:
    - check exist;
    - create;
    - load;
    - save;
    - overwrite
"""
import os
import json
from dotenv import load_dotenv

from app_config.app_notices import ERROR, WARNING, SUCCESS
from modules.parser_manager.template import Template


load_dotenv('app_config\site_parser_config\.env')


class FileManager(Template):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_site_name = os.getenv('DEFAULT_SITE_NAME')
    
    @staticmethod
    def file_exist() -> bool:
        return os.path.isfile(f'app_config\site_parser_config\parser_config.json')
    
    @staticmethod
    def overwrite_env(site_name: str) -> None:
        with open(r'app_config\site_parser_config\.env', 'w', encoding='utf-8') as env_file:
            env_file.write(f"""DEFAULT_SITE_NAME='{site_name}'""")

    @staticmethod
    def save_config(config_data: dict) -> None:
        with open(r'app_config\site_parser_config\parser_config.json', 'w', encoding='utf-8') as config_file:
            json.dump(config_data, config_file)
    
    def create_config(self) -> str:
        if self.file_exist():
            return f'[{ERROR}] File already exist!'
        with open(r'app_config\site_parser_config\parser_config.json', 'w', encoding='utf-8') as config_file:
            json.dump({}, config_file)
        return f'[{SUCCESS}] Config file created.'
    
    def load_config(self, config_file=False, site_config=False):
        if self.file_exist():
            with open(r'app_config\site_parser_config\parser_config.json', 'r', encoding='utf-8') as config_file:
                config = json.load(config_file)
                return config
                if config_file:
                    return config
                if site_config:
                    site_config = config.get(self.default_site_name, None)
                    if site_config:
                        return site_config, self.default_site_name
                    return config, None
                # if site_config:
                #     return site_config, self.default_site_name
                # if new_site:
                #     return config
                # site_config = config.get(self.default_site_name, None)
                # if site_config:
                #     return site_config, self.default_site_name
                # return config
        return None
    
    def load_site_config(self, config) -> tuple:
        return config.get(self.default_site_name, None), self.default_site_name

    # def overwrite_template(self, is_valid):
    #     if not self.file_exist:
    #         return self.create_template()
    
    # def create_parser_config(self) -> str:
    #     with open(r'app_config\site_parser_config\parser_config.json', 'w', encoding='utf-8')  as config_file:
    #         json.dump(self.template, config_file)
    #     return f'[{SUCCESS}] Config file created!'


# if __name__ == '__main__':
#     checker = FileManager()
    
#     # print(checker.name)
#     name = "dfg"
#     checker.overwrite_env(name)
#     # print(checker.template)
#     # print(checker.file_exist('template.json'))
