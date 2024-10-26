from rest_framework import serializers
from .models import UserColorTest

class UserColorTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserColorTest
        fields = ['id', 'test_name', 'uploaded_image', 'result_type', 'test_date']
