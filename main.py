"""
Main File MasterExcel
"""

from app_config.settings import NAME, MASTER_CMD_INPUT, PARSER_DIVS_DICT, CURRENT_MODULE
from app_config.app_notices import RESET_MODULE, INFO, HELP
from app_config.help_commands import MAIN_COMMANDS_DICT, MODULES, REBUILDER_COMMANDS_DICT,\
    FILE_PARSER_COMMANDS_DICT, SITE_PARSER_COMMANDS_DICT
from classes.modules_default import MainMethods
from modules.parser.file_parser import FileParser
from modules.parser.site_parser import SiteParser
from modules.rebuilder import Rebuilder
from classes.styler import Styler


master_excel = MainMethods(commands=MAIN_COMMANDS_DICT)
file_parser = FileParser(commands=FILE_PARSER_COMMANDS_DICT)
site_parser = SiteParser(commands=SITE_PARSER_COMMANDS_DICT)
rebuilder = Rebuilder(commands=REBUILDER_COMMANDS_DICT)
styler = Styler()

# print(rebuilder.EXPORT_DATA)
# print(rebuilder.EXPORT_DATA)

# rebuilder.EXPORT_DATA.append([2, 3, 4])
# print(file_parser.EXPORT_DATA)

print(f"""[{INFO}] Print {HELP} for call list commands.""")


def reset_module():
    print("All modules:")
    for module in MODULES.keys():
        print(f'\t{styler.module_styler(module)} - {MODULES[module]}')
    return input('Print module: ').strip().lower()


while True:

    # input_command = input(f"{NAME}({styler.module_styler(CURRENT_MODULE)}){MASTER_CMD_INPUT} ")
    input_command = styler.console_user_input_styler(f"{NAME}({styler.module_styler(CURRENT_MODULE)}){MASTER_CMD_INPUT} ")
    
    match input_command:
        case 'help':
            master_excel.help()
        case 'set':
            new_module = reset_module()
            if new_module and new_module in MODULES:
                # if new_module == 'parser':
                #     pass
                CURRENT_MODULE = new_module
                print(RESET_MODULE)
                continue
        case 'reset':
            CURRENT_MODULE = 'None-module'
            print(RESET_MODULE)
            continue
        case 'exit':
            break

    if CURRENT_MODULE == 'file-parser':
        match input_command:
            case '1':
                file_parser.help()
            case '2':
                print(file_parser.get_file_path())
            case '3':
                print(file_parser.set_file_path())
            case '4':
                print(file_parser.get_file_name())
            case '5':
                print(file_parser.parse_file(PARSER_DIVS_DICT))
            case '6':
                print(file_parser.excel_export())

    elif CURRENT_MODULE == 'site-parser':
        match input_command:
            case '1':
                site_parser.help()
            case '2':
                print(site_parser.to_empty_list())
            case '3':
                print(site_parser.add_info())
            case '4':
                print(site_parser.excel_export())
            case '5':
                print(site_parser.get_url())

    elif CURRENT_MODULE == 'rebuilder':
        match input_command:
            case '1':
                rebuilder.help()
            case '2':
                print(rebuilder.set_selected_file())
            case '3':
                rebuilder.get_params_status()
            case '4':
                print(rebuilder.get_file_name())
            case '5':
                print(rebuilder.get_rebuild_status())
            case '6':
                print(rebuilder.prepare_rebuild())
            case '7':
                print(rebuilder.excel_export())
