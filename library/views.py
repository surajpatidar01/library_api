from rest_framework import viewsets, permissions
from .models import Book, Task
from .serializer import BookSerializer, TaskSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        queryset = Task.objects.filter(user=self.request.user)

        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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