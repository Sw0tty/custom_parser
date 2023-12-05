"""
Main File MasterExcel
"""

from app_config.settings import NAME, MASTER_CMD_INPUT, PARSER_DIVS_DICT, CURRENT_MODULE, SITE_CONFIG
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


def reset_module():
    global CURRENT_MODULE
    global SITE_CONFIG
    print("All modules:")
    for module in MODULES.keys():
        print(f'\t{styler.module_styler(module)} - {MODULES[module]}')
    new_module = styler.console_user_input_styler("Print module: ").lower()
    if new_module and new_module in MODULES:
        # if new_module == 'manager':
        #     CURRENT_MODULE = new_module
        #     return RESET_MODULE
        
        config = config_manager.load_config()
        if config:
            CURRENT_MODULE = new_module
            site_config = config_manager.load_site_config(config)
            if site_config[0]:
                config_manager.connect(config, site_config=site_config[0], site_name=site_config[1])
                SITE_CONFIG = config_manager.site_name
                return f"[{SUCCESS}] Module reset."
            return f"[{WARNING}] Module reset, but previews site config not found!"
        
        # if isinstance(config_status, tuple):
        #     CURRENT_MODULE = new_module
        #     SITE_CONFIG = config_status[1]
        #     return f"[{SUCCESS}] Module reset."
            
        # if isinstance(config_status, dict):
        #     CURRENT_MODULE = new_module
        #     return f"[{WARNING}] Module reset, but previews site config not found!"
        return f"[{ERROR}] Config not found! Set the 'manager'."
    return f"[{WARNING}] Cancelled."


def cmd_builder(program_name, module, site_config, cmd_input):
    if module == 'None-module':
        return f"{program_name}({styler.module_styler(module)}){cmd_input} "
    return f"{program_name}({styler.module_styler(module)})\({styler.module_styler(site_config)}){cmd_input} "


while True:

    # input_command = input(f"{NAME}({styler.module_styler(CURRENT_MODULE)}){MASTER_CMD_INPUT} ")
    # input_command = styler.console_user_input_styler(f"{NAME}({styler.module_styler(CURRENT_MODULE)}){styler.module_styler(module)}{MASTER_CMD_INPUT} ")
    input_command = styler.console_user_input_styler(cmd_builder(NAME, CURRENT_MODULE, SITE_CONFIG, MASTER_CMD_INPUT))

    match input_command:
        case 'help':
            help_module.help(CURRENT_MODULE)
        case 'set':
            print(reset_module())
            continue
        case 'reset':
            if CURRENT_MODULE != 'None-module':
                CURRENT_MODULE = 'None-module'
                SITE_CONFIG = 'Config-not-selected'
                print(RESET_MODULE)
            continue
        case 'exit':
            break

    if CURRENT_MODULE == 'file-parser':
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

    elif CURRENT_MODULE == 'site-parser':
        match input_command:
            case '1':
                print(site_parser.to_empty_list())
            case '2':
                print(site_parser.add_info())
            case '3':
                print(site_parser.excel_export())
            case '4':
                print(site_parser.get_url())

    elif CURRENT_MODULE == 'rebuilder':
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
    elif CURRENT_MODULE == 'manager':
        match input_command:
            case '1':  # create config
                print(config_manager.create_config())
            case '2':  # add site
                config = config_manager.load_config()
                status, config_data = config_manager.add_parsing_site(config)
                if config_data:
                    config_manager.load_config()
                    SITE_CONFIG = config_data
                print(status)
            case '3':  # add site page
                pass
            case '4':  # reset config
                # print(config_manager.check_connection())
                print(config_manager.reset())
                SITE_CONFIG = config_manager.site_name
                
                
                # if validator.validate_unique_site()
                # file_manager.save_config(config)
