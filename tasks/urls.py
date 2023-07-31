from django.urls import path

from .views import TasklistView,TaskDetailView
urlpatterns = [
   
   path('',TasklistView.as_view(), name= 'task_list'),
   path('<int:pk>/',TaskDetailView.as_view(), name= 'task_detail')

]