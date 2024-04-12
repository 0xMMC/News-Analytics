if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")

@transformer
def transform(data, *args, **kwargs):
    dfs = []
    for val in data.values():
        dfs.append(pd.DataFrame(val))
    data = pd.concat(dfs)
    
    title_entities = {}
    summary_entities = {}

    for id, title, description in zip(data['ID'], data['title'], data['description']):
        try:
            title_ents = nlp(title)
            title_entities[id] = [ent.text for ent in title_ents.ents]
        except:
            title_entities[id] = ''

        try:
            summary_ents = nlp(description)
            summary_entities[id] = [ent.text for ent in summary_ents.ents]
        except:
            summary_entities[id] = ''


    df_title_entities = pd.DataFrame(title_entities.values(), index=title_entities.keys()).reset_index().melt(id_vars='index')
    df_title_entities.drop(columns='variable', inplace=True)
    df_title_entities.dropna(inplace=True)
    df_title_entities['value'] = df_title_entities['value'].str.replace('’','').str.strip()
    df_title_entities.columns = ['ID', 'Entities']

    df_summary_entities = pd.DataFrame(summary_entities.values(), index=summary_entities.keys()).reset_index().melt(id_vars='index')
    df_summary_entities.drop(columns='variable', inplace=True)
    df_summary_entities.dropna(inplace=True)
    df_summary_entities['value'] = df_summary_entities['value'].str.replace('’','').str.strip()
    df_summary_entities.columns = ['ID', 'Entities']

    entities = pd.concat([df_title_entities, df_summary_entities])
    entities.drop_duplicates(inplace=True)
    entities.sort_values(by='ID', inplace=True)
    
    return entities


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
