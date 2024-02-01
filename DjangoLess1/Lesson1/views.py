# from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import logging

# logging.basicConfig(level=logging.INFO, filename="logging_lesson1.log", filemode="w",
#                     format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def index(request):
    html = "<h1><b><i>Главная страница моего первого сайта на Django</i></b></h1>" \
           "<p>Домашнее задание для GeekBrains</p>"
    logging.info("Переход на главную страницу")
    return HttpResponse(html)


def about(request):
    html = "<h1><b><i>Страница о себе</i></b></h1>" \
           "<p>Меня зовут Завалищин Сергей. Сейчас вы можете видеть мой первый сайт на Django!</p>"
    logging.info("Переход на страницу о себе")
    return HttpResponse(html)
