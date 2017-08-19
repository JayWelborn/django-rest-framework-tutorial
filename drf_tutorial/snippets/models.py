# django imports
from django.db import models

# 3rd-party imports
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

# define pygment stuff
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.

class Snippet(models.Model):
    """
    Model for storing code snippets.

    Attributes:
        created(DateTimeField): date snippet was created
        title(CharField): title of code snippet
        code(TextField): field for housing the actual code
        linenos(BooleanField): should the output display line numbers?
        language(CharField): language for highlighting. default is python.
        style(CharField): how to display code. defaults to friendly.
        owner(ForeignKey): creator of the snippet
        highlighted(TextField): highlighted HTML representation of the code
    """

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, 
                                default='python', 
                                max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, 
                             default='friendly', 
                             max_length=100)

    owner = models.ForeignKey('auth.User',
                              related_name='snippets',
                              on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos = linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
        
            
