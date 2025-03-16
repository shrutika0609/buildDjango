from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World")
def homepage(request):
    return HttpResponse("Welcome to Little Lemon")
from datetime import datetime

def display_date(request):
    date_joined = datetime.now().year
    return HttpResponse(f"The current year is {date_joined}")
def menu(request):
    html_content = """
    <html>
        <head>
            <style>
                h1 { color: green; }
                p { color: blue; }
            </style>
        </head>
        <body>
            <h1>Little Lemon Menu</h1>
            <p>Here is the menu for today!</p>
        </body>
    </html>
    """
    return HttpResponse(html_content)
