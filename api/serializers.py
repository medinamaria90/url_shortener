
from rest_framework import serializers

from .models import Shorterlink


class ShortlinkSerializer (serializers.ModelSerializer):

    class Meta:
        model = Shorterlink
        fields = [
            'pk',
            'clicks',
            'last_click',
            'user',
            'link',
            'short_link',
            'expiration',
        ]
        read_only_fields = ['short_link', 'expiration', 'user']
