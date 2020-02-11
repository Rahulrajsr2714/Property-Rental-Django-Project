from .models import Property , Account
from rest_framework import serializers

class Userprofileserializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username','last_login','email')
class Propertyserializer(serializers.ModelSerializer):
    user = Userprofileserializer()
    class Meta:
        model = Property
        fields = ('date_added','property_name','user')