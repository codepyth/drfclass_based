from django.urls import path
from postdrfapp.views import GenderAdd, GenderDelete, GenderList, PostAdd, PostDelete, PostDetail, PostList, PostTypeAdd, PostTypeDelete, PostTypeList, RegisterUser


urlpatterns = [
    path('register/', RegisterUser.as_view()),
    path('gender/', GenderList.as_view()),
    path('gender/add', GenderAdd.as_view()),
    path('gender/delete/<int:pk>/', GenderDelete.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/add/', PostAdd.as_view()),
    path('posts/delete/<int:pk>/', PostDelete.as_view()),
    path('posts/detail/<int:pk>/', PostDetail.as_view()),
    path('posttype/', PostTypeList.as_view()),
    path('posttype/add/', PostTypeAdd.as_view()),
    path('posttype/delete/<int:pk>/', PostTypeDelete.as_view()),
    # path(''),
]