from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from demo.models import repair
from demo.models import suggestion
import datetime as dt
from datetime import date

# Create your views here.

# def index(request):
# 	return render(request,'index.html')

# def adminapp(request):
#  	return render(request,'adminapp.html')

def sucess(request):
	return render(request,'sucess.html')

def sent(request):
	return render(request,'thanks.html')	

def home(request):
	return render(request,'index.html')	

def repairs(request):
	if request.method=="POST":
		N=request.POST['Name']
		D=request.POST['Device']
		C=request.POST['Company']
		T=request.POST['Type']
		P=request.POST['Problem']
		Ph=request.POST['Phone']
		A=request.POST['Address']
		repair.objects.create(Name=N,Device=D,Company=C,Type=T,Problem=P,Phone=Ph,Address=A)
		return redirect('sucess')

	details=repair.objects.all()
	return render(request,'book.html',{'Details':details})	

def suggestions(request):
	if request.method=="POST":
		N=request.POST['Name']
		C=request.POST['Contact']
		E=request.POST['Email']
		M=request.POST['Message']
		suggestion.objects.create(Name=N,Contact=C,Email=E,Message=M)
		return redirect('sent')

	details=suggestion.objects.all()
	return render(request,'contact.html',{'Details':details})

def adminapp(request):
	details=repair.objects.all()
	return render(request,'adminapp.html',{'details':details})	

def feedback(request):
	details=suggestion.objects.all()
	return render(request,'feedback.html',{'details':details})	

def delete(request, id):
  details=repair.objects.get(id=id)
  details.delete()
  return redirect('adminapp')

	
