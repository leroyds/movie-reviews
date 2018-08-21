from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from django.conf import settings

urlpatterns = [
    path('',views.MovieList.as_view())
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
