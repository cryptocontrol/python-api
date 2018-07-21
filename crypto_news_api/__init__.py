import requests

class CryptoControlAPI:
    def __init__(self, apiKey, proxyServer = None):
        self.apiKey = apiKey
        self.proxyServer = proxyServer


    def _fetch(self, url):
        HOST = self.proxyServer if self.proxyServer else 'https://cryptocontrol.io/api/v1/public'
        URL = HOST + url
        HEADERS = {
            'x-api-key': self.apiKey,
            'user-agent': 'CryptoControl Python Client'
        }

        response = requests.get(url=URL, headers=HEADERS)

        if (response.status_code is 401): raise Exception("Invalid API Key")

        if (response.status_code is not 200):
            raise Exception("Bad response from the CryptoControl API")

        return response.json()


    def getTopNews(self, language = "en"):
        """
            Get the top news from the CryptoControl API. Returns a JSON array of articles
        """
        return self._fetch("/news?language=%s" % language)


    def getLatestNews(self, language = "en"):
        """
            Get the latest news from the CryptoControl API. Returns a JSON array of articles
        """
        return self._fetch("/news?latest=true&language=%s" % language)


    def getTopNewsByCategory(self, language = "en"):
        """
            Get news articles grouped by category from the CryptoControl News API. Returns a JSON
            object where each key reperesents a category and contains an array of articles.
        """
        return self._fetch("/news/category?language=%s" % language)


    def getTopNewsByCoin(self, coin, language= "en"):
        """
            Get the top news articles for a specific coin from the CryptoControl API.
            Returns a JSON array of articles
        """
        return self._fetch("/news/coin/%s?langage=%s" % (coin, language))


    def getLatestNewsByCoin(self, coin, language = "en"):
        """
            Get the latest news articles for a specific coin from the CryptoControl News API.
            Returns a JSON array of articles
        """
        return self._fetch("/news/coin/%s?latest=true&language=%s" % (coin, language))


    def getTopNewsByCoinCategory(self, coin, language = "en"):
        """
            Get news articles grouped by category for a specific coin from the CryptoControl News API. Returns a JSON
            object where each key reperesents a category and contains an array of articles.
        """
        return self._fetch("/news/coin/%s?language=%s" % (coin, language))


    def getTopRedditPostsByCoin(self, coin, language="en"):
        """
            Get top reddit posts for a specific coin.
        """
        return self._fetch("/reddit/coin/%s?language=%s" % (coin, language))


    def getLatestRedditPostsByCoin(self, coin, language="en"):
        """
            Get latest reddit posts for a specific coin.
        """
        return self._fetch("/news/coin/%s?latest=true&language=%s" % (coin, language))


    def getTopTweetsByCoin(self, coin, language="en"):
        """
            Get top tweets for a specific coin.
        """
        return self._fetch("/tweets/coin/%s?language=%s" % (coin, language))


    def getLatestTweetsByCoin(self, coin, language="en"):
        """
            Get latest tweets for a specific coin.
        """
        return self._fetch("/tweets/coin/%s?latest=true&language=%s" % (coin, language))


    def getTopFeedByCoin(self, coin, language="en"):
        """
            Get top feed (combined reddit/articles/tweets) for a given coin
        """
        return self._fetch("/feed/coin/%s?language=%s" % (coin, language))


    def getLatestFeedByCoin(self, coin, language="en"):
        """
            Get latest feed (combined reddit/articles/tweets) for a given coin
        """
        return self._fetch("/feed/coin/%s?latest=true&language=%s" % (coin, language))


    def getTopItemsByCoin(self, coin, language="en"):
        """
            Get top reddit/articles/tweets (seperated) for a given coin
        """
        return self._fetch("/feed/coin/%s?language=%s" % (coin, language))


    def getLatestItemsByCoin(self, coin, language="en"):
        """
            Get latest reddit/articles/tweets (seperated) for a given coin
        """
        return self._fetch("/feed/coin/%s?latest=true&language=%s" % (coin, language))


    def getCoinDetails(self, coin, language="en"):
        """
            Get all details about a single coin. (Wallets, links, blockexplorers, subreddits etc)
        """
        return self._fetch("/details/coin/%s?language=%s" % (coin, language))
