from django.conf.urls import url
from django.urls import path
from app_blog import views
app_name="app_blog"
urlpatterns = [
    path('',views.BlogList.as_view(),name="BlogList"),
    path('create-blog/',views.CreateBlog.as_view(),name="createblog"),
    path('details/(?P<slug>[\w\-]+)/$/', views.blog_details, name='blog_details'),
]
