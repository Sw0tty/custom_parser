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
        "zakupki.gov.ru": 
            {
                'SECURE_CONNECTION':True,
                'PARSING_PAGES':
                    [

                        {   
                            'PAGE_NAME': 'Закупки',
                            'PAGE_URL': 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={search_str}&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber={page}&recordsPerPage=_{self.__RESULTS_PER_PAGE}&fz44=on&fz223=on&af=on&priceFromGeneral={self.__PRICE}&currencyIdGeneral=-1&publishDateFrom={DATE_DAYS_AGO}&publishDateTo={TODAY_DATE}',
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
