{{ config(materialized="table") }}

select
    n.publishedAt,
    n.topic,
    e.Entities,
    count(*) Entities_Count
from
    news_analytics.entities e
left join
    news_analytics.news n on e.ID = n.ID
group by
    1,2,3