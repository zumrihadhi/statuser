import requests
import csv
from datetime import datetime

def check_status():
    urls = input("Enter the URLs (separated by commas): ").strip().split(",")
    fieldnames = ['URL', 'HTTP Status', 'Status', 'Time']
    filename = "Statuser_output.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for url in urls:
            try:
                if not url.startswith("http"):
                    url = "https://" + url
                response = requests.get(url, timeout=5)
                status_code = response.status_code
                status = ""
                if status_code == 200:
                    status = "OK"
                elif status_code == 404:
                    status = "Not Found"
                elif status_code == 500:
                    status = "Internal Server Error"
                else:
                    status = "Other error"

                writer.writerow({
                    'URL': url,
                    'HTTP Status': status_code,
                    'Status': status,
                    'Time': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                })
                print(f"Checking URL: {url}")
                print(f"HTTP Status: {status_code}")
                print(f"Status: {status}")
                print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print()
                
            except requests.exceptions.RequestException as e:
                print(f"Checking URL: {url}")
                print("Unable to connect to the URL")
                print()
                continue

if __name__ == "__main__":
    print("_"*52)
    print("\nWelcome to Statuser - A tool to check website status")
    print("_"*52)
    print()
    print("Author: Zumri Hadhi")
    print("Email: zumri@encryptasia.com")
    print("Website: encryptasia.com\n")
    check_status()
