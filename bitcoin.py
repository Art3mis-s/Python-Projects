import sys
import requests
# getting value from command-line argument
if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

# Get current price of Bitcoin as a float a print with the value of the command-line
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total_amount = bitcoin * value
    print(f"${total_amount:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit(1)