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
    s.*,
    (s.Title_Sentiment + s.Summary_Sentiment)/2 as Average_Sentiment,
    n.topic,
    n.publishedAt
from
    news_analytics.sentiments s
left join
    news_analytics.news n on s.ID = n.ID