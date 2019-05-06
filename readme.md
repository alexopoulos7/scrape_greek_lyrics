Scan and extract all lyrics for all greek poems and songs found in this
wonderful url [stixoi.info](http://www.stixoi.info/)
What is nice about this small code snippet is that we parallelize
requests to site which makes scraping process really fast.

On our tests we scrape more than 100K greek poems and songs.

## Requirements
1. Code has been tested thorougly using **Python 3.6**

## How to Install
The only requirement is [Beautiful Soup Library](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) that parses html content.
```python
pip install -r requirements.txt
```

## How to Run
Since its a simple python script the easiest way is to run
```
python scrape.py
```

If you prefer to run scrape process in the background so that you can
start and leave terminal window you can do on a Linux machine:
```
chmod +x scrape.py
nohup python3 -u ./scrape.py &
```