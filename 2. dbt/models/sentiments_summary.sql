{{ config(
    materialized='table',
    partition_by={
      "field": "topic",
      "data_type": "string"
    }
)}}

select
    s.*,
    (s.Title_Sentiment + s.Summary_Sentiment)/2 as Average_Sentiment,
    n.topic,
    n.publishedAt
from
    news_analytics.sentiments s
left join
    news_analytics.news n on s.ID = n.ID