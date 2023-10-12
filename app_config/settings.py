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
        "SITE_NAME (main site url page)": 
            {
                'PARSING_PAGES':
                    [
                        {
                            'PAGE(autonum)':
                                {
                                    'PAGE_URL': '',
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

SITE_PARSER_SETTINGS = [
    {
        "https://zakupki.gov.ru": 
            {
                'PARSING_PAGES':
                    [
                        {
                            '0':
                                {   
                                    'PAGE_URL': 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={search_str}&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber={page}&recordsPerPage=_{self.__RESULTS_PER_PAGE}&fz44=on&fz223=on&af=on&priceFromGeneral={self.__PRICE}&currencyIdGeneral=-1&publishDateFrom={DATE_DAYS_AGO}&publishDateTo={TODAY_DATE}',                             
                                    'PAGE_NAME': 'Закупки',
                                    'MAIN_PARSE_INFO_BLOCK': 'search-registry-entry-block box-shadow-search-input',
                                    'INFO_BLOCKS':
                                        [  # Custom field, class/custom value to add, styler
                                            (False, 'col-9 p-0 registry-entry__header-top__title text-truncate', None),  # purchases
                                            (False, 'registry-entry__body-value', None),  # name
                                            (False, 'price-block__value', None),  # price
                                            (False, 'registry-entry__body-href', None),  # customer
                                            (False, 'data-block mt-auto', None),  # end_date
                                            (True, 'CUSTOM_FIELDS'[0], None),
                                            (True, '', None),
                                            (False, 'registry-entry__header-mid__number', None),  # Href
                                        ],
                                    'CUSTOM_FIELDS': []
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

    for i in SITE_PARSER_SETTINGS[0].keys():
        print(i)
    
    print(SITE_PARSER_SETTINGS[0]['https://zakupki.gov.ru']['PARSING_PAGES'])
    
