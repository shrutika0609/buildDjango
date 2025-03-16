from django.http import HttpResponse

def home(request):
    path = request.path  # Access the path property of the request object
    return HttpResponse(path, content_type="text/plain; charset=utf-8")
