from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path
import pandas as pd

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(df: DataFrame, **kwargs) -> None:
    
    table_id = 'news-analytics-419010.news_analytics.news'
    
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    dfs = pd.concat(df)

    BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
        dfs,
        table_id,
        if_exists='append',
    )
