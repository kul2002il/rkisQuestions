from django.shortcuts import render
from .models import Question


def index(request):
	que = Question.objects.all()[:10]
	context = {"questions": que}
	return render(request, 'main/index.html', context=context)



