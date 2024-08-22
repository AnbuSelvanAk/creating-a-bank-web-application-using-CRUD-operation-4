from django.shortcuts import render,redirect
from apps.models import Bank
from apps.forms import BankForm


def delete(request,id):
	b=Bank.objects.get(id=id)
	b.delete()
	return redirect('/result')

def update(request,id):
	bank=Bank.objects.get(id=id)
	if request.method=="POST":
		form=BankForm(request.POST,instance=bank)
		if form.is_valid():
			form.save()
		return redirect('/result')
	return render(request,'appfile/update.html',{'b':bank})

def inserting(request):
	form=BankForm()
	if request.method=="POST":
		form=BankForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'appfile/inserting.html',{'form':form})

def read(request):
	bank=Bank.objects.all()
	return render(request,'appfile/result.html',{'b':bank})
