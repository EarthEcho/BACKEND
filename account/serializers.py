from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model
from .validators import validate_password, validate_user_password


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        required=True,
        validators=[validate_user_password, validate_password],
        help_text='''   Password must be at least 8
                        characters long.
                        password must contain a letter, caps, number
                        and symbol
                    '''
    )
    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
            'is_active',
            'is_staff',
            'is_superuser',
            'date_joined',
            'fullname',
            'last_login',

        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

        read_only_fields = (
            'id',
            'date_joined',
            'last_login',
            'is_staff',
            'is_superuser',
            'is_active',
            'fullname',
            'shortname'
        )

    def get_fullname(self, obj):
        if hasattr(obj, 'id'):
            return obj.get_full_name()
        return None

    def validate(self, attrs):

        query = User.objects.filter(email__iexact=attrs['email'])

        if query.exists():
            raise serializers.ValidationError(
                {'Email': "Invalid Email, use another."}
            )

        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {"Password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        del validated_data['confirm_password']
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializerInline(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'is_superuser',
            'date_joined',
            'fullname',
            'last_login',

        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

        read_only_fields = (
            'date_joined',
            'last_login',
            'is_staff',
            'is_superuser',
            'is_active',
            'fullname',
        )

    def get_fullname(self, obj):
        if hasattr(obj, 'id'):
            return obj.get_full_name()
        return None


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializerInline()

    class Meta:
        model = Profile
        fields = (
            'user',
            'id',
            'bio',
            'location',
            'avatar_url',
            'updated',
            'created'
        )

    def update(self, instance, validated_data):
        users_data = validated_data.pop('user')
        user = instance.user

        instance.bio = validated_data.get('bio', instance.bio)
        instance.location = validated_data.get('location', instance.location)
        instance.avatar_url = validated_data.get(
            'avatar_url', instance.avatar_url)
        instance.save()

        user.email = users_data.get('email', user.email)
        user.first_name = users_data.get('first_name', user.first_name)
        user.last_name = users_data.get('last_name', user.last_name)
        user.username = users_data.get('username', user.username)
        user.save()
        return instance
