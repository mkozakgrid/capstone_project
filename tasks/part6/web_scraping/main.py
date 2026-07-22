from urllib.request import urlopen

def main():
    url = "https://finance.yahoo.com/most-active"
    page = urlopen(url)
    html = page.read().decode('utf-8')

if __name__ == "__main__":
    main()