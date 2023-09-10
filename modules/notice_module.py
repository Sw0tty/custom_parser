"""
MasterExcel notices
"""
from colorama import Fore, Style
from modules.help_module import CURRENT_MODULE


ERROR = Style.BRIGHT + Fore.RED + "ERROR" + Style.RESET_ALL
SUCCESS = Style.BRIGHT + Fore.GREEN + "SUCCESS" + Style.RESET_ALL
INFO = Style.BRIGHT + Fore.LIGHTCYAN_EX + "INFO" + Style.RESET_ALL

HELP = f"[{INFO}] Print 'help' for call list commands."
CANCELLED = f'[{INFO}] Cancelled'
FILE_CREATED = f'[{SUCCESS}] File created!'
UNEXPECTED = f'[{ERROR}] Unexpected command!'
FILE_UNDEFINED = f'[{ERROR}] File undefined!'
FILE_PATH = f'[{INFO}] Path to file: '
FILE_NAME = f'[{INFO}] Name of selected file: '
ERROR_FILE_EXTENSION = f'[{ERROR}] File must have html extension!'
RESET_MODULE = f'[{SUCCESS}] Module reset!'


def module_styler(module):
    # if CURRENT_MODULE == 'None-module':
    #     return Fore.RED + module + Style.RESET_ALL
    return Fore.MAGENTA + module + Style.RESET_ALL
