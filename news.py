#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime

import psycopg2


def top3():

    try:
        db = psycopg2.connect("dbname=news")
    except psycopg2.Error as e:
        print("Unable to connect to the database")

    c = db.cursor()

    c.execute(
      "select articles.title, COUNT(articles.id) as cont FROM " +
      "articles join log ON log.path like " +
      "CONCAT('%',articles.slug,'%') " +
      "WHERE log.status like '%200 OK%' GROUP BY" +
      " articles.id order by cont desc Limit 3;"
    )

    results = c.fetchall()
    print("Top 3 articles\r\n")
    file.write("Top 3 articles\r\n")
    for x, y in enumerate(results):
        print(str(results[x][0]) + " -- " + str(results[x][1]) + " Views")
        file.write(str(results[x][0]) + " -- " + str(results[x][1]) + " Views")
        file.write("\r\n")
    print("\r\n")
    file.write("\r\n")

    db.close()

    return


def authors():

    try:
        db = psycopg2.connect("dbname=news")
    except psycopg2.Error as e:
        print("Unable to connect to the database")

    c = db.cursor()

    c.execute(
      "select authors.name, SUM(pubs.cont) as maisFamoso from authors" +
      ",(select COUNT(articles.id) as cont, articles.title," +
      "articles.id, articles.author FROM articles " +
      "join log ON log.path like " +
      "CONCAT('%',articles.slug,'%') and log.status like '%200 OK%' " +
      "GROUP BY articles.id) as pubs where authors.id=pubs.author GROUP BY " +
      "authors.name order by maisFamoso desc;")

    results = c.fetchall()

    print("Most popular authors\r\n")

    file.write("Most popular authors\r\n")

    for x, y in enumerate(results):
        print(str(results[x][0]) + " -- " + str(results[x][1]) + " Views")
        file.write(str(results[x][0]) + " -- " + str(results[x][1]) + " Views")
        file.write("\r\n")
    print("\n")
    file.write("\r\n")

    db.close()

    return


def daysRequisitionReallyFailed():

    # i learned how to get day, month and year from the following site:
    # http://mascix.blogspot.com/2008/02/postgresql-group-by-day-week-and-month.html
    try:
        db = psycopg2.connect("dbname=news")
    except psycopg2.Error as e:
        print("Unable to connect to the database")

    c = db.cursor()

    c.execute(
      "select * from ( select okay.Day, okay.HTTP_OKAY, notokay.HTTP_NOT, " +
      "(100.0 *notokay.HTTP_NOT / (okay.HTTP_OKAY+notokay.HTTP_NOT)) " +
      "as percent from (SELECT " +
      "date_trunc('day', log.time) AS Day, " +
      "count(log.status) as HTTP_OKAY FROM " +
      "log WHERE status like '%200 OK%' GROUP BY Day ORDER BY Day) as okay " +
      "join (SELECT date_trunc('day', log.time) AS Day, count(log.status) " +
      "as HTTP_NOT FROM log WHERE status" +
      " not like '%200 OK%' GROUP BY Day ORDER BY Day)" +
      " as notokay on okay.Day=notokay.Day) as" +
      " result WHERE result.percent>=1.00;")

    results = c.fetchall()
    print("Days with more than 1% of errors\r\n")
    file.write("Days with more than 1% of errors\r\n")

    for x, y in enumerate(results):

        dia = results[x][0].day
        month = results[x][0].month
        year = results[x][0].year
        percent = results[x][3]
        print(
          str(dia) + "/"+str(month) + "/"+str(year) +
          "  " + str(round(percent, 2)) + "% errors"
          )
        file.write(
          str(dia) + "/"+str(month) + "/"+str(year) +
          "  " + str(round(percent, 2)) + "% errors"
          )
        file.write("\r\n")
    print("\n")
    file.write("\r\n")

    db.close()

    return


print("Program starting...\n")

file = open("log.txt", "w")

top3()

authors()

daysRequisitionReallyFailed()

file.close()
