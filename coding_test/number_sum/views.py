from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from coding_test.number_sum.serializers import NumberSumSerializer

numbers_to_add = list(range(10000001))

class TotalViewSet(viewsets.GenericViewSet):
    
    def list(self, request=numbers_to_add):
        serializer = NumberSumSerializer(
            instance = self
        )
        return Response(serializer.data)
