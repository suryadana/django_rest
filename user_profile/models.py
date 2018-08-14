from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	MALE = 0
	FEMALE = 1
	GENDERS = (
		(MALE, 'Laki-laki'),
		(FEMALE, 'Perempuan')
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	birth = models.DateField(null=True)
	gender = models.PositiveSmallIntegerField(choices=GENDERS, default=MALE)
