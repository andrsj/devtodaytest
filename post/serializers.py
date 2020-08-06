from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):

    comments = serializers.SlugRelatedField(
        many=True, slug_field="content", read_only=True
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "creation_date",
            "count_upvotes",
            "author_name",
            "comments",
        )
        read_only_fields = ("count_upvotes",)
