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
    e.*,
    n.topic,
    n.publishedAt
from
    news_analytics.entities e
left join
    news_analytics.news n on e.ID = n.ID