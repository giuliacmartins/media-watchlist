from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home/', views.home, name='mylist-home'),
    path('personallist/', views.personallist, name='mylist-personallist'),
    path('search/', views.search, name='mylist-search'),
    path('animelist/', views.animelist, name='mylist-animelist'),
    path('api/addmedia', views.add_media, name='mylist-add-media'),
    path('api/addanime', views.add_anime, name='mylist-add-anime'),
    path('removemedia/<int:id>', views.remove_media, name='mylist-remove-media'),
    path('removecompleted/<int:id>', views.remove_completed, name='mylist-remove-completed'),
    path('removenotcompleted/<int:id>', views.remove_notcompleted, name='mylist-remove-not-completed'),
    path('completed/<int:id>', views.completed_media, name='mylist-completed-media'),
    path('notcompleted/<int:id>', views.not_completed_media, name='mylist-not-completed-media'),
    path('notcompletedtocompleted/<int:id>', views.not_completed_to_completed, name='mylist-not-completed-to-completed'),
    path('removeanime/<int:id>', views.remove_anime, name='mylist-remove-anime'),
    path('removecompletedanime/<int:id>', views.remove_completed_anime, name='mylist-remove-completed-anime'),
    path('removenotcompletedanime/<int:id>', views.remove_notcompleted_anime, name='mylist-remove-not-completed-anime'),
    path('completedanime/<int:id>', views.completed_anime, name='mylist-completed-anime'),
    path('notcompletedanime/<int:id>', views.not_completed_anime, name='mylist-not-completed-anime'),
    path('notcompletedtocompletedanime/<int:id>', views.not_completed_to_completed_anime, name='mylist-not-completed-to-completed-anime'),
    path('prioritywatchmedia/<int:id>', views.priority_media, name='mylist-priority-media'),
    path('prioritywatchanime/<int:id>', views.priority_anime, name='mylist-priority-anime'),
    path('removeprioritymedia/<int:id>', views.remove_priority_media, name='mylist-remove-priority-media'),
    path('removepriorityanime/<int:id>', views.remove_priority_anime, name='mylist-remove-priority-anime'),
    path('prioritymediatocompleted/<int:id>', views.priority_media_to_completed, name='mylist-priority-media-to-completed'),
    path('prioritymediatocompletedanime/<int:id>', views.priority_anime_to_completed_anime, name='mylist-priority-media-to-completed-anime'),
]