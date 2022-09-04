from django.http import HttpRequest
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request:HttpRequest):
    return TemplateResponse(request, "index.html", {})


def login(request:HttpRequest):
    return TemplateResponse(request, "login.html",{})
