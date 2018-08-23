from crypto_news_api import CryptoControlAPI
import sys

api = CryptoControlAPI(sys.argv[1])

api.enableSentiment()

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
