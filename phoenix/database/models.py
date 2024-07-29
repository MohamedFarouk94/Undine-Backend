from django.db import models


# Create your models here.
class Project(models.Model):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	url = models.CharField(max_length=255, null=True)
	image_url = models.CharField(max_length=255, null=True)
	date_created = models.DateField(auto_now_add=True)

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'url': self.url,
			'image_url': self.image_url,
			'date_created': self.date_created
		}
