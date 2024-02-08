from django.urls import path
from .views import addPost,viewPost,updatePost,deletePost

urlpatterns = [
    path('create',addPost,name='addPost'),
    path('view',viewPost,name='viewPost'),
    path('update/<id>',updatePost,name='updatePost/<id>'),
    path('delete/<id>',deletePost,name='deletePost')
]