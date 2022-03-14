import requests
from bs4 import BeautifulSoup


def get_first_news():
    headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36'
    }
    url = 'https://vc.ru/new'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    news = soup.find("div", class_='content-feed')

    if news.find('div', class_='content-title') != None:
        news_title = news.find('div', class_='content-title').text.strip()
    #if news.find('p') != None:
    #    news_desc = news.find('p').text.strip()
    news_url = news.find('a','content-link').get("href")
    news_date = news.find('time').get('title')
    
    news_dict = {
        'news_title': news_title,
        #'news_desc': news_desc,
        'news_url': news_url,
        'news_date': news_date
    }
    return news_dict


def main():
    get_first_news()


if __name__ == "__main__":
    main()