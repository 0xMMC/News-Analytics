if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

@transformer
def transform(data, *args, **kwargs):
    dfs = []
    for val in data.values():
        dfs.append(pd.DataFrame(val))
    data = pd.concat(dfs)
    
    title_sentiments = {}
    summary_sentiments = {}

    for id, title, description in zip(data['ID'], data['title'], data['description']):
        
        # Get title and summary sentiment
        try:
            title_sentiment = analyzer.polarity_scores(title)
            title_sentiments[id] = title_sentiment['compound']
        except:
            title_sentiments[id] = 0
        
        try:
            summary_sentiment = analyzer.polarity_scores(description)
            summary_sentiments[id] = summary_sentiment['compound']
        except:
            summary_sentiments[id] = 0

    df_title_sentiments = pd.DataFrame(title_sentiments.items(), columns=['ID','Title Sentiment'])
    df_summary_sentiments = pd.DataFrame(summary_sentiments.items(), columns=['ID','Summary Sentiment'])
    df_sentiments = pd.merge(df_title_sentiments, df_summary_sentiments, on='ID')

    return df_sentiments


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
