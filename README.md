# News Scraper

## Project Title
A Linux-based web scraping tool for extracting the latest news headlines from BBC News.

## Aim of the Project
The primary aim of this project is to develop a web scraping tool that extracts the latest news headlines from BBC News and saves them in a structured format (CSV file). This project serves multiple purposes, including:
- **Data Collection**: Automate the process of gathering news headlines.
- **Data Storage**: Store collected headlines in a CSV format for easy access and analysis.
- **Learning Web Scraping Techniques**: Provide hands-on experience with web scraping using Python.
- **Demonstrating Practical Applications of Python**: Showcase the practical use of Python in real-world scenarios.
- **Creating a Foundation for Further Development**: Lay the groundwork for future enhancements.

## Features
- Scrapes latest news headlines from the BBC News website.
- Saves headlines to a CSV file with a customizable delimiter.
- Command-line interface to read saved headlines by date.

## Technologies Used
- Python 3.x
- Libraries: `requests`, `BeautifulSoup`, `csv`
- Linux Command Line

## Files Included
- `news_scraper.py`: The main script for scraping news headlines.
- `read_headlines.sh`: A shell script for reading saved headlines by date.

## How to Run the Project

### Prerequisites
Make sure you have Python and the required libraries installed:
```bash
pip install requests beautifulsoup4
