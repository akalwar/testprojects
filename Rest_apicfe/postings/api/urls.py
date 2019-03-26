""""
Use this for reference when in doubt
restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import BlogPostRudView, BlogPostApiView

app_name ='api-postings'
urlpatterns = [
    path('', BlogPostApiView.as_view(), name='Post-listcreate'), #(?p<pk>\d+)
    path('<int:pk>/', BlogPostRudView.as_view(), name='Post-rud'),
]
