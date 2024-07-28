from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def hello_world(request, **kwargs):
	print('ok')
	return Response({'first-word': 'hello', 'second-word': 'world'})
