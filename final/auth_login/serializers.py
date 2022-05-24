from rest_framework.serializers import Serializer, ModelSerializer
from auth_login.models import SuperAdmin

class AdminSerializer(ModelSerializer):
    class Meta:
        model = SuperAdmin
        fields = ['username', 'email']