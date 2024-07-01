from forex_python.converter import CurrencyRates, RatesNotAvailableError

def convert_currency(amount, from_currency, to_currency):
    try:
        c = CurrencyRates()
        rate = c.convert(from_currency, to_currency, amount)
        return rate
    except RatesNotAvailableError:
        return None

def main():
    print("Welcome to Currency Converter!")
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            from_currency = input("Enter the currency you have (e.g., USD, EUR): ").upper()
            to_currency = input("Enter the currency you want to convert to (e.g., USD, EUR): ").upper()

            converted_amount = convert_currency(amount, from_currency, to_currency)
            if converted_amount is not None:
                print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
            else:
                print(f"Unable to convert {from_currency} to {to_currency}. Please check your input currencies.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        choice = input("\nDo you want to perform another conversion? (yes/no): ").lower()
        if choice != 'yes':
            break

    print("Thank you for using the Currency Converter!")

if __name__ == "__main__":
    main()
