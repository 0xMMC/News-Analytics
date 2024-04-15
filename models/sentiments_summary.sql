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
    s.*,
    (s.Title_Sentiment + s.Summary_Sentiment)/2 as Average_Sentiment,
    n.topic
from
    news_analytics.sentiments s
left join
    news_analytics.news n on s.ID = n.ID