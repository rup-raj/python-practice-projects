from newsapi import NewsApiClient
import requests

# Init
newsapi = NewsApiClient(api_key='2a929e3c2ce14a20b347d08a0e5bfb05')

def get_top_headline():
    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                              # sources='bbc-news,the-verge',
                                              #category='business',
                                              country='us',
                                              language='en')

    return top_headlines


def get_eveything():
    # /v2/everything
    all_articles = newsapi.get_everything(q='Tata',
                                          sources='bbc-news,the-verge,time',
                                          domains='bbc.co.uk,techcrunch.com',
                                          from_param='2024-08-10',
                                          to='2024-09-01',
                                          language='en',
                                          sort_by='relevancy',
                                          page=2)
    return all_articles


def get_source():
    # /v2/top-headlines/sources
    sources = newsapi.get_sources()
    return sources


def get_news():
    print(get_eveything())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_news()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
