{{ config(
    materialized='table',
    partition_by={
        "field": "publishedAt",
        "data_type": "date"
    },
    cluster_by=[
        "topic"
    ]
) }}

select
    extract(date from CAST(n.publishedAt as DATETIME)) AS publishedAt,
    e.*,
    n.topic
from
    news_analytics.entities e
left join
    news_analytics.news n on e.ID = n.ID