from rest_framework import serializers
from task_api.models import Emp_details



class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp_details
        fields =['emp_id','first_name','last_name','email','phone_num']