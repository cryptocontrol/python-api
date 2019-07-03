import requests

class CryptoControlAPI:
    def __init__(self, apiKey, proxyServer = None):
        self.apiKey = apiKey
        self.proxyServer = proxyServer
        self.sentiment = False


    def _fetch(self, url):
        host = self.proxyServer if self.proxyServer else 'https://cryptocontrol.io/api/v1/public'
        sentiment = "%ssentiment=%s" % (
            "&" if url.find("?") else "?",
            "true" if self.sentiment == True else "false"
        )

        finalURL = host + url + sentiment

        headers = {
            'x-api-key': self.apiKey,
            'user-agent': 'CryptoControl Python Client v2.3.1'
        }

        response = requests.get(url=finalURL, headers=headers)

        if (response.status_code is 401): raise Exception("Invalid API Key")
        if (response.status_code is 405): raise Exception("You are not a premium user. Visit https://cryptocontrol.io/about/premium for more info")
        if (response.status_code is not 200): raise Exception("Bad response from the CryptoControl API")

        return response.json()


    def enableSentiment(self):
        """
            Enable the sentiment datapoints
        """
        self.sentiment = True


    def getTopNews(self, language = "en", page = 0):
        """
            Get the top news from the CryptoControl API. Returns a JSON array of articles
        """
        return self._fetch("/news?language=%s&page=%d" % (language, page))


    def getLatestNews(self, language = "en", page = 0):
        """
            Get the latest news from the CryptoControl API. Returns a JSON array of articles
        """
        return self._fetch("/news?latest=true&language=%s&page=%d" % (language,page))


    def getTopNewsByCategory(self, language = "en", page = 0):
        """
            Get news articles grouped by category from the CryptoControl News API. Returns a JSON
            object where each key reperesents a category and contains an array of articles.
        """
        return self._fetch("/news/category?language=%s&page=%d" % (language,page))


    def getTopNewsByCoin(self, coin, language= "en", page = 0):
        """
            Get the top news articles for a specific coin from the CryptoControl API.
            Returns a JSON array of articles
        """
        return self._fetch("/news/coin/%s?langage=%s&page=%d" % (coin, language, page))


    def getLatestNewsByCoin(self, coin, language = "en", page = 0):
        """
            Get the latest news articles for a specific coin from the CryptoControl News API.
            Returns a JSON array of articles
        """
        return self._fetch("/news/coin/%s?latest=true&language=%s&page=%d" % (coin, language, page))


    def getTopNewsByCoinCategory(self, coin, language = "en", page = 0):
        """
            Get news articles grouped by category for a specific coin from the CryptoControl News API. Returns a JSON
            object where each key reperesents a category and contains an array of articles.
        """
        return self._fetch("/news/coin/%s?language=%s&page=%d" % (coin, language, page))


    def getTopRedditPostsByCoin(self, coin, language="en", page = 0):
        """
            Get top reddit posts for a specific coin.
        """
        return self._fetch("/reddit/coin/%s?language=%s&page=%d" % (coin, language, page))


    def getLatestRedditPostsByCoin(self, coin, language="en", page = 0):
        """
            Get latest reddit posts for a specific coin.
        """
        return self._fetch("/news/coin/%s?latest=true&language=%s&page=%d" % (coin, language, page))


    def getTopTweetsByCoin(self, coin, language="en", page = 0):
        """
            Get top tweets for a specific coin.
        """
        return self._fetch("/tweets/coin/%s?language=%s&page=%d" % (coin, language, page))


    def getLatestTweetsByCoin(self, coin, language="en", page = 0):
        """
            Get latest tweets for a specific coin.
        """
        return self._fetch("/tweets/coin/%s?latest=true&language=%s&page=%d" % (coin, language, page))


    def getTopFeedByCoin(self, coin, language="en", page = 0):
        """
            Get top feed (combined reddit/articles/tweets) for a given coin
        """
        return self._fetch("/feed/coin/%s?language=%s&page=%d" % (coin, language, page))


    def getLatestFeedByCoin(self, coin, language="en", page = 0):
        """
            Get latest feed (combined reddit/articles/tweets) for a given coin
        """
        return self._fetch("/feed/coin/%s?latest=true&language=%s&page=%d" % (coin, language, page))


    def getTopItemsByCoin(self, coin, language="en", page = 0):
        """
            Get top reddit/articles/tweets (seperated) for a given coin
        """
        return self._fetch("/feed/coin/%s?language=%s&page=%d" % (coin, language, page))


    def getLatestItemsByCoin(self, coin, language="en", page = 0):
        """
            Get latest reddit/articles/tweets (seperated) for a given coin
        """
        return self._fetch("/feed/coin/%s?latest=true&language=%s&page=%d" % (coin, language, page))


    def getCoinDetails(self, coin, language="en", page = 0):
        """
            Get all details about a single coin. (Wallets, links, blockexplorers, subreddits etc)
        """
        return self._fetch("/details/coin/%s?language=%s&page=%d" % (coin, language, page))
