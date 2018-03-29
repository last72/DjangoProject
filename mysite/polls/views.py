"""
Define function of webpages.
"""
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question


# Create your views here.
def index(request):
    """Index page"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """Details page"""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(question_id):
    """Results page"""
    response = "You're looking at the result of question %s"
    return HttpResponse(response % question_id)

def vote(question_id):
    """Vote page"""
    return HttpResponse("You're looking at the result of question %s." % question_id)
