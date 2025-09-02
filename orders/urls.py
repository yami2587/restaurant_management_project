from django.shortcuts import render

def menu_list(request):
    menu_items = [
        {"name": "Pizza","price":"250"},
        {"name": "pasta","price":"450"},
        {"name": "biryani","price":"650"},
        {"name": "Coffe","price":"150"},
    ]
    return render(request , "menu_list.html" , {"menu_item": menu_items})