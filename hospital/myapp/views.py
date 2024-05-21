from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PatientSerializer
from myapp import serializers
from .models import Patient


# Create your views here.
@api_view(["GET"])
def text(request):
    return HttpResponse("<h2>hello world</h2>")


# Create api_urls_list.
@api_view(["GET"])
def api_ulr(request):
    api_ulr_list = {
        'get_list': 'get_all/',
        'get_data': 'get_data/<int:id>/',
        'post': 'post_data/',
        'update': 'update_task/<int:id>/',
        'delete': 'delete_task/<int:id>/'
    }
    return Response({'api_ulr_List': api_ulr_list})


# Get All
@api_view(["GET"])
def get_all(request):
    patient_obt = Patient.objects.all()
    ser_data = PatientSerializer(patient_obt, many=True)
    return Response({"status": 200, "data": ser_data.data})


# Get By id
@api_view(["GET"])
def get_data(request, id):
    patient_obt = Patient.objects.get(id=id)
    ser_data = PatientSerializer(patient_obt)
    return Response({"status": 200, "data": ser_data.data})


# Post data method
@api_view(["POST"])
def post_data(request):
    result = PatientSerializer(data=request.data)
    if result.is_valid():
        result.save()
        return Response(result.data, status=status.HTTP_201_CREATED)
    # return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(result)


# Update data method
@api_view(["PUT"])
def update_task(request, id):
    response = Patient.objects.get(id=id)
    serializer = PatientSerializer(instance=response, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete data method
@api_view(["DELETE"])
def delete_task(request, _id):
    res = Patient.objects.get(id=_id)
    res.delete()
    return Response(
        "Data is deleted successfully!",
        status=status.HTTP_204_NO_CONTENT)


# Patch data method
@api_view(["PATCH"])
def patch(request, id):
    test_object = Patient.objects.get(id=id)
    serializer = PatientSerializer(test_object, data=request.data,
                                   partial=True)  # set partial=True to update a data partially
    if not serializer.is_valid():
        return JsonResponse(data="wrong parameters")
    serializer.save()
    return JsonResponse(data=serializer.data)
