from crypto_news_api import CryptoControlAPI
import sys

c = CryptoControlAPI(sys.argv[1])

print(c.getTopNewsByCoin("bitcoin"))
