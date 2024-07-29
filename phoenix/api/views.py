from rest_framework.decorators import api_view
from rest_framework.response import Response
from database.models import Project
from django.http import Http404


@api_view(['GET'])
def hello_world_from_root(request, **kwargs):
	return Response({'first-word': 'hello', 'second-word': 'world',
					'path': 'root'})


@api_view(['GET'])
def hello_world_from_api(request, **kwargs):
	return Response({'first-word': 'hello', 'second-word': 'world',
					'path': 'api'})


@api_view(['GET'])
def hello_world_from_v1(request, **kwargs):
	return Response({'first-word': 'hello', 'second-word': 'world',
					'path': 'api/v1'})


@api_view(['GET'])
def get_projects(request, **kwargs):
	return Response([project.to_dict() for project in Project.objects.all()])


@api_view(['GET'])
def get_project(request, **kwargs):
	try:
		return Response(Project.objects.get(id=kwargs['id']).to_dict())
	except Project.DoesNotExist:
		raise Http404('This project does not exist.')
