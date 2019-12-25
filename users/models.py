from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	img = models.ImageField(default='default.png', upload_to='profilePics')

	def __str__(self):
		return f'{self.user.username}\'s Profile'