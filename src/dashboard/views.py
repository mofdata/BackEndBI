from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db import connection

def dashboard(request):
    def query(param):
        with connection.cursor() as cursor:
            cursor.execute("select * from table where bar = data")

            row = cursor.fetchone() 

        return row
    

    return HttpResponse("hello world")

