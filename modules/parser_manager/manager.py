"""
Changing parser_config.
"""
import json
import requests
from bs4 import BeautifulSoup as bs

from app_config.app_notices import SUCCESS, ERROR, WARNING, INFO
from app_config.settings import PARSER_HEADERS, DEFAULT_MODULE, DEFAULT_SITE_CONFIG
from modules.help import MODULES
from classes.styler import Styler
from modules.parser_manager.validator import Validator
from modules.parser_manager.connector import ConfigConnector
from modules.parser_manager.file_manager import FileManager
# from classes.modules_default import HelpMethod


class ConfigManager(FileManager, Validator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.styler = Styler()
        self.connected = False
        self.config = None
        self.site_config = None
        self.site_name = None
        self.current_module = None
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
    
    def get_current_module(self) -> str:
        if self.current_module:
            return self.current_module
        return DEFAULT_MODULE
    
    def get_config_name(self) -> str:
        if self.site_name:
            return self.site_name
        return DEFAULT_SITE_CONFIG
    
    @staticmethod
    def get_response_data(url):
        response = requests.get(url, headers=PARSER_HEADERS)
        return response
        return bs(response.text, 'html.parser')
    
    def get_page_title(self, response_data) -> str:
        # response = requests.get(url, headers=PARSER_HEADERS)
        response_data = bs(response_data.text, 'html.parser')
        return response_data.find('title').text.strip()
    
    @staticmethod
    def get_paginate_class(response_data: str):
        if "pagin" in response_data:
            middle_index = response_data.index("pagin")
            start_index = middle_index - (response_data[middle_index::-1].index(chr(34)) - 1)
            end_index = start_index + response_data[middle_index:].index(chr(34))
            return response_data[start_index:end_index]
        return None
    
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
            self.connect(self.load_config(), config_file[domain], domain)
            return f"[{SUCCESS}] Site added.", domain
        return f"[{WARNING}] Cancelled.", None

    def add_parsing_page(self) -> tuple:
        if not self.connected:
            return f"[{ERROR}] Not connected to config file!"
        
        url = input("Input site page url: ").strip()

        if url:
            if not self.validate_url(url):
                return f"[{ERROR}] Invalid url!", None
            
            domain = self.get_domain(url)
            if domain != self.site_name:
                return f"[{ERROR}] Site page url not from this site!", None

            response_data = self.get_response_data(url)
            page_title = self.get_page_title(response_data)
            paginate_class = self.get_paginate_class(response_data=response_data.text)

            if self.validate_unique_site(page_title, self.site_config['PARSING_PAGES'].keys()):
                answer = self.styler.console_input_styler("Site page already exist in site config! Add anyway? [y/n]: ")
                if answer != 'y':
                    response_data.clear()
                    return f"[{WARNING}] Cancelled.", None
                
                count = 0

                for key in self.site_config['PARSING_PAGES']:
                    if page_title in key:
                        count += 1

                page_title = f"{page_title}_{count}"
                # return f"[{ERROR}] Site page already exist in site config!", None

            self.site_config['PARSING_PAGES'][page_title] = self.page_template
            self.site_config['PARSING_PAGES'][page_title]['PAGE_URL'] = url
            self.site_config['PARSING_PAGES'][page_title]['PAGINATOR_CLASS_NAME'] = paginate_class
            self.config[domain] = self.site_config
            self.save_config(self.config)
            del response_data
            return f"[{SUCCESS}] Site page added.", page_title
        return f"[{WARNING}] Cancelled.", None
    
    def connect(self, config, site_config, site_name):
        if config:
            self.config = config
            if site_config:
                self.site_config = site_config
                self.site_name = site_name
                self.connected = True
            return f"[{SUCCESS}] Config set."
        return f"[{ERROR}] "

    def set_module(self):
        print("All modules:")
        for module in MODULES.keys():
            print(f'\t{self.styler.module_styler(module)} - {MODULES[module]}')
        selected_module = self.styler.console_input_styler("Print module: ").lower()
        if selected_module and selected_module in MODULES:
            
            config = self.load_config()
            if config:
                self.current_module = selected_module
                site_config = self.load_site_config(config)
                if site_config[0]:
                    self.connect(config, site_config=site_config[0], site_name=site_config[1])
                    return f"[{SUCCESS}] Module set."
                return f"[{WARNING}] Module set, but previews site config not found!"

            if selected_module == "manager":
                self.current_module = selected_module
                return f"[{SUCCESS}] Manager set."
            return f"[{ERROR}] Config not found! Set the 'manager'."
        return f"[{WARNING}] Cancelled."

    def reset(self):
        if self.current_module:
            self.connected = False
            self.config = None
            self.site_config = None
            self.site_name = None
            self.current_module = None
            return f"[{SUCCESS}] Parser reset."
        return f"[{INFO}] Parser already on default status."

    def set_config(self):
        config_dict = {str(key[0] + 1): key[1] for key in enumerate(self.config.keys())}

        for site in config_dict.keys():
            print(f"\t{site} - {config_dict[site]}")
        answer = input("Print a number of site name: ").strip()
        if answer and answer in config_dict.keys():
            self.overwrite_env(config_dict[answer])
            return self.connect(self.config, self.config[config_dict[answer]], config_dict[answer])
        return f"[{WARNING}] Cancelled."
    
    # def check_connection(self):
    #     if self.connected:
    #         return f"[{INFO}] Now loaded config for '{self.site_name}'."
    #     return f"[{ERROR}] No loaded any site config."

if __name__ == '__main__':
    manager = ConfigManager()
    url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html'
    response_data = manager.get_response_data(url)
    response_data = bs(response_data.text, 'html.parser')

    div = response_data.find('div')

    # print(div.find_next('div').text)

    divs = response_data.find_all('div', class_=True)
    classes = []

    for div in divs:
        classes.append(" ".join(div.attrs['class']))
    
    classes_set = list(set(classes))

    classes_dict = dict({class_: classes.count(class_) for class_ in classes_set})

    classes_dict = {k: v for k, v in sorted(classes_dict.items(), key=lambda item: item[1])}
    # print(classes_dict)
    # for i in classes_dict.items():
    #     print(i)
    

    for class_ in classes_dict:
        if classes_dict[class_] == 1:
            try:
                div = response_data.find('div', class_=class_)
                
                next_div = div.find_next('div')
                if classes_dict[" ".join(next_div.attrs['class'])] >= 10:
                    print(class_, "===", " ".join(next_div.attrs['class']))

            except KeyError:
                pass
            
        
        # print(div.attrs['class'])
        # if classes_dict[" ".join(parent_div.attrs['class'])] == 1:
        #     print(" ".join(parent_div.attrs['class']))
            # div = response_data.find('div', class_=class_)
            # try:
            #     next_div = " ".join(div.find_next('div').attrs['class'])
            #     if classes_dict[next_div] >= 10:
            #         print(class_, "===", next_div)
            # except KeyError:
            #     pass





    # for class_ in classes_dict:
    #     if classes_dict[class_] == 1:
    #         print(classes_dict[class_])
    #         div = response_data.find('div', class_=class_)
    #         try:
    #             next_div = " ".join(div.find_next('div').attrs['class'])
    #             if classes_dict[next_div] >= 10:
    #                 print(class_, "===", next_div)
    #         except KeyError:
    #             pass
        # if classes_dict[parent_div] == 1:
        #     print(classes_dict[parent_div])




    # print(manager.get_paginate_class(response_data))
    # print("pagin" in response_data.text)
    # paginator = manager.get_paginate_class(response_data.text)
    # print(paginator)
    # if "pagin" in response_data.text:
    #     middle_index = response_data.text.index("pagin")
    #     start_index = middle_index - (response_data.text[middle_index::-1].index(chr(34)) + 1)       
    #     end_index = start_index + response_data.text[middle_index:].index(chr(34))
    #     paginate_class = response_data.text[start_index:end_index]
    #     print(paginate_class)
    # for i in manager.get_paginate_class(response_data):
    #     print(i.text)


