from django.shortcuts import render
from models import Grade, Subfield,Grade, Stage

def stage(request):
	context={}
	stage=Stage.objects.all().order_by('pk')
	print stage
	context['stagelist']=stage
	return render(request,'stagelist.html',context)

def stagedetail(request, pk):
	context = {}
	stage = Stage.objects.get(pk=pk)
	context['stage'] = stage
	return render(request, 'stagedetail.html', context)

# Create your views here.
def gradelist(request):
	context={}
	grades=Grade.objects.all().order_by('pk')
	print grades
	context['gradelist']=grades
	return render(request,'gradelist.html',context)

def gradedetail(request, pk):
	context = {}
	grade = Grade.objects.get(pk=pk)
	context['grade'] = grade
	return render(request, 'gradedetail.html', context)

def subfielddetail(request,pk):
	context ={}
	subfield = Subfield.objects.get(pk=pk)
	context['subfield'] = subfield
	return render(request, 'subfielddetail.html', context)

def teacher (request):
	context={}
	return render(request,'teacher.html',context)