from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Group, Message

@login_required
def groups(request):
    groups = Group.objects.all()

    return render(request, 'group/groups.html', {'groups': groups})

@login_required
def group(request, slug):
    # group details for viewing before joining
    #slug to find the group in db
    group = Group.objects.get(slug=slug)
    messages=Message.objects.filter(group=group)[0:25]

    return render(request, 'group/group.html', {'group': group, 'messages': messages})
