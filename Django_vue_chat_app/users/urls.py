
from django.urls import path,include,re_path
from .views import test
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
urlpatterns = [
    path('test/', test,name='test'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
