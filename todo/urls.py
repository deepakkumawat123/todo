from django.urls import path
from.import views

urlpatterns = [

    path('addTask/',views.addTask,name='addTask'),
    # marks as done 
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    # marks as under 
    path('mark_as_under/<int:pk>/',views.mark_as_under,name='mark_as_under'),
    #edit feature

    path('edit/<int:pk>/',views.edit,name='edit'),
    
    path('delete/<int:pk>/',views.delete,name='delete'),
  
] 