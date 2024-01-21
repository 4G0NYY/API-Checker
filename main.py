import requests

def is_api_working(api_url):
    try:
        response = requests.get(api_url)
        return response.status_code == 200
    except requests.RequestException:
        return False

def main():
    input_file = "api.txt"
    output_file = "new.txt"

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            api_url = line.strip()
            if is_api_working(api_url):
                print(f"Working API: {api_url}")
                outfile.write(api_url + "\n")

if __name__ == "__main__":
    main()
