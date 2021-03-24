from django.shortcuts import render
from django.http import JsonResponse

def Home(request):
    movie= {
        "movie name":"vakeel sab",
        "language":"Telugu",
        "year":2021
    }
    return JsonResponse(movie)
