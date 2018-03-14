from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse

class QuestionModelsTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		time = timezone.now() +datetime.timedelta(days=30)
		future_q = Question(pub_date=time)
		self.assertIs(future_q.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_q =  Question(pub_date=time)
		self.assertIs(old_q.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		time = timezone.now()- datetime.timedelta(hours=23, minutes=59, seconds=50)
		recent_q = Question(pub_date=time)
		self.assertIs(recent_q.was_published_recently(), True)

def create_question(question_text, days):
	time = timezone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
	def test_no_question(self):
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, " No polls here")
		self.assertQuerysetEqual(response.context['latest_q_list'],[])
	def test_past_question(self):
		create_question("What;s Your favorite name?", -2)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_q_list'],['<Question: What;s Your favorite name?>']
		)
	def test_future_question(self):
		create_question("Future Question", 10)
		res = self.client.get(reverse("polls:index"))
		self.assertEqual(res.status_code, 200)
		self.assertContains(res, " No polls here")
		self.assertQuerysetEqual(res.context['latest_q_list'],[])
	def test_future_and_two_past_questions(self):
		create_question("Future Question", 10)
		create_question("Past Question", -10)
		create_question("More Qu", -12)
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['latest_q_list'],['<Question: Past Question>','<Question: More Qu>'])


class QuestionDetailViewTests(TestCase):
	def test_future_question(self):
		future_q = create_question("Future Question",10)
	
		url =reverse('polls:detail', args=(future_q.id,))
		res = self.client.get(url)
		self.assertEqual(res.status_code, 404)
	def test_past_question(self):
		past_q = create_question("Past Question", -10)
		res = self.client.get(reverse("polls:detail", args=(past_q.id,)))
		self.assertContains(res, past_q.question_text)