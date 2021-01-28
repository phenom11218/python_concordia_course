from babel.numbers import format_currency

print(format_currency(1099.98,"USD",locale='en_US'))
print(format_currency(1099.98,"USD",locale='en_CA'))
print(format_currency(1099.98,"USD",locale='fr_CA'))