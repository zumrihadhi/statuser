# Statuser

This is a Python script that allows you to check the status of websites and save the results to a CSV file. 

You are prompted to enter a list of URLs separated by commas, and the script sends GET requests to each URL, retrieves the HTTP status code, and determines the status of the website. The results, including the URL, HTTP status code, status, and time, are saved to a CSV file named "Statuser_output.csv". 

If there is an exception while sending the GET request, a message indicating that the URL could not be connected to is displayed
