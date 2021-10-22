import argparse
import logging

from yaml import parse
logging.basicConfig(level=logging.INFO)

from common import config

logger = logging.getLogger(__name__)

def _news_scraper(news_site_vid):
    host = config()['news_sites'][news_site_vid]['url']

    logging.info(f'Beginning scrape for {host}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    news_sites_choices = list(config() ['news_sites'].keys())
    parser.add_argument('news_site',
                        help ='The news sites that you want to scrape',
                        type=str,
                        choices=news_sites_choices)

    args = parser.parse_args()
    _news_scraper(args.news_site) 
