# В файле currency_converter.py
def convert(from_currency, to_currency, amount, rates):
    initial_amount = amount
    if from_currency != 'EUR':
        amount = amount / rates[from_currency]
    output = round(amount * rates[to_currency], 2)
    print('{} {}  = {} {}'.format(initial_amount, from_currency, output, to_currency))