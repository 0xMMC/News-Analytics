{{ config(
    materialized='table',
    partition_by={
      "field": "topic",
      "data_type": "string"
    }
)}}

select
    e.*,
    n.topic,
    n.publishedAt
from
    news_analytics.entities e
left join
    news_analytics.news n on e.ID = n.ID