from currency_converter import CurrencyConverter

def convert_currency(amount, from_curr, to_curr):
    c = CurrencyConverter()
    try:
        result = c.convert(amount, from_curr.upper(), to_curr.upper())
        print(f"{amount} {from_curr} is equal to {result:.2f} {to_curr}")
    except ValueError:
        print("One of the currency codes is not supported.")

if __name__ == "__main__":
    print("--- Real-Time Currency Converter ---")
    amt = float(input("Enter Amount: "))
    curr_from = input("From Currency (e.g., USD): ")
    curr_to = input("To Currency (e.g., INR): ")
    convert_currency(amt, curr_from, curr_to)
