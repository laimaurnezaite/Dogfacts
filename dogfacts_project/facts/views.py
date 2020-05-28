from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.http import HttpResponseRedirect
from .models import Fact

# Create your views here.

def home(request):
    # all_facts = Fact.objects.all()
    # context = {
    #     'facts':all_facts,
    # }
    return render(request, 'home.html')
    # return HttpResponse("Start")

def addFact(request):
    new_fact = Fact()
    new_fact.text = request.POST.get('new_fact')
    new_fact.user_id = request.user.id
    new_fact.save()

    return redirect("/")
    

def morefacts(request):
    all_facts = Fact.objects.all()
    context = {
        'facts':all_facts,
    }
    return render(request, 'facts.html', context)

