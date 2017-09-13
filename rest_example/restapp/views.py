from django.contrib.auth.models import User
from django.http import Http404

from restapp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from restapp.models import *
class UserList(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetail(APIView):

    def get_object(self, pk):
        try:    
            print   (pk)
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print (pk)
        user = self.get_object(pk)
        user = UserSerializer(user)
        print (user.data)
        return Response(user.data)

    def put(self, request, pk, format=None):
        print (pk)
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print (pk)
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class VillageList(APIView):

    def get(self, request, format=None):

        users = village.objects.all()
        #print (users)
        serializer = VillageSerializer(users, many=True)
        print (len(users))
        #print ("ger")
        
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = VillageSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VillageDetail(APIView):

    def get_object(self, pk):
        try:
            return village.objects.get(pk=pk)
        except village.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = VillageSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = VillageSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HouseholdsList(APIView):

    def get(self, request, format=None):

        users = Households.objects.all()
        #print (users)
        serializer = HouseSerializer(users, many=True)
        #print ("ger")
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = HouseSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HouseHoldDetail(APIView):

    def get_object(self, pk):
        try:
            return Households.objects.get(pk=pk)
        except Households.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = HouseSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = HouseSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PersonList(APIView):

    def get(self, request, format=None):

        users = person.objects.all()
        #print (users)
        serializer = PersonSerializer(users, many=True)
        #print ("ger")
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PersonDetail(APIView):

    def get_object(self, pk):
        try:
            return person.objects.get(pk=pk)
        except person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = PersonSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = PersonSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FarmList(APIView):

    def get(self, request, format=None):

        users = farm.objects.all()
        #print (users)
        serializer = FarmSerializer(users, many=True)
        #print ("ger")
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = FarmSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FarmDetail(APIView):

    def get_object(self, pk):
        try:
            return farm.objects.get(pk=pk)
        except farm.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = FarmSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = FarmSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PointsList(APIView):

    def get(self, request, format=None):

        users = points.objects.all()
        #print (users)
        serializer = PointsSerializer(users, many=True)
        #print ("ger")
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = PointsSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PointsDetail(APIView):

    def get_object(self, pk):
        users = points.objects.get(farm_id=pk)
        #print (users)
        serializer = PointsSerializer(users, many=True)
        #print ("ger")
        return Response(serializer.data)

    def get(self, request, pk, format=None):
        users = points.objects.filter(farm_id=pk)
        #print (users)
        serializer = PointsSerializer(users, many=True)
        #print ("ger")
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = PointsSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class WellList(APIView):

    def get(self, request, format=None):

        users = well.objects.all()
        #print (users)
        serializer = WellSerializer(users, many=True)
        #print ("ger")
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = WellSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WellDetail(APIView):

    def get_object(self, pk):
        try:
            return well.objects.get(pk=pk)
        except well.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = WellSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = WellSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class WateryieldList(APIView):

    def get(self, request, format=None):

        users = wateryield.objects.all()
        #print (users)
        serializer = WateryieldSerializer(users, many=True)
        #print ("ger")
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = WateryieldSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WateryieldDetail(APIView):

    def get_object(self, pk):
        try:
            return wateryield.objects.get(well_id=pk)
        except wateryield.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = WateryieldSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = WateryieldSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


