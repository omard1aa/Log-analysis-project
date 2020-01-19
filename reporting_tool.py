#!/usr/bin/env python3

import psycopg2

DBNAME = 'news'


def getQuery(sql_query):
    connection = psycopg2.connect(database=DBNAME, user='vagrant')
    cursor = connection.cursor()
    cursor.execute(sql_query)
    results = cursor.fetchall()
    connection.close()
    return results


def manipulateQueryResult(query_result):
    query_result_output = ""
    for line in query_result:
        query_result_output += '\"' + str(line[0]) + "\""
        query_result_output += ' -- '
        query_result_output += str(line[1])
        query_result_output += ' views.\n'
    return query_result_output


def manipulateQuery3_Result(query_result):
    query_result_output = ""
    for line in query_result:
        query_result_output += '\"' + str(line[0]) + "\""
        query_result_output += ' -- '
        query_result_output += str(line[1])
        query_result_output += '% errors.\n'
    return query_result_output


sql_query_1 = ('''SELECT title, COUNT(*) as views
             FROM articles
             JOIN log ON log.path = CONCAT('/article/', articles.slug)
             GROUP BY title ORDER BY views DESC LIMIT 3;''')

sql_query_2 = ('''SELECT authors.name , COUNT(*) as views
            FROM authors JOIN articles ON articles.author = authors.id
            JOIN log ON log.path = CONCAT('/article/', articles.slug)
            GROUP BY authors.name ORDER BY views DESC;''')

sql_query_3 = ('''SELECT * from (SELECT date(time), ROUND(100.0 * SUM(case log.status
            when '200 OK' then 0 else 1 end ) / COUNT(log.status),3) as error
            FROM log GROUP BY date(time)
            ORDER BY error desc) as "sub query" WHERE error > 1;''')


if(__name__ == '__main__'):
    question = input(''' "Please choose your question to be answered:\n
        1. What are the most popular three articles of all time?\n
        2. Who are the most popular article authors of all time?\n
        3. On which days did more than 1 % of requests lead to errors?\n''')

    query_result_1 = getQuery(sql_query_1)
    result_1 = manipulateQueryResult(query_result_1)

    query_result_2 = getQuery(sql_query_2)
    result_2 = manipulateQueryResult(query_result_2)

    query_result_3 = getQuery(sql_query_3)
    result_3 = manipulateQuery3_Result(query_result_3)

    if(question == '1')):
        print(result_1)
    elif(question == '2'):
        print(result_2)
    elif(question == '3'):
        print(result_3)
    else:
        print("Not a valid option, Please enter 1, 2 or 3")
