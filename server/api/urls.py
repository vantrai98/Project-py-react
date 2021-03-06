from django.urls.conf import path
from api.user import users
from api.project import projects

urlpatterns = [
    path('users', users.UserList.as_view(), name="users"),
    path('users/<int:pk>', users.UserDetail.as_view(), name="user_detail"),
    path('projects', projects.ProjectList.as_view(), name="projects"),
]
