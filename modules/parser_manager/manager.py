"""
Changing parser_config.
"""
import json

from app_config.app_notices import SUCCESS, ERROR, WARNING
from modules.parser_manager.validator import Validator
from modules.parser_manager.template import Template
from modules.parser_manager.file_manager import FileManager
# from classes.modules_default import HelpMethod


class ConfigManager(FileManager, Validator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connection = None
        # self.config = self.load_config()
    
    @staticmethod
    def get_domain(url: str) -> str:
        """
        Return the site domain.
        """
        return url[url.find('/') + 2:url.find('/', 8)]
    
    @staticmethod
    def get_main_url(url: str) -> str:
        """
        Return the site main page url.
        """
        return url[:url.find('/', 8)]
    
    @staticmethod
    def check_secure(url: str) -> bool:
        """
        Return secure site status.
        """
        return 's' in url[:url.find(':')]
    
    def add_parsing_site(self, config_file):
        url = input("Input site url: ").strip()
        if url:
            
            domain = self.get_domain(url)
            
            if not self.validate_url(url):
                return f'[{ERROR}] Invalid url!'
            if self.validate_unique_site(domain, config_file.keys()):
                return f'[{ERROR}] Site already exist in config!'
            config_file[domain] = self.template
            config_file[domain]['SECURE_CONNECTION'] = self.check_secure(url)
            config_file[domain]['SITE_URL'] = self.get_main_url(url)
            self.save_config(config_file)
            return f'[{SUCCESS}] Site added.'
        return f'[{WARNING}] Cancelled.'

    def connect_to_config(self):
        pass

    def add_parsing_page(self):
        pass

    def load_template(self):
        with open(r'path', 'r', 'utf-8') as config:
            config_file = json.loads(config)
        return config_file
    
    def set_name(self):
        pass
    
    # def save_config(self, file):
    #     with open(r'path', 'w', 'utf-8') as config:
    #         json.dumps(file , config)
    #     return f'[{SUCCESS}] File saved.'

    
