from django.shortcuts import render
from firstapp.models import Topic, AccessRecord, Webpage, User

# Create your views here.

def Help(request):
    userlist=User.objects.order_by("first_name")
    date_dict={'access_users': userlist}
    return render(request, 'firstapp/Help.html', context=date_dict)

