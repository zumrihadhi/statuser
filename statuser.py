import requests # library for making HTTP requests
import csv # library for reading and writing CSV files
from datetime import datetime # library for working with dates and times

def check_status():
    # Ask the user to input a list of URLs separated by commas
    urls = input("Enter the URLs (separated by commas): ").strip().split(",")

    # Define the field names for the CSV file
    fieldnames = ['URL', 'HTTP Status', 'Status', 'Time']

    # Define the name of the CSV file
    filename = "Statuser_output.csv"

    # Open the CSV file for writing
    with open(filename, 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row in the CSV file
        writer.writeheader()

        # Loop through the URLs
        for url in urls:
            try:
                # If the URL doesn't start with "http", add "https://" to the front
                if not url.startswith("http"):
                    url = "https://" + url
                # Make an HTTP GET request to the URL with a timeout of 5 seconds
                response = requests.get(url, timeout=5)
                # Get the HTTP status code from the response
                status_code = response.status_code
                # Initialize a variable to store the status as a string
                status = ""
                # Check the status code and set the status string accordingly
                if status_code == 200:
                    status = "OK"
                elif status_code == 404:
                    status = "Not Found"
                elif status_code == 500:
                    status = "Internal Server Error"
                else:
                    status = "Other error"

                # Write a row in the CSV file with the URL, HTTP status code, status, and current time
                writer.writerow({
                    'URL': url,
                    'HTTP Status': status_code,
                    'Status': status,
                    'Time': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                })

                # Print the results to the console
                print()
                print(f"Checking URL: {url}")
                print(f"HTTP Status: {status_code}")
                print(f"Status: {status}")
                print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print()
                
            # Handle exceptions if the request fails
            except requests.exceptions.RequestException as e:
                print(f"Checking URL: {url}")
                print("Unable to connect to the URL")
                print()
                # Continue with the next URL
                continue

# If the script is being run as the main module, run the check_status() function
if __name__ == "__main__":
    # Print a welcome message
    print("_"*52)
    print("\nWelcome to Statuser - A tool to check website status")
    print("_"*52)
    print()
    print("Author: Zumri Hadhi")
    print("Email: zumri@encryptasia.com")
    print("Website: encryptasia.com\n")
    check_status()
