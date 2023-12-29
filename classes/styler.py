"""
Style console commands, parsing strings.
"""
from colorama import Fore, Style

from app_config.app_notices import ERROR
from app_config.settings import DEFAULT_MODULE, DEFAULT_SITE_CONFIG
from classes.exceptions import TooManyArguments, UnexpectedSideParameter
from modules.parser_manager.template import exclude_words, status_1, status_2, status_3, correct_words, accepted_words, status_1_mod, status_2_mod, status_3_mod


class Styler:

    def __init__(self) -> None:
        self.styler_dict = {
            'price': self.price_styler,
            'side_taker': self.side_taker_styler,
            'remove_extra': self.remove_extra_chars,
        }

    def accept_data_styler(data):
        for word in accepted_words:
            if word in data:
                return True
        return False

    @staticmethod
    def set_status_code(data):
        for status in status_1_mod:
            if status in data:
                return 1
        for status in status_2_mod:
            if status in data:
                return 2
        for status in status_3_mod:
            if status in data:
                return 3
        return "Undefined"
    
    @staticmethod
    def is_code(string):
        if string in status_1:
            return 1
        if string in status_2:
            return 2
        if string in status_3:
            return 3

    def set_status_code_old(self, text):
        for string in correct_words:
            if string in text:
                return self.is_code(string)
        return "Undefined"
    
    @staticmethod
    def reset_all_styles() -> None:
        """
        Clearing the input style.
        """
        print("\x1B[0m" + Fore.RESET, end='', flush=True)

    @staticmethod
    def exclude_data_styler(checked_data: str) -> bool:
        """
        Searching wrong data.
        """
        for exclusion_word in exclude_words:
            if exclusion_word in checked_data:
                return True
        return False

    @staticmethod
    def module_styler(module: str) -> str:
        """
        Colored selected module.
        """
        if module == DEFAULT_MODULE or module == DEFAULT_SITE_CONFIG:
            return Fore.RED + module + Style.RESET_ALL
        return Fore.MAGENTA + module + Style.RESET_ALL
    
    def cmd_builder(self, program_name, module, site_config, cmd_input) -> str:
        """
        Build cmd logic view.
        """
        if module == DEFAULT_MODULE:
            return f"{program_name}({self.module_styler(module)}){cmd_input} "
        return f"{program_name}({self.module_styler(module)})\({self.module_styler(site_config)}){cmd_input} "
    
    @staticmethod
    def side_taker_styler(string, side):
        """
        Return right or left taken string side.
        Delimiter is Upper letter in string
        """
        try:
            if side not in ['left', 'right']:
                raise UnexpectedSideParameter
            values = string.strip().split()
            middle = [values[0]]

            if len(values) > 2:
                for i in values[1:]:
                    if i[0].isupper():
                        middle.append(i)
                    else:
                        middle.append(f'{middle.pop(-1)} {i}')

            # if len(middle) > 2:
            #     raise TooManyArguments
            
            if side == 'left':
                return middle[0]
            return middle[-1]
        except TooManyArguments:
            return f'[{ERROR}] Too many given arguments to unpack (expected 1-2)'

    @staticmethod
    def remove_extra_chars(text: str) -> str:
        """
        Removes extra chars in some str
        """
        if '\n' in text:
            text = text.strip().replace('\n', ' ')
        return text
    
    @staticmethod
    def __is_empty_string(price: str):
        if price is None:
            return True

        price = price.replace(' ', '')
        price = price.replace(chr(160), '')
        
        if not price:
            return True
        return False
    
    @staticmethod
    def __add_float_part(float_part: str):
        if float_part:
            return float_part
        return ",00"
    
    @staticmethod
    def __add_currency(currency, price_currency: bool):
        if currency is None:
            currency = "₽"
        if price_currency:
            return f" {currency}"
        return ""

    def price_styler(self, price: str, price_currency=False):
        """
        Return price in format like '1 000 000.00'
        """
        try:
            if self.__is_empty_string(price):
                return 'Сумма не указана'
            
            price = price.replace(' ', '')
            price = price.replace(chr(160), '')

            if not price[0].isdigit():
                currency = price[0]
                price = price[1:]
            elif not price[-1].isdigit():
                currency = price[-1]
                price = price[:-1]
            else:
                currency = None

            if '.' in price or ',' in price:
                price = price.replace('.', ',')
                float_part = price[price.rfind(','):]
                price = price[:price.rfind(',')]
            else:
                float_part = None

            new_price = ''
            char_count = 0
            for char in price[::-1]:
                char_count += 1
                new_price += char
                if char_count != len(price) and char_count % 3 == 0:
                    new_price += chr(160)
            new_price = new_price[::-1]
            
            new_price += self.__add_float_part(float_part)
            
            new_price += self.__add_currency(currency, price_currency)

            return new_price
        
        except TooManyArguments:
            return f'[{ERROR}] Too many given arguments to unpack (expected 1-2)'
        
    # @staticmethod
    # def old_price_styler(price: str, price_currency=False):
    #     """
    #     Return price in format like '1 000 000.00'
    #     """
    #     try:
    #         st = ''
    #         elements = []
    #         price = price.replace(' ', '')
    #         price = price.replace(chr(160), '')

    #         if price[0].isdigit():
    #             for i in price[::-1]:
    #                 if not i.isdigit():
    #                     st += i
    #                     continue
    #                 st = st[::-1]
    #                 elements.append(st)
    #                 price = price.replace(st, '')

    #                 elements.append(price)
    #                 break

    #         elements = sorted(elements)

    #         match len(elements):
    #             case 1:
    #                 price = elements[0]
    #             case 2:
    #                 price, currency = elements               
    #             case _:
    #                 raise TooManyArguments
    #         float_part = ''
    #         count_ = 0
    #         new_price = ''

    #         if '.' in price or ',' in price:
    #           price = price.replace('.', ',')
    #           float_part = price[price.rfind(','):]
    #           price = price[:price.rfind(',')]
                                
    #         for i in price[::-1]:
    #             new_price += i
    #             count_ += 1
    #             if count_ % 3 == 0 and count_ != len(price):
    #                 new_price += chr(160)
    #         new_price = new_price[::-1]

    #         if not float_part:
    #             float_part = ',00'

    #         new_price += float_part
    #         if price_currency:
    #             return f'{new_price} {currency}'
    #         return new_price
    #     except TooManyArguments:
    #         return f'[{ERROR}] Too many given arguments to unpack (expected 1-2)'
        
    def console_input_styler(self, help_string):
        answer = input(help_string + Fore.GREEN + "\x1B[3m").strip()
        self.reset_all_styles()
        return answer

    # def console_help_strings_styler(self, string):
    #     return Fore.GREEN + "\x1B[3m" + string


if __name__ == '__main__':
    styler = Styler()
    
    vvv = 'fdfdf'
    text = """
                                        аукцион в электронной форме, участниками которого могут быть только субъекты малого и среднего предпринимательства,
(№ ЦА 117-23) по выбору организации на право заключения договора на поставку персональных компьютеров (включающих в себя: системный блок, монитор, клавиатура, манипулятор «мышь»), моноблоков и ноутбуков для обеспечения рабочих мест работников Керченского филиала ФГУП «НИКИМП».
                                    """
    # print(text)
    # print(styler.new_price_styler(value, True))
    # print(value.isdigit())
    # print(styler.remove_extra_chars(text))
    # print(styler.side_taker_styler(string, side='left'))
    # print(vvv[0].isupper())

    def get_domain(url: str) -> str:
        """
        Return the site domain
        """
        return url[url.find('/') + 2:url.find('/', 8)]
    

    url = 'https://zakupki.gov.ru/epz/order/notice/notice223/common-info.html?noticeInfoId=15828618'
    # domain = get_domain(url)
    # print(get_domain(url))

    # print(domain in url)

    def is_empty_string(price: str):
        if price is None:
            return True

        price = price.replace(' ', '')
        price = price.replace(chr(160), '')
        
        if not price:
            return True
        return False

    def new_price_styler(price: str, price_currency=False):
        """
        Return price in format like '1 000 000.00'
        """
        try:
            if is_empty_string(price):
                return 'Сумма не указана'

            if not price[0].isdigit():
                currency = price[0]
                price = price[1:]
            elif not price[-1].isdigit():
                currency = price[-1]
                price = price[:-1]
            else:
                currency = None

            if '.' in price or ',' in price:
                price = price.replace('.', ',')
                float_part = price[price.rfind(','):]
                price = price[:price.rfind(',')]
            else:
                float_part = None

            new_price = ''
            char_count = 0
            for char in price[::-1]:
                char_count += 1
                new_price += char
                if char_count != len(price) and char_count % 3 == 0:
                    new_price += " "
            new_price = new_price[::-1]

            if float_part:
                new_price += float_part
            else:
                new_price += ",00"
            
            if price_currency:
                new_price += f" {currency}"
            return price, float_part, currency, new_price
        
        except TooManyArguments:
            return f'[{ERROR}] Too many given arguments to unpack (expected 1-2)'

    value = '1 175 369,46 ₽'  # 1 175 369,46 ₽
    value2 = '    17536946.123₽'  # 1 175 369,46 ₽
    value3 = ''
    # price = new_price_styler(value3, price_currency=True)
    # print(price)

    print(styler.price_styler(value3, price_currency=True))

