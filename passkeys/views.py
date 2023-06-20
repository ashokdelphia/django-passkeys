from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import UserPasskey

@login_required
def index(request,enroll=False): # noqa
    keys = UserPasskey.objects.filter(user=request.user) # pragma: no cover
    return render(request,'PassKeys.html',{"keys":keys,"enroll":enroll}) # pragma: no cover


@login_required
def delKey(request):
    key=UserPasskey.objects.get(user=request.user, id=request.GET["id"])
    key.delete()
    return HttpResponse("Deleted Successfully")

@login_required
def toggleKey(request):
    id=request.GET["id"]
    q=UserPasskey.objects.filter(user=request.user, id=id)
    if q.count()==1:
        key=q[0]
        key.enabled=not key.enabled
        key.save()
        return HttpResponse("OK")
    return HttpResponse("Error: You own this token so you can't toggle it", status=403)
