from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from auth_login.models import SuperAdmin
from auth_login.serializers import AdminSerializer
import json


@api_view(['GET', 'POST'])
def admin_user(request):
    if request.method == 'GET':
        queryset = SuperAdmin.objects.all()
        serializer = AdminSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = json.loads(request.body)
        data['password'] = make_password(data['password'])
        print(data)
        serializer = AdminSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)