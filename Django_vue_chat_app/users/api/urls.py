
from django.urls import path,include,re_path
from users.api.views import CustomUserview
from django.conf.urls import url
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
urlpatterns = [
    path(r'user/', CustomUserview.as_view(),name='current_user'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
