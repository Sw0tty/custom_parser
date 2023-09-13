"""
File with help commands
"""


CURRENT_MODULE = 'None-module'

MODULES = {
    'rebuilder': 'rebuilding the excel file for template',
    'file-parser': 'parse the file',
    'site-parser': 'parse the site',
}

MAIN_COMMANDS_DICT = {
    'set': 'set module',
    'reset': 'reset current module',
    'exit': 'close master',
}

FILE_PARSER_COMMANDS_DICT = {
    '1': 'all commands in current module',
    '2': 'get current parse file',
    '3': 'set new parse file',
    '4': 'get name file',
    '5': 'parse the file',
    '6': 'export in excel file',
}

SITE_PARSER_COMMANDS_DICT = {
    '1': 'all commands in current module',
    '2': 'get actual request type',
    '3': 'set new request type',
    '4': 'get actual parse source',
    '5': 'set new parse source',
    '6': 'parse the resource',
    '7': 'get name file',
    '8': 'export in excel file',
}

PARSER_COMMANDS_DICT = {
    '1': 'all commands in current module',
    '2': 'get actual request type',
    '3': 'set new request type',
    '4': 'get actual parse source',
    '5': 'set new parse source',
    '6': 'parse the resource',
    '7': 'get name file',
    '8': 'export in excel file',
}

REBUILDER_COMMANDS_DICT = {
    '1': 'all commands in current module',
    '2': 'set file for rebuild',
    '3': 'get file path',
    '4': 'get file name',
    '5': 'check rebuild info',
    '6': 'prepare rebuild to export in excel file',
    '7': 'export rebuild in excel file',
}
