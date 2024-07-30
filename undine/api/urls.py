from django.urls import path
from . import views


urlpatterns = [
	path('', 						 views.hello_world_from_root, 	name='hello_world'),
	path('api', 					 views.hello_world_from_api,	name='hello_world'),
	path('api/v1', 					 views.hello_world_from_v1,		name='hello_world'),
	path('api/v1/projects', 		 views.get_projects, 		  	name='get_projects'),
	path('api/v1/projects/<int:id>', views.get_project, 		  	name='get_project'),
]
