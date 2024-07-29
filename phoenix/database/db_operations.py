from .models import Project
from django.db import connection


def create_projects(n_projects=10):
	for i in range(1, n_projects + 1):
		Project.objects.create(
			name=f'project {i}',
			description=f'This is project {i}.',
			url=f'www.project{i}.com',
			image_url=f'www.project{i}image.png')


def delete_all_projects():
	Project.objects.all().delete()


def reset_auto_increment():
	with connection.cursor() as cursor:
		cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{Project._meta.db_table}'")
