from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueTogetherValidator


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]

    def validate(self, data):
        data = super().validate(data)
        name = data['name']
        if not name:
            raise serializers.ValidationError('This field required')

        for instance in Category.objects.all():
            if instance.name == name:
                raise serializers.ValidationError(detail="Такая категория уже существует", code="Категория создана")

        return data


class ReturnNameSerializer(serializers.RelatedField):

    def to_representation(self, value):
        return value.name


class ResumeSerializer(serializers.ModelSerializer):

    category = ReturnNameSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = ['id',
                  'first_name',
                  'last_name',
                  'surname',
                  'comment',
                  'phone_number',
                  'email',
                  'file',
                  'category',
                  ]


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ['id', 'title', 'link','image']


class WishlistSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    wished_resume = ResumeSerializer()

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'wished_resume']


class WishlistCreateSerializer(serializers.ModelSerializer):

    wished_resume = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'wished_resume']

    # def validate(self, data):
    #     data = super().validate(data)
    #     user = data['user']
    #     wished_resume = data['wished_resume']
    #
    #     for instance in Wishlist.objects.filter(user=user):
    #         if instance.wished_resume == wished_resume:
    #             raise serializers.ValidationError(detail="Это резюме уже добавлено в закладку", code="Закладка создана")
    #     return data

class WishlistDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    wished_resume = ResumeSerializer()

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'wished_resume']