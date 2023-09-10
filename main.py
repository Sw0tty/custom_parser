"""
Main File MasterExcel
"""
from classes.mas_parser import Parser
from classes.parser.file_parser import FileParser
from classes.rebuilder import Rebuilder
from modules.parser_params import NAME, MASTER_CMD_INPUT, PARSER_DIVS_DICT, ZAK_44
from modules.notice_module import module_styler, HELP, UNEXPECTED, RESET_MODULE
from modules.help_module import CURRENT_MODULE, COMMANDS_DICT, MODULES, PARSER_COMMANDS_DICT, REBUILDER_COMMANDS_DICT, FILE_PARSER_COMMANDS_DICT, SITE_PARSER_COMMANDS_DICT


parser = Parser(PARSER_COMMANDS_DICT)
file_parser = FileParser(FILE_PARSER_COMMANDS_DICT)
# site_parser = SiteParser(SITE_PARSER_COMMANDS_DICT)
rebuilder = Rebuilder(REBUILDER_COMMANDS_DICT)

print(HELP)


def reset_module():
    print("All modules:")
    for module in MODULES.keys():
        print(f'\t{module_styler(module)} - {MODULES[module]}')
    return input('Print module: ').strip().lower()


while True:

    input_command = input(f"{NAME}({module_styler(CURRENT_MODULE)}){MASTER_CMD_INPUT} ")

    match input_command:
        case 'help':
            for key in COMMANDS_DICT.keys():
                print(f'\t{key} - {COMMANDS_DICT[key]}')
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
                rebuilder.help()
            case '2':
                print(rebuilder.set_file_path())
            case '3':
                print(rebuilder.get_file_path())
            case '4':
                print(rebuilder.get_file_name())
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
