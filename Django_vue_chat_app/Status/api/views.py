from .serializers import MessagesSerializer,StatusSerializer,CommentsSerializer
from Status.models import Messages,Status,Comments
from rest_framework import generics ,status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from Status.api.permissions import IsPostOwnerorReadonly
from rest_framework.response import Response

from rest_framework.filters import SearchFilter,OrderingFilter
class StatusCreate(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    def perform_create(self, serializer):
        sender=self.request.user
        serializer.save(author=sender)
class Statusedit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'slug'
    permission_classes = [IsPostOwnerorReadonly]
class CommentCreate(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    lookup_field = 'pk'
    def perform_create(self, serializer):
        post_pk = self.kwargs.get('pk')
        post = get_object_or_404(Status,pk=post_pk)
        user=self.request.user
        serializer.save(author=user,post=post)
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
class MessagesCreate(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['time','sender__username','receiver__username']
    def perform_create(self, serializer):
        sender=self.request.user
        serializer.save(sender=sender)
class StatusLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an answer instance."""
    serializer_class = StatusSerializer


    def delete(self, request, slug):
        """Remove request.user from the voters queryset of an answer instance."""
        answer = get_object_or_404(Status, slug=slug)
        user = request.user

        answer.likes.remove(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug):
        """Add request.user to the voters queryset of an answer instance."""
        answer = get_object_or_404(Status, slug=slug)
        user = request.user

        answer.likes.add(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
class Messageedit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    lookup_field = 'pk'