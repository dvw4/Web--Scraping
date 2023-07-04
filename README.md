# Web--Scraping
A python program that periodically downloads and extracts the information about the
most active stocks on NYSE (The New York Stock Exchange), and saves/updates the information
in a database.

In an infinite loop, the python program sends HTTP requests to get the web page containing the
data about the most active stocks on NYSE from https://finance.yahoo.com/most-active, checks
HTTP status (retries the request if it fails to get the page and terminates if the retry fails), analyzes
the response to extract the data, add the data in mongodb database as new mongodb
documents, and sleeps 3 minutes to limit request frequency. The program only saves the following
5 fields into the database: Symbol, Name, Price (Introday), Change, and Volume. For simplicity,
it only adds new data into the database as new documents, and does not merge it with the existing
data in the database (e.g., calculating average prices, total volumes, etc)
