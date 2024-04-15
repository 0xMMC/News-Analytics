{{ config(
    materialized='table',
    partition_by={
        "field": "News_Date",
        "data_type": "date"
    },
    cluster_by=[
        "topic"
    ]
) }}

select
    extract(date from CAST(n.publishedAt as DATETIME)) AS News_Date,
    k.*,
    n.topic,
    n.publishedAt
from
    news_analytics.keywords k
left join
    news_analytics.news n on k.ID = n.ID