from datetime import date


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
