from Status.models import Messages,Status,Comments
from rest_framework import serializers
class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = Comments
        exclude = ('post','likes')

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y,%I:%M:%S")

class StatusSerializer(serializers.ModelSerializer):
    reviews = CommentsSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    likes_post = serializers.SerializerMethodField()
    # user_has_answered = serializers.SerializerMethodField()

    class Meta:
        model = Status
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y,%I:%M:%S")

    def get_likes_post(self, instance):
        return instance.likes.count()

    # def get_user_has_answered(self, instance):
    #     request = self.context.get("request")
    #     return instance.comments.filter(author=request.user).exists()

class MessagesSerializer(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()
    class Meta:
        model = Messages
        fields = '__all__'
    def get_time(self, instance):
        return instance.time.strftime("%B %d, %Y,%I:%M:%S %p")
