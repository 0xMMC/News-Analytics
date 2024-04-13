{{ config(
    materialized='table',
    partition_by={
      "field": "topic",
      "data_type": "string"
    }
)}}

select
    k.*,
    n.topic,
    n.publishedAt
from
    news_analytics.keywords k
left join
    news_analytics.news n on k.ID = n.ID