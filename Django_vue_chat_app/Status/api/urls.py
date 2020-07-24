from .views import MessagesCreate,Messageedit,StatusCreate,Statusedit,StatusLikeAPIView,CommentCreate,CommentDetail
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path(r'status/', StatusCreate.as_view(), name='status'),
    path(r'status/<str:slug>', Statusedit.as_view(), name='status-edit'),
    path(r'message/', MessagesCreate.as_view(), name='message'),
    path(r'comment/<str:pk>/', CommentDetail.as_view(), name='comment-create'),
    path(r'status/<str:slug>/comment', CommentCreate.as_view(), name='comment-post'),
    path(r'message/<int:pk>', Messageedit.as_view(), name='message-edit'),
    path(r'status/<str:slug>/like', StatusLikeAPIView.as_view(), name='like'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)