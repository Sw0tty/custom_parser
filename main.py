"""
Main File MasterExcel
"""
from classes.mas_parser import Parser
from modules.parser.file_parser import FileParser
from modules.parser.site_parser import SiteParser
from modules.rebuilder import Rebuilder
from app_config.settings import NAME, MASTER_CMD_INPUT, PARSER_DIVS_DICT, ZAK_44, module_styler
from app_config.app_notices import UNEXPECTED, RESET_MODULE, INFO
from app_config.help_commands import CURRENT_MODULE, MAIN_COMMANDS_DICT, MODULES, PARSER_COMMANDS_DICT, REBUILDER_COMMANDS_DICT, FILE_PARSER_COMMANDS_DICT, SITE_PARSER_COMMANDS_DICT
from classes.parent import MasterExcel

parser = Parser(PARSER_COMMANDS_DICT)
file_parser = FileParser(FILE_PARSER_COMMANDS_DICT)
site_parser = SiteParser(SITE_PARSER_COMMANDS_DICT)
rebuilder = Rebuilder(REBUILDER_COMMANDS_DICT)
master_excel = MasterExcel(MAIN_COMMANDS_DICT)

print(f"[{INFO}] Print 'help' for call list commands.")


def reset_module():
    print("All modules:")
    for module in MODULES.keys():
        print(f'\t{module_styler(module)} - {MODULES[module]}')
    return input('Print module: ').strip().lower()


while True:

    input_command = input(f"{NAME}({module_styler(CURRENT_MODULE)}){MASTER_CMD_INPUT} ")

    match input_command:
        case 'help':
            master_excel.help()
            continue
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
                print(file_parser.parse_file())
            case '6':
                print(file_parser.excel_import(PARSER_DIVS_DICT))
            case _:
                print(UNEXPECTED)
    elif CURRENT_MODULE == 'site-parser':
        match input_command:
            case '1':
                site_parser.help()
            # case '2':
            #     print(site_parser.set_file_path())
            # case '3':
            #     print(site_parser.get_file_path())
            # case '4':
            #     print(site_parser.get_file_name())
            case _:
                print(UNEXPECTED)
    elif CURRENT_MODULE == 'rebuilder':
        match input_command:
            case '1':
                rebuilder.help()
            case '2':
                print(rebuilder.set_file_path())
            case '3':
                print(rebuilder.get_file_path())
            case '4':
                print(rebuilder.get_file_name())
            case '5':
                print(rebuilder.check_rebuild())
            case '6':
                print(rebuilder.prepare_rebuild())
            case '7':
                print(rebuilder.excel_import())
            case _:
                print(UNEXPECTED)
