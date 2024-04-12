if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from mage_ai.data_preparation.shared.secrets import get_secret_value

import requests
import pandas as pd
from datetime import datetime, timedelta
import uuid

from rake_nltk import Rake

import nltk
nltk.download('stopwords')
nltk.download('punkt')

import spacy
nlp = spacy.load("en_core_web_sm")

TODAY_START = str(datetime.today().date()-timedelta(days=1))+"T00:00:00"
TODAY_NOW = str(datetime.today().date()) + "T" + str(datetime.today().time())[:8]
SOURCES = 'abc-news,al-jazeera-english,associated-press,axios,bbc-news,bloomberg,cnn,google-news,national-geographic,new-scientist,reddit-r-all,reuters,techcrunch,techradar,the-huffington-post,the-verge,the-wall-street-journal,the-washington-post,time,wired'

NEWS_API_KEY = get_secret_value('NEWS_API_KEY')

def get_news(topic:str, date_from:str, date_to:str) -> tuple[pd.DataFrame]:

    url = ('https://newsapi.org/v2/everything?'
        f'from={date_from}&'
        f'to={date_to}&'
        'sortBy=popularity&'
        f'q={topic}&'
        f'sources={SOURCES}&'
        f'apiKey={NEWS_API_KEY}')


    response = requests.get(url)
    response.raise_for_status()
    r = response.json()

    df = pd.DataFrame(r['articles'])
    df['source'] = df['source'].apply(lambda x:x['name'])
    df['ID'] = [str(uuid.uuid4()) for x in df['publishedAt']]
    df['topic'] = topic

    return df

@data_loader
def load_data(*args, **kwargs):
    TOPICS = ['stock-market', 'climate-change', 'elections', 
          'longevity', 'public-health','technology', 
          'artificial-intelligence','natural-disaster', 'international-politics',
          'social-media','inflation','education',
          'entertainment','science','human-rights']
    TEST_TOPICS = ['stock-market', 'climate-change']

    return [[{topic:get_news(topic=topic, date_from=TODAY_START, date_to=TODAY_NOW)} for topic in TOPICS]]

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'