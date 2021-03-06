from requests import get, utils


def currency_rates(valute):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encod = utils.get_unicode_from_response(response)
    list_content = encod.split("<CharCode>")
    for i in list_content:
        if valute in i:
            list_end = i.replace("/", "").split("<Value>")
            return list_end[-2]


print(currency_rates("USD"))
print(currency_rates("EUR"))