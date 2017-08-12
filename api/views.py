from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from api.models import Mark
from api.serializers import MarkSerializer

def error_json_response(message):
    return JsonResponse({"success": False, "message": message}, status=400)

def json_response(message, status=200):
    return JsonResponse({"success": True, "message": message}, status=status)

def index(request):
    return HttpResponse("OK")

@api_view(['GET'])
def get_marks(request):
    marks = Mark.objects.all()
    serializer = MarkSerializer(marks, many=True)
    return json_response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def add_mark(request):
    data = JSONParser().parse(request)
    serializer = MarkSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return json_response(serializer.data, status=201)
    return error_json_response(serializer.errors)
