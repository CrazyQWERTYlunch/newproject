import logging
from django.shortcuts import HttpResponse

# logger = logging.getLogger(__name__)


def index(request):
    html = f"""<!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Homework 1</title>
    </head>
    <body>
        <h1>Это главная страница сайта на Django.</h1>
        <h3>Она находится по адресу: {request.get_host() + request.path}</h3>
    </body>
    </html>
        """
    # logger.debug('Index page requested.')

    return HttpResponse(html)


def about_myself(request):
    html = f"""<!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Homework 1</title>
    </head>
    <body>
        <h1>Это страница обо мне.</h1>
        <h3>Учусь делать первый сайт на django</h3>
    </body>
    </html>
        """
    # logger.debug('About page requested.')

    return HttpResponse(html)
