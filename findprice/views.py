from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import render
from .extras import indian_currency_format , make_inputs , predict_price_value
def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
def predict_price(request):
    if request.method == "POST":
        inputs = make_inputs(request)
        price = predict_price_value(inputs)
        price = indian_currency_format(price)
        data = {
            'price':price
        }
        return JsonResponse(data)