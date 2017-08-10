from res_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
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
    
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, 
                                  allow_blank=True, 
                                  max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, 
                                       default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES,
                                    default='frienly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, 
        given the validated data
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
