# from django.shortcuts import render
# # from django.http import HttpResponse
# # from django.template import loader

# # def members(request):
# #     return HttpResponse("Hello World !!")

# from .models import Member

# def members(request):
#     all_members = Member.objects.all() # Fetches all rows from the table
#     return render(request, 'members/all_members.html', {'members': all_members})


# from django.shortcuts import render
# from .models import Member

# def members(request):
#     all_members = Member.objects.all()
#     return render(request, 'members/all_members.html', {'mymembers': all_members})

# def details(request, id):
#     member = Member.objects.get(id=id)
#     return render(request, 'members/details.html', {'member':member})

from django.shortcuts import render, get_object_or_404
from .models import Member

def all_members(request):
    # Fetch all members from the database
    members = Member.objects.all()
    return render(request, 'members/all_members.html', {'members': members})

def member_details(request, id):
    # Fetch a single member by its ID
    member = get_object_or_404(Member, pk=id)
    return render(request, 'members/details.html', {'member': member})
