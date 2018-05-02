# Log Analysis

This project is my answer to the thrid deliverable of the Udacity Full-Stack Nanodegree. 

## Description: 
This python file will answer three questions from PostgreSQL [databse](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) provided by Udacity. 
- question 1: "What are the most popular three articles of all time?"
- question 2: "Who are the most popular article authors of all time?"
- question 3: "On which days did more than 1% of requests lead to errors?"


## Contents: 
1. log-analysis.py - Python file to run the queries. 
2. results.txt - A text file that contains the result with the current database used: news. 
### I created a View to answer the third question
```
CREATE VIEW error_view as SELECT date(time),round(100.0*sum(case log.status when '200 OK' 
then 0 else 1 end)/count(log.status),2) as "Error_Percentage" from log group by date(time) 
ORDER BY "Error_Percentage" DESC;
```
