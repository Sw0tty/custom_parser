"""
Changing parser_config.
"""
import json

from app_config.app_notices import SUCCESS, ERROR, WARNING, INFO
from modules.parser_manager.validator import Validator
from modules.parser_manager.connector import ConfigConnector
from modules.parser_manager.file_manager import FileManager
# from classes.modules_default import HelpMethod


class ConfigManager(FileManager, Validator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connected = None
        self.config = None
        self.site_config = None
        self.site_name = None
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

            if self.validate_unique_site(domain, config_file.keys()):
                return f"[{ERROR}] Site already exist in config!", None
            if not self.validate_url(url):
                return f"[{ERROR}] Invalid url!", None
            
            self.overwrite_env(domain)
            config_file[domain] = self.template
            config_file[domain]['SECURE_CONNECTION'] = self.check_secure(url)
            config_file[domain]['SITE_URL'] = self.get_main_url(url)
            self.save_config(config_file)
            return f"[{SUCCESS}] Site added.", domain
        return f"[{WARNING}] Cancelled.", None

    def connect_to_config(self):
        pass

    def add_parsing_page(self, site_config) -> tuple:
        url = input("Input site page url: ").strip()
        if url:
            domain = self.get_domain(url)

            if self.validate_unique_site(domain, site_config['PARSING_PAGES'].keys()):
                return f"[{ERROR}] Site page already exist in site config!", None
            if not self.validate_url(url):
                return f"[{ERROR}] Invalid url!", None
            site_config['PARSING_PAGES']["???"] = self.page_template
            self.save_config(site_config)
            return f"[{SUCCESS}] Site page added.", domain
        return f"[{WARNING}] Cancelled.", None
    
    def connect(self, config, site_config, site_name):
        if config:
            self.config = config
            if site_config:
                self.site_config = site_config
                self.site_name = site_name
                self.connected = True
            return f"[{SUCCESS}] Config reset."
        return f"[{ERROR}] "

    def reset(self):
        config_dict = {str(key[0] + 1): key[1] for key in enumerate(self.config.keys())}
        print(config_dict)
        for site in config_dict.keys():
            print(f"\t{site} - {config_dict[site]}")
        answer = input("Print a number of site name: ").strip()
        if answer and answer in config_dict.keys():
            self.overwrite_env(config_dict[answer])
            return self.connect(self.config, self.config[config_dict[answer]], config_dict[answer])
        return f"[{WARNING}] Cancelled."
    
    def check_connection(self):
        if self.connected:
            return f"[{INFO}] Now connected to '{self.site_name}'."
        return f"[{ERROR}] No connected to any site config."
    
    # def load_template(self):
    #     with open(r'path', 'r', 'utf-8') as config:
    #         config_file = json.loads(config)
    #     return config_file
    
    def get_site_config(self):
        pass
    
    # def save_config(self, file):
    #     with open(r'path', 'w', 'utf-8') as config:
    #         json.dumps(file , config)
    #     return f'[{SUCCESS}] File saved.'

    
