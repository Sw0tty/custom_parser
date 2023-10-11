from datetime import date


TODAY_DATE = date.today().strftime('%d.%m.%Y')

NAME = 'MasterExcel'
MASTER_CMD_INPUT = r'\>'
CURRENT_MODULE = 'None-module'

PARSER_HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

SUPPORTED_FORMATS = [('CSV file', '*.csv'), ('Excel book', '*.xlsx'), ('Excel book 97-2003', '*.xls')]

DEFAULT_NAME_SAVE_FILE = f'Выгрузка {TODAY_DATE}'
DEFAULT_FILE_SHEET_NAME = f'Выгрузка {TODAY_DATE}'

# EXCEL_TEMPLATE = {
#     DEFAULT_FILE_SHEET_NAME: [
#         ['Закупки по', 'Наименование закупки', 'Начальная (максимальная) цена контракта',
#          'Наименование заказчика', 'Дата окончания подачи заявок', 'Интерес',
#          'Категория', 'Ссылка']
#     ]
# }

EXCEL_TEMPLATE = [
    ['Закупки по', 'Наименование закупки', 'Начальная (максимальная) цена контракта',
         'Наименование заказчика', 'Дата окончания подачи заявок', 'Интерес',
         'Категория', 'Ссылка']
         ]

EXCEL_EXPORT_COLUMNS_TEMPLATE = ['Закупки по', 'Наименование закупки', 'Начальная (максимальная) цена контракта',
         'Наименование заказчика', 'Дата окончания подачи заявок', 'Интерес',
         'Категория', 'Ссылка']

# Main site block with parsing info
MAIN_PARSER_BLOCK = "search-registry-entry-block box-shadow-search-input"

SITE_BLOCK = {
    "search-registry-entry-block box-shadow-search-input": 
        {
            'purchases': 'col-9 p-0 registry-entry__header-top__title text-truncate',
            'name': 'registry-entry__body-value',
            'price': 'price-block__value',
            'customer': 'registry-entry__body-href',
            'end_date': 'data-block mt-auto',  # 'data-block mt-auto': styler - ''
            'org_href': 'registry-entry__header-mid__number',
        }
}

SITE_BLOCK_template = [
    {
        "SITE_NAME (main site name page)": 
            {
                'PARSING_PAGES':
                    [
                        {
                            'PAGE(autonum)':
                                {
                                    'PAGE_NAME': '',  # html title block name
                                    'MAIN_PARSE_INFO_BLOCK': '',  # main block with all infos about (INFO_BLOCKS)
                                    'INFO_BLOCKS': []
                                }
                        },
                    ],
                'PAGINATOR_CLASS_NAME': '',  # Name of sita paginator
                'EXPORT': {
                    'EXCEL': {
                        'EXCEL_COLUMNS_TITLE': [],
                        'ROW_COMMON_TITLES': []
                    },
                    # 'JSON': ''
                }
                # 'OPTIONS': {

                # }
            }
    },
]

SITE_BLOCK_NEW = [
    {
        "SITE_NAME (main site name page)": 
            {
                'PARSING_PAGES':
                    [
                        {
                            '0':
                                {                                   
                                    'PAGE_NAME': 'Закупки',
                                    'MAIN_PARSE_INFO_BLOCK': 'search-registry-entry-block box-shadow-search-input',
                                    'INFO_BLOCKS': []
                                }
                        },
                    ],
                'PAGINATOR_CLASS_NAME': 'paginator-block',
                'EXPORT': {
                    'EXCEL': {
                        'EXCEL_COLUMNS_TITLE': ['Закупки по', 'Наименование закупки', 'Начальная (максимальная) цена контракта',
                                'Наименование заказчика', 'Дата окончания подачи заявок', 'Интерес',
                                'Категория', 'Ссылка'],
                        'ROW_COMMON_TITLES': []
                    },
                    # 'JSON': ''
                }
            }
    },
]

# Classes in main parsing block
PARSER_DIVS_DICT = {
    'purchases': 'col-9 p-0 registry-entry__header-top__title text-truncate',
    'name': 'registry-entry__body-value',
    'price': 'price-block__value',
    'customer': 'registry-entry__body-href',
    'end_date': 'data-block mt-auto',
    'org_href': 'registry-entry__header-mid__number',
}

# PARSER_DIVS_DICT_OLD = {
#     'purchases': ('col-9 p-0 registry-entry__header-top__title text-truncate', 'Закупки по: '),
#     'name': ('registry-entry__body-value', 'Наименование закупки: '),
#     'price': ('price-block__value', 'Цена: '),
#     'customer': ('registry-entry__body-href', 'Заказчик: '),
#     'end_date': ('data-block mt-auto', 'Дата окончания: '),
#     'org_href': ('registry-entry__header-mid__number', 'Ссылка: '),
# }

ZAK_44 = 'https://zakupki.gov.ru/epz/order/notice/ea20/view/common-info.html?regNumber='


# Style the price value
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
        new_price = new_price[::-1] + price[-3::]
        return new_price
    except ValueError:
        return price


if __name__ == '__main__':
    print(price_styler('123456.78'))
