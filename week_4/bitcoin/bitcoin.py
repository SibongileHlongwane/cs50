import sys, requests

if len(sys.argv) != 2: sys.exit("Missing command-line argument")
try: n = float(sys.argv[1])
except: sys.exit("Command-line argument is not a number")

API_KEY = "c4972e199095164e2a56cd06da3aac6fe7c27ef37009eed9a734ace2df481237"  

try:
    url = f"https://api.coincap.io/v2/assets/bitcoin?apiKey={API_KEY}"
    price = requests.get(url).json()["data"]["priceUsd"]
    print(f"${float(price)*n:,.4f}")
except:
    sys.exit("Error fetching Bitcoin price")

 