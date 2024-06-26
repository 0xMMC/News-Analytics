from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path

import pandas as pd

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    dfs = pd.concat(df)

    dfs['publishedAt'] = pd.to_datetime(dfs['publishedAt'])

    mindate = dfs['publishedAt'].min().date()
    maxdate = dfs['publishedAt'].max().date()


    bucket_name = 'news-analytics-419010-terra-bucket'
    object_key = f'{mindate} to {maxdate} news.parquet'

    GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
        dfs,
        bucket_name,
        object_key,
    )
