from datetime import date
from colorama import Fore, Style


TODAY = date.today().strftime('%d.%m.%Y')

NAME = 'MasterExcel'
MASTER_CMD_INPUT = r'\>'

EXCEL_TEMPLATE = {
    f'Выгрузка {TODAY}': [
        ['Закупки по', 'Наименование закупки', 'Начальная (максимальная) цена контракта',
         'Наименование заказчика', 'Дата окончания подачи заявок', 'Интерес',
         'Категория', 'Ссылка']
    ]
}

MAIN_PARSER_BLOCK = "search-registry-entry-block box-shadow-search-input"

PARSER_HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

PARSER_DIVS_DICT = {
    'purchases': ('col-9 p-0 registry-entry__header-top__title text-truncate', 'Закупки по: '),
    'name': ('registry-entry__body-value', 'Наименование закупки: '),
    'price': ('price-block__value', 'Цена: '),
    'customer': ('registry-entry__body-href', 'Заказчик: '),
    'end_date': ('data-block mt-auto', 'Дата окончания: '),
    'org_href': ('registry-entry__header-mid__number', 'Ссылка: '),
}

ZAK_44 = 'https://zakupki.gov.ru/epz/order/notice/ea20/view/common-info.html?regNumber='


def module_styler(module):
    # if CURRENT_MODULE not in MODULES:
    #     return Fore.RED + module + Style.RESET_ALL
    return Fore.MAGENTA + module + Style.RESET_ALL


def price_styler(price):
    try:
        float(price)
        count_ = 0
        new_price = ''
        for i in price[-4::-1]:
            new_price += i
            count_ += 1
            if count_ % 3 == 0 and count_ != len(price) - 3:
                new_price += ' '
        new_price = (new_price[::-1] + price[-3::]).replace('.', ',')
        return new_price
    except ValueError:
        return price


if __name__ == '__main__':
    print(price_styler('123456.78'))
