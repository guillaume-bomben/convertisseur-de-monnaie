import datetime
from forex_python.converter import *

# Création d'une instance de CurrencyRates
c = CurrencyRates()

def save_conversion_history(amount, from_currency, to_currency, converted_amount):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conversion_info = f"{timestamp}: {amount} {from_currency} => {converted_amount} {to_currency}\n"
    with open('conversion_history.txt', 'a') as file:
        file.write(conversion_info)

def check_valid_currency(currency):
    currency_codes = CurrencyCodes()
    if currency_codes.get_currency_name(currency) is None:
        return False
    return True


def change_curency():
    from_currency = input("Entrez une devise de départ :")
    to_currency = input("Entrez une devise de sortie :")
    amount = int(input("Entrez le montant a convertir :"))
    
    while check_valid_currency(from_currency) == False or check_valid_currency(to_currency) == False:
        print("Une des devise n'est soit pas valide , soit non prie en charge par la bibliotheque")
        from_currency = input("Entrez une devise de départ :")
        to_currency = input("Entrez une devise de sortie :")
        amount = int(input("Entrez le montant a convertir :"))
        
    converted_amount = c.convert(from_currency,to_currency,amount)
    print(f"Le taux de change entre {from_currency} et {to_currency} est : {c.get_rate(from_currency,to_currency)}")
    print(f"{amount} {from_currency} est equivalent a environ {converted_amount} {to_currency}")
    
    save_conversion_history(amount,from_currency,to_currency,converted_amount)


change_curency()