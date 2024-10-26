from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserColorTest
from .serializers import UserColorTestSerializer
from rest_framework.response import Response
from rest_framework import status


class UserColorTestViewSet(viewsets.ModelViewSet):
    serializer_class = UserColorTestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserColorTest.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response({"id": serializer.instance.id}, status=status.HTTP_201_CREATED)
