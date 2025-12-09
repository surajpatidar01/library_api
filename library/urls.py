

from rest_framework.routers import DefaultRouter
from .views import BookViewSet, TaskViewSet

router = DefaultRouter()
router.register('book', BookViewSet,basename='book'),
router.register('task', TaskViewSet,basename='task'),

urlpatterns = router.urls



















# from django.contrib import admin
# from django.urls import path
# from .views import (BookCreateList,BookRetrieveUpdateDestroyView,
#                     TaskCreateList,TaskRetrieveUpdateDestroyView,)
#
# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     # path('book/',BookListView.as_view(),name='book'),
#     # path('book/<int:pk>/update/', BookUpdate.as_view()),
#     # path('book/<int:pk>/create/',BookListCreateView.as_view()),
#     # path('book/<int:pk>/delete',BookDelete.as_view()),
#     # path('book/<int:pk>',BookListCreateView.as_view(),name='book_create'),
#     # path('book/<int:pk>',BookRetrieveUpdateDestroyView.as_view(),name='book_update_Destroy'),
#     # path('book/<int:pk>retrieve-update-delete',BookRetrieveUpdateDestroyView.as_view()),
#     # path('book/<int:pk>/list-create',BookCreateList.as_view()),
#     # path('book/',BookListView.as_view()),
#     # #--------Task
#     # path('task/create',TaskListView.as_view()),
#     # path('task/<int:pk>',TaskCreateList.as_view()),
#     # path('task/<int:pk>',TaskRetrieveUpdateDestroyView.as_view()),
#
#     #----Book urls
#     path('book/', BookCreateList.as_view(), name='book-list-create'),
#     path('book/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-rud'),
#
#
#     #--Task urls
#     path('task/', TaskCreateList.as_view(), name='task-list-create'),
#     path('task/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-rud'),
#
#
#
#
# ]
#
#
