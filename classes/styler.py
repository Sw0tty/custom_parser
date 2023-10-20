"""
Style console commands, parsing strings.
"""
from colorama import Fore, Style

from app_config.app_notices import ERROR
from app_config.settings import CURRENT_MODULE
from classes.exceptions import TooManyArguments, UnexpectedSideParameter


class Styler:

    @staticmethod
    def reset_all_styles():
        print("\x1B[0m" + Fore.RESET, end='', flush=True)

    @staticmethod
    def module_styler(module):
        """
        Colored selected module.
        Needed in console_version.
        """
        if module == CURRENT_MODULE:
            return Fore.RED + module + Style.RESET_ALL
        return Fore.MAGENTA + module + Style.RESET_ALL
    
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
    def price_styler(price: str, price_currency=False):
        """
        Return price in format like '1 000 000.00'
        """
        try:
            st = ''
            elements = []
            price = price.replace(' ', '')
            price = price.replace(chr(160), '')

            if price[0].isdigit():
                for i in price[::-1]:
                    if not i.isdigit():
                        st += i
                        continue
                    st = st[::-1]
                    elements.append(st)
                    price = price.replace(st, '')

                    elements.append(price)
                    break

            elements = sorted(elements)

            match len(elements):
                case 1:
                    price = elements[0]
                case 2:
                    price, currency = elements               
                case _:
                    raise TooManyArguments
            float_part = ''
            count_ = 0
            new_price = ''

            if '.' in price or ',' in price:
              price = price.replace('.', ',')
              float_part = price[price.rfind(','):]
              price = price[:price.rfind(',')]
                                
            for i in price[::-1]:
                new_price += i
                count_ += 1
                if count_ % 3 == 0 and count_ != len(price):
                    new_price += chr(160)
            new_price = new_price[::-1]

            if not float_part:
                float_part = ',00'

            new_price += float_part
            if price_currency:
                return f'{new_price} {currency}'
            return new_price
        except TooManyArguments:
            return f'[{ERROR}] Too many given arguments to unpack (expected 1-2)'

    @staticmethod
    def old_price_styler(price, price_currency=False):
        try:
            float(price)

            elements = sorted(price.split())

            match len(elements):
                case 1:
                    price = elements[0]
                case 2:
                    price, currency = elements                    
                case _:
                    raise TooManyArguments

            count_ = 0
            new_price = ''
            for i in price[-4::-1]:
                new_price += i
                count_ += 1
                if count_ % 3 == 0 and count_ != len(price) - 3:
                    new_price += ' '
            new_price = new_price[::-1] + price[-3::]

            dot = new_price.rfind('.')

            if dot < 0:
                print(price)
                new_price += ',00'
            if price_currency:
                return f'{price} {currency}'
            return new_price
        except TooManyArguments:
            return f'[{ERROR}] Too many given arguments to unpack (expected 1-2)'
        
    def console_user_input_styler(self, help_string):
        answer = input(help_string + Fore.GREEN + "\x1B[3m").strip()
        self.reset_all_styles()
        return answer
    
    def console_help_strings_styler(self, string):
        style_string = Fore.GREEN + "\x1B[3m" + string
        
        return style_string
    
    def get_main_url(self):
        pass

if __name__ == '__main__':
    styler = Styler()
    value = '1 175 369,46 ₽'  # 1 175 369,46 ₽
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
    domain = get_domain(url)
    # print(get_domain(url))

    print(domain in url)

