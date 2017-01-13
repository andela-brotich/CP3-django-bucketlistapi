from django.http import HttpResponse


def index(request):
    response = HttpResponse("OK")
    response["Access-Control-Allow-Origin"] = "*"
    return response