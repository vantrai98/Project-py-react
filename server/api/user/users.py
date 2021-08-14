from api.user.serializer import UserSerializer
from rest_framework import mixins, generics
from rest_framework import permissions
from django.contrib.auth.models import User


class UserList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    #  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    queryset = User.objects

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
