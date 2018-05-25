import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = 'crypto_news_api',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    version = '1.0.1',
    description = 'Client to get a crypto newsfeed in your app from the CryptoControl API',
    author = 'Steven Enamakel',
    author_email = 'enamakel@cryptocontrol.io',
    url = 'https://github.com/cryptocontrol/python-api',
    download_url = 'https://github.com/cryptocontrol/python-api/archive/1.0.1.tar.gz',
    keywords = ["crypto", "news", "cryptocurrency", "blockchain", "api"],
    classifiers = [],
)