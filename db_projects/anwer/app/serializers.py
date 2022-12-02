from rest_framework import serializers
from app.models import Doctor
class DoctorRegSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields =('id','name','email','phone','department','place')