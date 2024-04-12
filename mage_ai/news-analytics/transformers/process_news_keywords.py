if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
from rake_nltk import Rake

import nltk
nltk.download('stopwords')
nltk.download('punkt')

kw_extractor = Rake(max_length=2)
def get_significant_keywords(text:str) -> list:
    
    final_keywords = []

    try:
        kw_extractor.extract_keywords_from_text(text)
        ranked_keywords = kw_extractor.get_ranked_phrases_with_scores()
    
        for kw in ranked_keywords:
            try:
                if kw[0] >= 4:
                    final_keywords.append(kw[1])
            except:
                pass
    except:
        pass
    return final_keywords

@transformer
def transform(data, *args, **kwargs):
    dfs = []
    for val in data.values():
        dfs.append(pd.DataFrame(val))
    data = pd.concat(dfs)
    
    title_keywords = {}
    summary_keywords = {}

    for id, title, description in zip(data['ID'], data['title'], data['description']):
        title_keywords[id] = get_significant_keywords(title)
        summary_keywords[id] = get_significant_keywords(description)

    df_title_keywords = pd.DataFrame(title_keywords.values(), index=title_keywords.keys()).reset_index().melt(id_vars='index')
    df_title_keywords.drop(columns='variable', inplace=True)
    df_title_keywords.dropna(inplace=True)
    df_title_keywords['value'] = df_title_keywords['value'].str.replace('’','').str.strip()
    df_title_keywords.columns = ['ID', 'Keywords']

    df_summary_keywords = pd.DataFrame(summary_keywords.values(), index=summary_keywords.keys()).reset_index().melt(id_vars='index')
    df_summary_keywords.drop(columns='variable', inplace=True)
    df_summary_keywords.dropna(inplace=True)
    df_summary_keywords['value'] = df_summary_keywords['value'].str.replace('’','').str.strip()
    df_summary_keywords.columns = ['ID', 'Keywords']

    df_keywords = pd.concat([df_title_keywords, df_summary_keywords])
    df_keywords.drop_duplicates(inplace=True)
    df_keywords.sort_values(by='ID', inplace=True)

    return df_keywords


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
