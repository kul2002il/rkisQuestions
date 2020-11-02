from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	def Meta(self):
		pass


class Question(models.Model):
	title = models.CharField(max_length=255, verbose_name="Название", default='')
	datetime = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата публикации')
	text = models.CharField(max_length=255, verbose_name="Текст", default='')

	def __str__(self):
		return self.title


class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.CharField(max_length=255, verbose_name="Вариант", default='')

	def __str__(self):
		return self.text


class Voice(models.Model):
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.text


