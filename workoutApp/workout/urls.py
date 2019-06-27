from django.urls import path

from .import views

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    # ex: /workout/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /workout/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
]
