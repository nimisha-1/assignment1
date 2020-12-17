from django.shortcuts import render
from rest_framework import generics
from task_api.models import Emp_details
from task_api.serializers import EmpSerializer
from rest_framework.decorators import api_view
# from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class Emplist(generics.ListCreateAPIView):
    queryset = Emp_details.objects.all()
    serializer_class = EmpSerializer


class Empdetail(generics.RetrieveDestroyAPIView):
    queryset = Emp_details
    serializer_class = EmpSerializer

@api_view(['GET','POST'])
def EmpDetail(request):
    if request.method=='POST':
        emp_id=request.data['emp_id']
        first_name=request.data['first_name']
        last_name=request.data['last_name']
        email=request.data['email']
        phone_num=request.data['phone_num']
        data=Emp_details.objects.create(emp_id=emp_id, first_name=first_name, last_name=last_name, email=email, phone_num=phone_num)
        data.save()
        msg="data saved sucessfully"


        return Response(msg, status=200)
    elif request.method == 'GET':
        queryset = Emp_details.objects.all()
        datadict={}
        for item in queryset:
            datadict['emp_id']=item.emp_id
            datadict['first_name']=item.first_name
            datadict['last_name']=item.last_name
            datadict['email']=item.email
            datadict['phone_num']=item.phone_num
        return Response(datadict, status=200)
    return
