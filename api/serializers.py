import re
from rest_framework import serializers
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from rest_framework.reverse import reverse

from .models import Shorterlink


class ShortlinkSerializer (serializers.ModelSerializer):
    link = serializers.URLField(
        validators=[URLValidator()],
        error_messages={
            'invalid': 'Don\'t forget to include the protocol http:// or https://'
        }
    )

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
