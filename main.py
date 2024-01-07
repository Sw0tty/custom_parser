"""
Main File MasterExcel
"""

from app_config.settings import NAME, MASTER_CMD_INPUT, PARSER_DIVS_DICT, DEFAULT_SITE_CONFIG
from app_config.app_notices import RESET_MODULE, INFO, HELP, ERROR, WARNING, SUCCESS
from modules.help import HelpModule, MODULES
from classes.modules_default import MainMethods
from modules.parser.file_parser import FileParser
from modules.parser.site_parser import SiteParser
from modules.rebuilder import Rebuilder
from classes.styler import Styler
from modules.parser_manager.manager import ConfigManager
from modules.parser_manager.file_manager import FileManager
from modules.parser_manager.validator import Validator

import datetime
import os
from tkinter.messagebox import showwarning


help_module = HelpModule()
master_excel = MainMethods()
file_parser = FileParser()
site_parser = SiteParser()
rebuilder = Rebuilder()
styler = Styler()
config_manager = ConfigManager()
# file_manager = FileManager()
validator = Validator()
# config = config_manager.load_config(True)
# print(config.keys())
# print(config_manager.template)

if datetime.datetime.today().weekday() + 1 == 5:   
    WEEK_AGO = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%d.%m.%Y")
    TODAY_DATE = datetime.date.today().strftime('%d.%m.%Y')
    if os.path.exists(fr"C:\Users\Егор\Desktop\Еженедельный отчет Егоров от {WEEK_AGO}.doc"):
        os.rename(fr"C:\Users\Егор\Desktop\Еженедельный отчет Егоров от {WEEK_AGO}.doc", fr"C:\Users\Егор\Desktop\Еженедельный отчет Егоров от {TODAY_DATE}.doc")
        showwarning(title="Пятница файл", message="Еженедельный файл")


print(f"""[{INFO}] Print {HELP} for call list commands.""")


while True:

    input_command = styler.console_input_styler(
        styler.cmd_builder(
            NAME,
            config_manager.get_current_module(),
            config_manager.get_config_name(),
            MASTER_CMD_INPUT
        )
    )

    match input_command:
        case 'help':
            help_module.help(config_manager.get_current_module())
        case 'set':
            print(config_manager.set_module())
            continue
        case 'reset':
            print(config_manager.reset())
            continue
        case 'exit':
            break

    if config_manager.get_current_module() == 'file-parser':
        match input_command:
            case '1':
                print(file_parser.get_file_path())
            case '2':
                print(file_parser.set_file_path())
            case '3':
                print(file_parser.get_file_name())
            case '4':
                print(file_parser.parse_file(PARSER_DIVS_DICT))
            case '5':
                print(file_parser.excel_export())

    elif config_manager.get_current_module() == 'site-parser':
        match input_command:
            case '1':
                print(site_parser.to_empty_list())
            case '2':
                print(site_parser.add_info())
            case '3':
                print(site_parser.excel_export())
            case '4':
                print(site_parser.get_url())

    elif config_manager.get_current_module() == 'rebuilder':
        match input_command:
            case '1':
                print(rebuilder.set_selected_file())
            case '2':
                rebuilder.get_params_status()
            case '3':
                print(rebuilder.get_file_name())
            case '4':
                print(rebuilder.get_rebuild_status())
            case '5':
                print(rebuilder.prepare_rebuild())
            case '6':
                print(rebuilder.excel_export())

    elif config_manager.get_current_module() == 'manager':
        match input_command:
            case '1':  # create config
                print(config_manager.create_config())
            case '2':  # add site
                config = config_manager.load_config()
                status = config_manager.add_parsing_site(config)
                # if config_data:
                #     config_manager.load_config()
                #     SITE_CONFIG = config_data
                print(status)
            case '3':  # add site page
                status = config_manager.add_parsing_page()
                print(status)
                # print(config_data)
            case '4':  # reset config
                # print(config_manager.check_connection())
                print(config_manager.set_config())
                SITE_CONFIG = config_manager.get_site_name()
            case '5':
                print(config_manager.delete_parsing_site())
                # print(config_manager.get_page_title('https://docs-python.ru/'))
                
                
                # if validator.validate_unique_site()
                # file_manager.save_config(config)
