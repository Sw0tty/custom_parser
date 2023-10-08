"""
"""
from colorama import Fore, Style

from app_config.app_notices import ERROR
from app_config.settings import CURRENT_MODULE
from classes.exceptions import TooManyArguments, UnexpectedSideParameter


class Styler:

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
                        print(middle[-1])
                    else:
                        middle.append(f'{middle.pop(-1)} {i}')

            if len(middle) > 2:
                raise TooManyArguments
            
            if side == 'left':
                return middle[0]
            return middle[-1]
        except TooManyArguments:
            return f'[{ERROR}] Too many given arguments to unpack (expected 1-2)'


    @staticmethod
    def price_styler(price, price_currency=False):
        """
        Return price in format like '1 000 000.00'
        """
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
                new_price += '.00'
            if price_currency:
                return f'{price} {currency}'
            return new_price
        except TooManyArguments:
            return f'[{ERROR}] Too many given arguments to unpack (expected 1-2)'

if __name__ == '__main__':
    styler = Styler()
    value = '200000.00'
    vvv = 'fdfdf'
    string = '223-ФЗ Запрос котировок в электронной форме, участниками которого могут быть только субъекты малого и среднего предпринимательства'
    # print(styler.price_styler(value))
    print(styler.taker_styler(string, side='left'))
    print(vvv[0].isupper())
