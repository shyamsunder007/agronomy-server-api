from django.contrib.auth.models import User

from rest_framework_gis import serializers
from restapp.models import *

class RadomSerializer(serializers.ModelSerializer):
    class Meta:
        model = random
        fields = ('id','farm_id','point','poly')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = village
        #print (str(model)+"hai")
        fields = ('id', 'village_name')


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Households
        #print (str(model)+"hai")
        fields = ('id', 'Households_lat','Households_lon','Households_vilid')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = person
        #print (str(model)+"hai")
        fields = ('id', 'person','gender','age','person_hid')

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = farm
        #print (str(model)+"hai")
        fields = ('id', 'house_id','farm_area','season_crop')

class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = points
        #print (str(model)+"hai")
        fields = ('id', 'farm_id','lat','lon')

class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = well
        #print (str(model)+"hai")
        fields = ('id', 'farm_id','lat','lon')

class WateryieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = wateryield
        #print (str(model)+"hai")
        fields = ('id', 'well_id','yieldd','DateTimeField')

class DumbSerializer(serializers.ModelSerializer):
    class Meta:
        model = dumb
        #print (str(model)+"hai")
        fields = ('id', 'farmm_id','point')
