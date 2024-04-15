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
    n.topic,
    k.Keywords,
    count(*) Keyword_Count
from
    news_analytics.keywords k
left join
    news_analytics.news n on k.ID = n.ID
group by
    1,2,3