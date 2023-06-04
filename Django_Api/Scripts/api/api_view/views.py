from django.shortcuts import render
from api_view.models import product
from rest_framework.response import Response
from api_view.serializer import ProductsSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def product_list(request):
    products = product.objects.all() #complex data
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def product_create(request):
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def action(request,pk):
    try: 
        products = product.objects.get(pk = pk)
    except:
        return Response({
            'error':'Product Does Not Exist'
        },status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductsSerializer(products) #above state is complex we need to get it to json file
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = ProductsSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)
    if request.method == "DELETE":
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        