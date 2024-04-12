{{ config(materialized="table") }}

select
    e.*,
    n.topic,
    n.publishedAt
from
    news_analytics.entities e
left join
    news_analytics.news n on e.ID = n.ID