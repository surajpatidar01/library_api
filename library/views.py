from rest_framework import viewsets
from .models import Book, Task
from .serializer import BookSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import APIException



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    #filter user, category ,status ;;
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['status','category']

    def get_queryset(self):
        try:
            queryset = Task.objects.filter(user=self.request.user)

            status = self.request.query_params.get('status')
            if status:
                queryset = queryset.filter(status=status)

            category = self.request.query_params.get('category')
            if category:
                queryset = queryset.filter(category=category)
            return queryset

        except Exception as e :
            raise APIException(f"Task could not be created: {str(e)}")



    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)

        except Exception as e:
            raise ValidationError(f"Task could not be created: {str(e)}")


#--book view

# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookListCreateView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookUpdate(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#

# class BookDelete(generics.DestroyAPIView):
#     queryset = Book.objects.all()

    # serializer_class = BookSerializer


# class TaskListView(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer