import requests 

Api_Key = "Enter your own API Key here"

# Will get conversions relative to USD
url = f"https://v6.exchangerate-api.com/v6/{Api_Key}/latest/USD"

info = requests.get(url)

# This converts the data in json to a python dictionary
data = info.json()

rates = data["conversion_rates"]
try:
    amount = float(input("Enter the amount of the currency you want to be converted :"))
except ValueError:
    print("Please enter a valid number ")


from_currency = input("Enter the currency you want to convert, add the exact input , example --> for yen use JPY :").upper()

if from_currency not in data["conversion_rates"]:
    print("Enter a valid currency")
    exit()


to_currency = input("Enter the currecny you want , same input scheme should be used as above :").upper()

if to_currency not in data["conversion_rates"]:
    print("Enter a valid currency")
    exit()


# The main currency converting function
def convertor(amount, from_currency, to_currency,):

    # Instead of changing the url again and again for these conversions , we use USD as a common point through which conversion can be done
    amount_in_USD =  amount / data["conversion_rates"][from_currency]
    amount_of_to_currency = amount_in_USD * data["conversion_rates"][to_currency]

    return amount_of_to_currency

result = convertor(amount, from_currency, to_currency)

print(f"{amount} {from_currency} = {result} {to_currency}")