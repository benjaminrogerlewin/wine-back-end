from rest_framework import serializers

from .models import Wine, Rating, User

class WineSerializer(serializers.HyperlinkedModelSerializer):
    ratings = serializers.HyperlinkedRelatedField(
        view_name='rating_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Wine
        fields = ('id', 'ratings', 'producer', 'vintage', 'grape', 'area', 'image', 'rated', 'wine_type')

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    wine = serializers.HyperlinkedRelatedField(
        view_name='wine_detail',
        read_only=True
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    class Meta:
        model = Rating
        fields = ('id', 'wine', 'user', 'user_id', 'wine_id', 'rating', 'review', 'taste', 'notes')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    ratings = serializers.HyperlinkedRelatedField(
        view_name='rating_detail',
        read_only=True
    )
    class Meta:
        model = Rating
        fields = ('id', 'ratings', 'username', 'email', 'password', 'location')