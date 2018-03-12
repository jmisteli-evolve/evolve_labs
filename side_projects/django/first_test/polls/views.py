from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from polls.models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_q_list'

	def queryset(self):
		"""Return the last 5 published question"""
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/details.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

# def index(request):
# 	latest_q_list = Question.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('polls/index.html')
# 	context = {
# 		'latest_q_list': latest_q_list,
# 	}
# 	return HttpResponse(template.render(context, request))
# 	"""
# 	#Alternative code using render shortcut
# 	latest_q_list = Question.objects.order_by('-pub_date')[:5]
# 	context = {'latest_q_list: latest_q_list'}
# 	return render(request, 'polls/index.html', context)
# 	"""

# def blob(request):
# 	return HttpResponse("This is BLOB~~~~?")

# def detail(req, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(req, 'polls/details.html', {'question': question})
# 	"""
# 	try: 
# 		question = Question.objects.get(pk=question_id)
# 	except:
# 		raise Http404("Question does not exist")
# 	return render(req, 'polls/details.html', {'question':question})
# 	"""
# def results(req, question_id):
# 	return HttpResponse("You're looking at the result of question %s" % question_id)

def vote(req, question_id):
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk=req.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(req, 'polls/details.html', {
			'question':question,
			'error_message': "You didn't select a choice"
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect((reverse('polls:results', args=(question.id,))))
# def results(req, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(req, 'polls/results.html', {'question':question})