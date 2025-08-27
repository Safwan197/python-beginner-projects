# Currency Converter

currency_rates = {
    "USD": 285.7,  # US Dollar
    "EUR": 332.40, # Euro
    "GBP": 382.95, # British Pound
    "AED": 77.65,  # UAE Dirham
    "SAR": 76.0,   # Saudi Riyal
    "CNY": 39.3,   # Chinese Yuan
    "JPY": 1.95,   # Japanese Yen
    "AUD": 192.4,  # Australian Dollar
    "CAD": 211.8,  # Canadian Dollar
    "CHF": 326.7   # Swiss Franc
}
pkr = float(input("Enter Amount (PKR)  : "))
currency = input("Select Currency (USD,AED,SAR,GBP,EUR,CNY,JPY,AUD,CAD,CHF)  : ").upper()

if currency in currency_rates:      # Condition checking if currency available in above dictionary
    converted_amount = pkr / currency_rates[currency]
else:
    print("Amount Not Found")

print("Here's your Converted Amount : ", converted_amount , currency)
