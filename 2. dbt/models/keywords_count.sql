{{ config(
    materialized='table',
    partition_by={
      "field": "topic",
      "data_type": "string"
    }
)}}

select
    n.publishedAt,
    n.topic,
    k.Keywords,
    count(*) Keyword_Count
from
    news_analytics.keywords k
left join
    news_analytics.news n on k.ID = n.ID
group by
    1,2,3