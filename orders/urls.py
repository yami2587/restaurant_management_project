from django.shortcuts import render
from django.http import HttpResponse

def menu_list(request):
    try:  
        menu_items = [
            {"name": "Pizza","price":"250"},
            {"name": "pasta","price":"450"},
            {"name": "biryani","price":"650"},
            {"name": "Coffe","price":"150"},
        ]
        return render(request , "menu_list.html" , {"menu_item": menu_items})
    except Exception as e:
        error_message: f"Oops! somthing wrong : {str(e)}"
        return HttpResponse(error_message,status=500)
