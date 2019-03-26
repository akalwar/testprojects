from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    #/music/
    path('', views.IndexView.as_view(), name='index'),
    #/music/pk
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #/music/album/add
    path('album/add/', views.AlbumCreate.as_view(), name='Album_add'),
    # /music/album/pk/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='Album_Update'),
    # /music/add
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='Album_Delete'),
    # /music/register
    path('register/', views.UserFormView.as_view(), name='register'),
]


