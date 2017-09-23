from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse, HttpResponse
import json


#view type: 1: The serializer alone is not able to respond to an API request, that's why we need to implement a view.
#In this first version of the view (that we will improve soon) we will "manually" transform the data available in the
#serializer dictionary to a JSON response

# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)


# def product_list(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return JSONResponse(serializer.data)

#view type: 2: class based APIS
class ProductList(APIView):
    #http://127.0.0.1:8000/products/
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    #TODO: add sample format here:
    #http://127.0.0.1:8000/products/
    #name(str), description(str), price(str)
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class handleJson(APIView):
    #http://127.0.0.1:8000/returnjson/
    def get(selfself, request, format=None):
        #return JsonResponse({'foo':'bar'})
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Some error message'
        return HttpResponse(json.dumps(response_data), content_type="application/json")


