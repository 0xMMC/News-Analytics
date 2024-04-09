import requests
import pandas as pd
from datetime import datetime, timedelta

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from rake_nltk import Rake

import nltk
nltk.download('stopwords')
nltk.download('punkt')

import spacy
nlp = spacy.load("en_core_web_sm")


# TODO Optimise to 100 requests per day

TODAY = str(datetime.today().date())
AGO_30 = str(datetime.today().date()-timedelta(days=30))

API_KEY = '11fe08baf94b4d759343973d4e2000df'

SOURCES = 'abc-news,al-jazeera-english,associated-press,axios,bbc-news,bloomberg,cnn,google-news,national-geographic,new-scientist,reddit-r-all,reuters,techcrunch,techradar,the-huffington-post,the-verge,the-wall-street-journal,the-washington-post,time,wired'
TOPICS = ['stock-market', 'climate-change', 'elections', 
          'longevity', 'public-health','technology', 
          'artificial-intelligence','natural-disaster', 'international-politics',
          'social-media','inflation','education',
          'entertainment','science','human-rights']

url = ('https://newsapi.org/v2/everything?'
       f'from={AGO_30}&'
       f'to={TODAY}&'
       'sortBy=popularity&'
       'q=international-politics&'
       f'sources={SOURCES}&'
       'apiKey=11fe08baf94b4d759343973d4e2000df')


response = requests.get(url)
r = response.json()

df = pd.DataFrame(r['articles'])
df['source'] = df['source'].apply(lambda x:x['name'])
# TODO - generate unique hash for each
df['ID'] = (df['title']+df['publishedAt']).apply(hash)

title_sentiments = {}
summary_sentiments = {}

# TODO - clean dashes and ' ’' and trim
title_keywords = {}
summary_keywords = {}

# TODO clean 's s
title_entities = {}
summary_entities = {}

kw_extractor = Rake(max_length=2)
def get_significant_keywords(text:str) -> list:
    global kw_extractor
    kw_extractor.extract_keywords_from_text(text)
    ranked_keywords = kw_extractor.get_ranked_phrases_with_scores()
    final_keywords = []
    for kw in ranked_keywords:
        try:
            if kw[0] >= 4:
                final_keywords.append(kw[1])
        except:
            pass
    return final_keywords

analyzer = SentimentIntensityAnalyzer()

for id, title, description in zip(df['ID'], df['title'], df['description']):
    
    # Get title and summary sentiment
    title_sentiment = analyzer.polarity_scores(title)
    summary_sentiment = analyzer.polarity_scores(description)

    title_sentiments[id] = title_sentiment['compound']
    summary_sentiments[id] = summary_sentiment['compound']

    # Extract keywords from title and description
    title_keywords[id] = get_significant_keywords(title)
    summary_keywords[id] = get_significant_keywords(description)

    # Extract entitites from title and description
    title_ents = nlp(title)
    summary_ents = nlp(description)
    title_entities[id] = [ent.text for ent in title_ents.ents]
    summary_entities[id] = [ent.text for ent in summary_ents.ents]



"""
The SentimentIntensityAnalyzer class from the VADER library provides a 
polarity_scores method that analyzes the input text and returns a dictionary with
 four key-value pairs:
"neg": The negative sentiment score, ranging from 0 to 1.
"neu": The neutral sentiment score, ranging from 0 to 1.
"pos": The positive sentiment score, ranging from 0 to 1.
"compound": The compound score, which is a metric that combines 
the previous three scores into a single metric that ranges 
from -1 (most negative) to 1 (most positive).
"""

"""
To extract the top 3 keywords from each news article, you can use a 
keyword extraction library like rake-nltk (Rapid Automatic Keyword Extraction).
"""

"""
To perform Named Entity Recognition (NER) on the news titles and summaries, 
we can use the spaCy library, which is a powerful natural language processing (NLP) 
library for Python.

"""
