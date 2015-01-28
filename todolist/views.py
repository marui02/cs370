from django.shortcuts import render
from todolist.models import ListItem

# Create your views here.
def index(self):
    items = ListItem.objects.all()
    return render_to_response("index",{'items':items})
