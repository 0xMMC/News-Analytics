{{ config(materialized="table") }}

select
    k.*,
    n.topic,
    n.publishedAt
from
    news_analytics.keywords k
left join
    news_analytics.news n on k.ID = n.ID