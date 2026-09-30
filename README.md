# Web Scraping Project

## Project Overview
A simple Python web scraping project that collects book data from a website and saves it into a CSV file for further analysis.

## What broke, or took longer than expected?
The price value was returned as a string instead of a float, so I had to clean the value first before converting it to a number.

## If the site started blocking you after 50 requests, what would you change?
I would add a small delay between requests and reduce the number of requests sent at once. I could also scrape the data in 
