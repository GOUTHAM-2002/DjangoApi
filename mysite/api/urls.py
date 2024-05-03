from django.urls import path,include
from . import views

urlpatterns = [
    path("blogposts/",views.BlogPostListCreate.as_view(),name ="blogpost-create" ),
path("blogposts/<int:pk>/",views.BlogPostUpdateOrDelete.as_view(),name ="blogpost-updateordelete" ),
]