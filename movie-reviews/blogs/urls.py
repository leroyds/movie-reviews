from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from django.conf import settings

app_name = 'post'

urlpatterns = [
    path('',views.MovieList.as_view(),name='list'),
    path('post_key/<int:pk>/',views.MovieDetailView.as_view(),name='detail_pk'),
    path('post/<slug:slug>/',views.MovieDetailView.as_view(),name='detail'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
