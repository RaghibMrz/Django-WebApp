from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# class User(object):
# 	"""docstring for User"""
# 	def __init__(self, arg):
# 		super(User, self).__init__()
# 		self.arg = arg


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	img = models.ImageField(default='default.png', upload_to='profilePics')
	userID = models.CharField(max_length=64)


	def __str__(self):
		return f'{self.user.username}\'s Profile'


	#overriding save method to scale down any uploaded picture
	#optimises speed and saves space
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		image = Image.open(self.img.path)

		if image.height > 200 or image.width > 200:
			outputSize = (200, 200)
			image = image.resize(outputSize)
			image.save(self.img.path)