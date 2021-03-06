# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
'''
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
'''
from emp_CRUD.models import employee_Tables
from emp_CRUD.serializers import EmployeeSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class EmpList(APIView):
	"""
    	GET all employees, or POST or create a new employee.
    	"""

	def get(self, request, format=None): # format is optional but it can be used for format of a response 
		employees = employee_Tables.objects.all()
        	serializer = EmployeeSerializer(employees, many=True)
        	return Response(serializer.data)

	def post(self, request, format=None):
        	serializer = EmployeeSerializer(data=request.data)
        	if serializer.is_valid():
            		serializer.save()
            		return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:        	
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpList_details(APIView):
	"""
    	GET, PUT and DELETE for employees with attribute emp_ID
    	"""
	def get(self, request, emp_id, format=None): # format is optional but it can be used for format of a response 
		# Retrieve EMP by its emp_ID
		try:
        		emp = employee_Tables.objects.get(emp_ID=emp_id)
        		serializer = EmployeeSerializer(emp)
        		return Response(serializer.data)
    		except emp.DoesNotExist:
        		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def put(self, request, emp_id, format=None):
		# Update an EMP by its emp_ID
		try:
        		emp = employee_Tables.objects.get(emp_ID=emp_id)
			serializer = EmployeeSerializer(emp, data=request.data)
        		if serializer.is_valid():
            			serializer.save()
            			return Response(serializer.data)
			else:
        			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    		except emp.DoesNotExist:
        		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
	def delete(request, emp_id):
		# Delete an EMP by its emp_ID
		try:
        		emp = employee_Tables.objects.get(emp_ID=emp_id)
			emp.delete()
        		return Response(status=status.HTTP_204_NO_CONTENT)

    		except emp.DoesNotExist:
        		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		
