from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'discreteMath/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last 3 published questions"""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'discreteMath/detail.html'

class ResultsView(generic.DetailView):
    model=Question
    template_name = 'discreteMath/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request,'discreteMath/detail.html',{
            'question' : question,
            'error_message' : "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('discreteMath:results', args=(question.id,)))

