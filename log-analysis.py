#!/usr/bin/env python

import psycopg2

database_name = "news"

# Store queries into variables


# Store results



# Get query results from databse and return them



# Print results method


# Store query results


# Print query results

# create views because third question is difficult

question 1 - What are the most popular three articles of all time?
databases needed are articles and log
select article title where log method GET is highest
print top 3 in desc (based on GET)

question_1 = SELECT title from articles where 
JOIN log
GROUP BY title ORDER BY views DESC LIMIT 3

question 2 -  Who are the most popular article authors of all time?
need all databases
join articles and authors
select authors where log method GET is highest
print top 3 desc (based on GET)

question 3 - On which days did more than 1% of requests lead to errors?
On which days did more than 1% of requests lead to errors?
errors is log status 400 +
