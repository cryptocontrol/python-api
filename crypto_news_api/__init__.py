import requests

class CryptoControlAPI:
    def __init__(self, apiKey):
        self.apiKey = apiKey

    def _fetch(self, url):
        URL = "https://cryptocontrol.io/api/v1/public%s" % url
        HEADERS = {
            'x-api-key': self.apiKey,
            'user-agent': 'CryptoControl Python Client'
        }

        response = requests.get(url=URL, headers=HEADERS)

        print(response.status_code)
        print(response.status_code is 200)
        print(type(response.status_code))
        print(URL)

        if (response.status_code is 401): raise Exception("Invalid API Key")

        if (response.status_code is not 200):
            raise Exception("Bad response from the CryptoControl API")

        return response.json()


    def getTopNews(self):
        """
            Get the top news from the CryptoControl API. Returns a JSON array of articles
        """
        return self._fetch("/news")


    def getLatestNews(self):
        """
            Get the latest news from the CryptoControl API. Returns a JSON array of articles
        """
        return self._fetch("/news?latest=true")


    def getTopNewsByCategory(self):
        """
            Get news articles grouped by category from the CryptoControl News API. Returns a JSON
            object where each key reperesents a category and contains an array of articles.
        """
        return self._fetch("/news/category")


    def getTopNewsByCoin(self, coin):
        """
            Get the top news articles for a specific coin from the CryptoControl API.
            Returns a JSON array of articles
        """
        return self._fetch("/news/coin/%s" % coin)


    def getLatestNewsByCoin(self, coin):
        """
            Get the latest news articles for a specific coin from the CryptoControl News API.
            Returns a JSON array of articles
        """
        return self._fetch("/news/coin/%s?latest=true" % coin)


    def getTopNewsByCoinCategory(self, coin):
        """
            Get news articles grouped by category for a specific coin from the CryptoControl News API. Returns a JSON
            object where each key reperesents a category and contains an array of articles.
        """
        return self._fetch("/news/coin/%s/category" % coin)
