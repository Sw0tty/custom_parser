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
    
    def get_site_name(self) -> str:
        """
        Return current site_name config.
        """
        return self.site_name
    
    def get_current_module(self) -> str:
        if self.current_module:
            return self.current_module
        return DEFAULT_MODULE
    
    def get_config_name(self) -> str:
        if self.site_name:
            return self.site_name
        return DEFAULT_SITE_CONFIG
    
    @staticmethod
    def __get_response_data(url):
        return requests.get(url, headers=PARSER_HEADERS)
        return bs(response.text, 'html.parser')
    
    @staticmethod
    def __get_page_title(response_data) -> str:
        return response_data.find('title').text.strip()
    
    @staticmethod
    def __get_paginate_class(response_data: str):
        if "pagin" in response_data:
            middle_index = response_data.index("pagin")
            start_index = middle_index - (response_data[middle_index::-1].index(chr(34)) - 1)
            end_index = start_index + response_data[start_index:].index(chr(34))
            return response_data[start_index:end_index]
        return None
    
    def find_info_block_class(self, response_data, classes_dict, previews_classes, blocks_on_page):
        if len(previews_classes) > 1:
            supposed_main_block_classes = []
            for class_ in previews_classes:
                try:
                    blocks_class = response_data.find('div', class_=class_)
                    main_class = blocks_class.find_next('div')
                    if classes_dict[" ".join(main_class.attrs['class'])] == blocks_on_page:
                        supposed_main_block_classes.append(" ".join(main_class.attrs['class']))
                except KeyError:
                    continue
            return self.find_info_block_class(response_data, classes_dict, supposed_main_block_classes, blocks_on_page)
        return previews_classes[0]
    
    def add_parsing_site(self, config_file) -> str:
        url = input("Input site url: ").strip()
        if url:
            
            domain = self.get_domain(url)

            if self.validate_unique_site(domain, config_file.keys()):
                return f"[{ERROR}] Site already exist in config!"
            if not self.validate_url(url):
                return f"[{ERROR}] Invalid url!"
            
            self.overwrite_env(domain)
            config_file[domain] = self.template
            config_file[domain]['SECURE_CONNECTION'] = self.check_secure(url)
            config_file[domain]['SITE_URL'] = self.get_main_url(url)
            self.save_config(config_file)
            self.connect(self.load_config(), config_file[domain], domain)
            return f"[{SUCCESS}] Site '{domain}' added."
        return f"[{WARNING}] Cancelled."

    def add_parsing_page(self) -> str:
        if not self.connected:
            return f"[{ERROR}] Not connected to config file!"
        
        url = input("Input site page url: ").strip()

        if not url:
            return f"[{WARNING}] Cancelled."
        
        if not self.validate_url(url):
            return f"[{ERROR}] Invalid url!"
        
        domain = self.get_domain(url)

        if domain != self.site_name:
            return f"[{ERROR}] Site page url not from this site!"

        response_data = self.__get_response_data(url)
        page_title = self.__get_page_title(bs(response_data.text, 'html.parser'))
        paginate_class = self.__get_paginate_class(response_data=response_data.text)

        # ------------ Class Block ------------------
        response_data = bs(response_data.text, 'html.parser')
        
        # divs = response_data.find_all('div', class_=True)
        # classes = []
        # for div in divs:
        #     classes.append(" ".join(div.attrs['class']))

        classes = set(" ".join(div.attrs['class']) for div in response_data.find_all('div', class_=True))
        
        # classes_set = list(set(classes))
        classes_dict = dict({class_: classes.count(class_) for class_ in classes})

        supposed_holder_blocks_classes_list = [class_ for class_ in classes_dict if classes_dict[class_] == 1]

        # for class_ in classes_dict:
        #     if classes_dict[class_] == 1:
        #         supposed_holder_blocks_classes_list.append(class_)

        info_block_class = self.find_info_block_class(response_data, classes_dict, supposed_holder_blocks_classes_list, 10)
        # ------------------------------


        if self.validate_unique_site(page_title, self.site_config['PARSING_PAGES'].keys()):
            answer = self.styler.console_input_styler("Site page already exist in site config! Add anyway? [y/n]: ")
            if answer != 'y':
                return f"[{WARNING}] Cancelled."
            
            count = 0
            for key in self.site_config['PARSING_PAGES']:
                if page_title in key:
                    count += 1

            page_title = f"{page_title}_{count}"
            
        self.site_config['PARSING_PAGES'][page_title] = self.page_template
        self.site_config['PARSING_PAGES'][page_title]['PAGE_URL'] = url
        self.site_config['PARSING_PAGES'][page_title]['PAGINATOR_CLASS_NAME'] = paginate_class
        self.site_config['PARSING_PAGES'][page_title]['MAIN_PARSE_INFO_BLOCK'] = info_block_class
        self.config[domain] = self.site_config
        self.save_config(self.config)

        return f"[{SUCCESS}] Site page '{page_title}' added."
        
    def delete_parsing_site(self) -> str:
        config_dict = {str(key[0] + 1): key[1] for key in enumerate(self.config.keys())}

        for site in config_dict.keys():
            print(f"\t{site} - {config_dict[site]}")
        answer = input("Print a number of site name to delete config: ").strip()
        if answer and answer in config_dict.keys():
            confirmation = input(f"Are you sure to want delete '{config_dict[answer]}' config?[Y/(any button)]: ").strip()
            if confirmation and confirmation == 'Y':
                del self.config[config_dict[answer]]
                self.save_config(self.config)
                if config_dict[answer] == self.site_name:
                    self.config = self.load_config()
                    self.site_config = None
                    self.site_name = None
                return f"[{SUCCESS}] Site config for '{config_dict[answer]}' has been deleted."
        return f"[{WARNING}] Cancelled."

    def connect(self, config, site_config, site_name) -> str:
        if config:
            self.config = config
            if site_config:
                self.site_config = site_config
                self.site_name = site_name
                self.connected = True
            return f"[{SUCCESS}] Config set."
        return f"[{ERROR}] Config file not found!"

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
                self.config = config
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


if __name__ == '__main__':
    manager = ConfigManager()
    url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html'
    response_data = manager.get_response_data(url)
    response_data = bs(response_data.text, 'html.parser')

    # div = response_data.find('div')

    divs = response_data.find_all('div', class_=True)
    classes = []

    for div in divs:
        classes.append(" ".join(div.attrs['class']))
    
    classes_set = list(set(classes))
    classes_dict = dict({class_: classes.count(class_) for class_ in classes_set})

    # classes_dict = {k: v for k, v in sorted(classes_dict.items(), key=lambda item: item[1])}
    # print(classes_dict)
    # for i in classes_dict.items():
    #     print(i)
    
    # def find_next_class(classes_dict, supposed_main_block_classes):
    #     for class_ in supposed_main_block_classes:
    #         blocks_class = response_data.find('div', class_=class_)
    #         main_class = blocks_class.find_next('div')
    #         if classes_dict[" ".join(next_div_in_block.attrs['class'])] > classes_dict[class_]:
    #             input_block = next_div_in_block.find_next('div')
    #             if classes_dict[" ".join(main_class.attrs['class'])] == classes_dict[" ".join(main_class.attrs['class'])]:
    #                 print("Main: ", class_, "===", "Docher:", " ".join(next_div_in_block.attrs['class']))
    
    supposed_holder_blocks_classes_list = []

    for class_ in classes_dict:
        if classes_dict[class_] == 1:
            supposed_holder_blocks_classes_list.append(class_)

            # try:
            #     supposed_main_class = response_data.find('div', class_=class_)
                
            #     next_div_in_block = supposed_main_class.find_next('div')

            #     if classes_dict[" ".join(next_div_in_block.attrs['class'])] > classes_dict[class_]:
            #         input_block = next_div_in_block.find_next('div')
            #         if classes_dict[" ".join(input_block.attrs['class'])] == classes_dict[" ".join(next_div_in_block.attrs['class'])]:
            #             input_input_block = input_block.find_next('div')
            #             if classes_dict[" ".join(input_input_block.attrs['class'])] == classes_dict[" ".join(input_block.attrs['class'])]:
            #                 print("Main: ", class_, "===", "Docher:", " ".join(next_div_in_block.attrs['class']))

            # except KeyError:
            #     pass

    # supposed_main_block_classes = []

    # if len(supposed_holder_blocks_classes_list) > 1:
    #     for class_ in supposed_holder_blocks_classes_list:
    #         try:
    #             blocks_class = response_data.find('div', class_=class_)
    #             main_class = blocks_class.find_next('div')
    #             if classes_dict[" ".join(main_class.attrs['class'])] > classes_dict[class_]:
    #                 supposed_main_block_classes.append(main_class) 
    #         except KeyError:
    #             pass
            
    # divs = response_data.find_all('div', class_=True)
    # classes = []

    # for div in divs:
    #     classes.append(" ".join(div.attrs['class']))
    
    # classes_set = list(set(classes))
    # classes_dict = dict({class_: classes.count(class_) for class_ in classes_set})

    # supposed_holder_blocks_classes_list = []

    # for class_ in classes_dict:
    #     if classes_dict[class_] == 1:
    #         supposed_holder_blocks_classes_list.append(class_)

    def find_info_block_class(classes_dict, previews_classes, blocks_on_page):
        if len(previews_classes) > 1:
            supposed_main_block_classes = []
            for class_ in previews_classes:
                try:
                    blocks_class = response_data.find('div', class_=class_)
                    main_class = blocks_class.find_next('div')
                    if classes_dict[" ".join(main_class.attrs['class'])] == blocks_on_page:
                        supposed_main_block_classes.append(" ".join(main_class.attrs['class']))
                except KeyError:
                    continue
            return find_info_block_class(classes_dict, supposed_main_block_classes, blocks_on_page)
        return previews_classes[0]
    
    print(find_info_block_class(classes_dict, supposed_holder_blocks_classes_list, 10))
    # return supposed_classes_list[0]
            
        
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


