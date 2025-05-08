from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader

# def members(request):
#     return HttpResponse("Hello World !!")

def members(request):
    return render(request, 'members/home.html')