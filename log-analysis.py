#!/usr/bin/env python

# need psycopg2 to handle postgresql
import psycopg2

News_Database = "news"

# created question variables. These will be printed later.
question_1 = "What are the most popular three articles of all time?"
question_2 = "Who are the most popular article authors of all time?"
question_3 = "On which days did more than 1% of requests lead to errors?"

# created answer variables, which are PostgreSQL statements
answer_1 = """SELECT title, COUNT(*) as article_views FROM articles \n
              JOIN log ON articles.slug = SUBSTRING(log.path, 10)\n
              GROUP BY title ORDER BY article_views DESC LIMIT 3;"""

answer_2 = """SELECT authors.name, COUNT(*) as author_rank \n
              FROM articles JOIN authors ON articles.author = authors.id \n
              JOIN log ON articles.slug = substring(log.path, 10)\n
              WHERE log.status = '200 OK' GROUP BY authors.name \n
              ORDER BY author_rank DESC;"""

answer_3 = "SELECT * FROM error_view WHERE \"Error_Percentage\" > 1;"


# returns query result
def get_query_Results(query):
    db = psycopg2.connect(database=News_Database)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# print_results will show the answer run, formatted, and line down
def print_results(answers):
    for i in range(len(answers)):
        title = answers[i][0]
        res = answers[i][1]
        print("\t" + "%s - %d" % (title, res))
    print("\n")


# Run get_query_Results and store into result variables
result_1 = get_query_Results(answer_1)
result_2 = get_query_Results(answer_2)
result_3 = get_query_Results(answer_3)

# Print all Questions and Answers.
print(question_1)
print_results(result_1)
print(question_2)
print_results(result_2)
print(question_3)
print_results(result_3)
