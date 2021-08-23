from django.db.models import fields
from rest_framework import serializers
from .models import *


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(GenderSerializer, self).to_representation(instance)
        rep['gender'] = instance.gender.gender
        return rep


class UserSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'gender', 'email', 'password']

class UserSerializerForPK(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'gender', 'email']

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializerForPK()

    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(PostSerializer, self).to_representation(instance)
        rep['posttype'] = instance.posttype.post_type
        # rep['foreignkeyname'] = instance.foreignkeyname.actualfieldname in parent table
        return rep


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"


class PostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostType
        fields = "__all__"
