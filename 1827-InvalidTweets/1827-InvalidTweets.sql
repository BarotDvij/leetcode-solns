-- Last updated: 10/15/2025, 3:02:58 AM
-- Write your PostgreSQL query statement below
Select tweet_id
From Tweets
Where
    Length(content) > 15