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
    e.Entities,
    count(*) AS Entities_Count
from
    news_analytics.entities e
left join
    news_analytics.news n on e.ID = n.ID
group by
    1,2,3