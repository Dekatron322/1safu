from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, TextInput, Select
from django.utils import timezone



class Message(models.Model):
	title = models.CharField(blank=True, max_length=100)
	message = models.TextField()
	#user = models.OneToOneField(User, on_delete=models.CASCADE)
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title
