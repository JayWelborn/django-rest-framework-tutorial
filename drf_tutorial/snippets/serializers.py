from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    """
    Serializer for Snippets.

    Serializers are used for encoding native Python objects to JSON, and parsing
    JSON into a native python object. They will be used by our web API to encode
    data for and receive data from our front end. Serializers function similarly
    to django forms.
    
    Fields:
        id(IntegerField): pk of snippet was created
        title(CharField): title of code snippet
        code(TextField): field for housing the actual code
        linenos(BooleanField): should the output display line numbers?
        language(CharField): language for highlighting. default is python.
        style(CharField): how to display code. defaults to friendly
    """
    
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
