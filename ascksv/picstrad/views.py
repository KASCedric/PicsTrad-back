from PIL import Image
from django.shortcuts import render
from django.http import HttpResponse
from pytesseract import pytesseract
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


def my_view(request):
    # answer = [{'data': 'Hello world!'}]
    answer = {'data': 'Hello world!'}
    return JsonResponse(answer, safe=False)


def ced(request):
    answer = {'data': 'Hello cedric!'}
    return JsonResponse(answer, safe=False)


@api_view(["POST"])
def year_of_birth(request):

    data = request.data

    try:
        age = data["age"]
        year = 2020 - age
        data['year_of_birth'] = year
        return JsonResponse(data, safe=False)

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def image(request):
    data = request.data
    print(data)
    request_image = data['image'].file
    filename = "request_image.jpeg"

    with open(filename, 'wb') as out:
        out.write(request_image.read())

    # answer = {'data': "saved"}
    # return JsonResponse(answer, safe=False)

    print(type(request_image))

    print(data)
    # test = Image.open(filename)

    text = pytesseract.image_to_string(Image.open(filename))
    # os.remove(filename)
    print(text)

    answer = {'data': text}
    return JsonResponse(answer, safe=False)
