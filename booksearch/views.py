from django.shortcuts import render
from django.http import HttpResponse
import os
import psycopg2


def index(request):
    return render(request, 'booksearch/Frontpage.html', {})


def top(request):
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Raamatud;")
    book = cur.fetchone()
    cur.close()
    conn.close()
    html = "<html><body>Top1 raamat on %s.</body></html>" % book[1]
    return HttpResponse(html)
