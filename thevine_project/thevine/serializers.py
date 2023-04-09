from rest_framework import serializers

from .models import Wine, Rating, User

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    wine = serializers.HyperlinkedRelatedField(
        view_name='wine_detail',
        read_only=True
    )

    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    wine_url = serializers.PrimaryKeyRelatedField(
        queryset=Wine.objects.all(),
        source='wine'
    )

    user_url = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )
    class Meta:
        model = Rating
        fields = ('id', 'wine', 'wine_url', 'user', 'user_url', 'user_id', 'wine_id', 'rating', 'review', 'taste', 'notes')

class WineSerializer(serializers.HyperlinkedModelSerializer):
    ratings = RatingSerializer(
        many=True,
        read_only=True
    )

    wine_url = serializers.ModelSerializer.serializer_url_field(
        view_name='wine_detail'
    )

    class Meta:
        model = Wine
        fields = ('id', 'wine_url', 'ratings', 'producer', 'vintage', 'grape', 'area', 'image', 'rated', 'wine_type')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    ratings = RatingSerializer(
        many=True,
        read_only=True
    )

    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail'
    )
    class Meta:
        model = User
        fields = ('id', 'user_url', 'ratings', 'username', 'email', 'password', 'location')