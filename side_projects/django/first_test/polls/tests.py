from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question

class QuestionModelsTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		time = timezone.now() +datetime.timedelta(days=30)
		future_q = Question(pub_date=time)
		self.assertIs(future_q.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_q =  Question(pub_date=time)
		self.assertIs(old_q.was_published_recently, False)

	def test_was_published_recently_with_recent_question(self):
		time = timezone.now()- datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_q = Question(pub_date=time)
		self.assertIs(recent_q.was_published_recently, True)