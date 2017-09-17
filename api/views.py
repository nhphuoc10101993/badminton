from rest_framework import generics
from .serializers import BucketListSerializer
from .models import BucketList
class CreateView(generics.ListCreateAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    def perform_create(self, serializer):
        serializer.save()

