from rest_framework import api_view
from resk_framework.response import Response

@api_view(['GET'])
def menu_view(request):
    menu = [
        {
            'name':'Margherita Pizza',
            'description':'Classic cheese pizza with basil'
            'price':299
        },
        {
            'name':'Pneer Tikka',
            'description':'Classic grilld panner freshly spicy chilli and some juciy onion gravy ahhhhh'
            'price':799
        },
        {
            'name':'Gulab jamun',
            'description':'Traditional gol gol kalle bolls with juciy suger syrup and optional - soaked with rum'
            'price':99
        }
                
    ]
    return Response(menu) 