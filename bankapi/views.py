from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from main.serializers import BanksSerializer
from main.models import Banks
from .models import Banks
from .serializers import BanksSerializer

class BankCityDetailView(generics.ListCreateAPIView):
	queryset = Banks.objects.all()
	
	def get(self, request, bank_name, city):
		branch_qset = Banks.objects.filter(
		city__iexact=city, bank_name__icontains=bank_name)
		serializer = BanksSerializer(branch_qset, many=True)
		return Response(serializer.data)

class IfscDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Banks.objects.all()
	serializer_class = BanksSerializer
	def get(self, request, *args, **kwargs):
		try:
			a_bank = self.queryset.get(ifsc=kwargs["ifsc"])
			return Response(BanksSerializer(a_bank).data)
		except Banks.DoesNotExist:
			return Response(
				data={
				"message": "This IFSC {} does not exist. Please enter valid IFSC Code".format(kwargs["ifsc"])
				},
				status=status.HTTP_404_NOT_FOUND
			)