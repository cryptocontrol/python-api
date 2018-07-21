CryptoControl - Python Crypto News API
=========================

Official Python client for the [CryptoControl.io](https://cryptocontrol.io) API. The CryptoControl python client lets developers access rich formatted articles from cryptonews sources from all around the world.

## Installation
```sh
pip install crypto-news-api
```

## Usage
First make sure that you've recieved an API key by visiting [https://cryptocontrol.io/apis](https://cryptocontrol.io/apis). With the API key you can write the following code.


```python
from crypto_news_api import CryptoControlAPI

# Connect to the CryptoControl API
api = CryptoControlAPI("API_KEY_HERE")

# Connect to a self-hosted proxy server (to improve performance) that points to cryptocontrol.io
proxyApi = CryptoControlAPI("API_KEY_HERE", "http://cryptocontrol_proxy/api/v1/public")

# Get top news
print(api.getTopNews())

# get latest russian news
print(api.getLatestNews("ru"))

# get top bitcoin news
print(api.getTopNewsByCoin("bitcoin"))

# get top EOS tweets
print(api.getTopTweetsByCoin("eos"))

# get top Ripple reddit posts
print(api.getLatestRedditPostsByCoin("ripple"))

# get reddit/tweets/articles in a single combined feed for NEO
print(api.getTopFeedByCoin("neo"))

# get latest reddit/tweets/articles (seperated) for Litecoin
print(api.getLatestItemsByCoin("litecoin"))

# get details (subreddits, twitter handles, description, links) for ethereum
print(api.getCoinDetails("ethereum"))

```

## Available Functions

- **getTopNews(lang?: enum)** Get the top news articles.
- **getLatestNews(lang?: enum)** Get the latest news articles.
- **getTopNewsByCategory(lang?: enum)** Get news articles grouped by category.
- **getTopNewsByCoin(coin: String, lang?: enum)** Get the top news articles for a specific coin from the CryptoControl API.
- **getLatestNewsByCoin(coin: String, lang?: enum)** Get the latest news articles for a specific coin.
- **getTopNewsByCoinCategory(coin: String, lang?: enum)** Get news articles grouped by category for a specific coin.
- **getTopRedditPostsByCoin(coin: String, lang?: enum)** Get top reddit posts for a particular coin
- **getLatestRedditPostsByCoin(coin: String, lang?: enum)** Get latest reddit posts for a particular coin
- **getTopTweetsByCoin(coin: String, lang?: enum)** Get top tweets for a particular coin
- **getLatestTweetsByCoin(coin: String, lang?: enum)** Get latest tweets for a particular coin
- **getTopFeedByCoin(coin: String, lang?: enum)** Get a combined feed (reddit/tweets/articles) for a particular coin (sorted by time)
- **getLatestFeedByCoin(coin: String, lang?: enum)** Get a combined feed (reddit/tweets/articles) for a particular coin (sorted by relevance)
- **getTopItemsByCoin(coin: String, lang?: enum)** Get reddit/tweets/articles (seperated) for a particular coin (sorted by time)
- **getLatestItemsByCoin(coin: String, lang?: enum)** Get reddit/tweets/articles (seperated) for a particular coin (sorted by relevance)
- **getCoinDetails(coin: String)** Get all details about a particular coin (links, description, subreddits, twitter etc..)

`lang` allows developers to choose which language they'd like to get the feed. Currently CryptoControl supports English (`en`) and Russian (`ru`) article feeds.

The coin slugs are the coin id's used from the CoinMarketCap api. You can see the full list of coins here: [https://api.coinmarketcap.com/v1/ticker/?limit=2000](https://api.coinmarketcap.com/v1/ticker/?limit=2000)

## Sample response from the server

```javascript
[{
    "hotness": 70862.60323026273,
    "activityHotness": 4.601980262729618,
    "primaryCategory": "General",
    "words": 1444,
    "similarArticles": [
        {
            "_id": "5b363b525b113200191a1d5f",
            "publishedAt": "2018-06-29T13:42:44.000Z",
            "title": "Op-Ed: Challenge of Mining Centralization Unveils Bitcoin’s Elegant Design",
            "url": "https://cryptocontrol.io/r/api/article/5b363b525b113200191a1d5f?ref=5ac11440ec0af7be35528459",
            "source": {
                "_id": "59d8c361ef8bf95cc2bfb66f",
                "name": "Bitcoin Magazine",
                "url": "https://bitcoinmagazine.com/"
            },
            "sourceDomain": "bitcoinmagazine.com",
            "thumbnail": null
        },
        {
            "_id": "5b3865405c5681000f2f7407",
            "publishedAt": "2018-06-30T14:58:00.000Z",
            "title": "Arbitration on a Governed Blockchain: EOS’ Crisis of Dispute Resolution",
            "url": "https://cryptocontrol.io/r/api/article/5b3865405c5681000f2f7407?ref=5ac11440ec0af7be35528459",
            "source": {
                "_id": "59d70be3ef8bf95cc2aa2b4f",
                "name": "CoinTelegraph",
                "url": "https://cointelegraph.com/"
            },
            "sourceDomain": "cointelegraph.com",
            "thumbnail": null
        }
    ],
    "coins": [
        {
            "_id": "59cb59f9b0836b0a63aebc7c",
            "name": "Ethereum",
            "tradingSymbol": "eth",
            "slug": "ethereum"
        },
        {
            "_id": "59d21e9b83a0523906a45dc5",
            "name": "EOS",
            "slug": "eos",
            "tradingSymbol": "eos"
        }
    ],
    "_id": "5b3a2e1b104844000fd64e28",
    "description": "The EOS governance disaster offers a strong reminder of how entrenched human mistrust can be difficult to overcome.",
    "publishedAt": "2018-07-02T12:00:27.000Z",
    "title": "It's Too Soon for On-Chain Governance - CoinDesk",
    "url": "https://cryptocontrol.io/r/api/article/5b3a2e1b104844000fd64e28?ref=5ac11440ec0af7be35528459",
    "source": {
        "_id": "59ce11393a44cf289a9a71f5",
        "name": "CoinDesk",
        "url": "http://coindesk.com"
    },
    "thumbnail": "https://cryptocontrol.io/r/thumbnail/5b3a2e1b104844000fd64e28?ref=5ac11440ec0af7be35528459",
    "sourceName": "CoinDesk",
    "sourceUrl": "http://coindesk.com",
    "sourceDomain": "coindesk.com",
    "originalImageUrl": "https://media.coindesk.com/uploads/2018/06/shutterstock_153840266-e1530230263310.jpg"
}]
```