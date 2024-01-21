import requests

def is_api_working(api_url, payload=None):
    try:
        if payload:
            response = requests.post(api_url, json=payload)
        else:
            response = requests.get(api_url)
        
        # You can customize the conditions for considering an API as working
        return response.status_code == 200  # Assume a successful response code is 200 OK
    except requests.RequestException:
        return False

def main():
    input_file = "api.txt"
    output_file = "new.txt"
    ethereum_payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            api_url = line.strip()

            payload = ethereum_payload if "ethereum" in api_url.lower() else None

            if is_api_working(api_url, payload):
                print(f"Working API: {api_url}")
                outfile.write(api_url + "\n")

if __name__ == "__main__":
    main()