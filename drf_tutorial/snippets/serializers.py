from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
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
        owner(ReadOnlyField): creator of the code snippet
        highlight(HyperlinkedIdentityField): hyperlinked relationship to
                                             highlighted snippet
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight',
                                                     format='html')
    
    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'title', 'code', 
                  'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Users.

    Fields:
        id: pk of user
        username: user's username
        snippets: list of snippets associated with user
    """
    snippets = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='snippet-detail',
                                                   read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
