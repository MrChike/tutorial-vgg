from django.db import models  # Tut 1 - Serialization
from pygments.lexers import get_all_lexers  # Tut 1 - Serialization
from pygments.styles import get_all_styles  # Tut 1 - Serialization
from pygments.lexers import get_lexer_by_name  # Tut 4, Step 1 - Auth & Perm
from pygments.formatters.html import HtmlFormatter  # Tut 4, Step 1 - Auth & Perm
from pygments import highlight  # Tut 4, Step 1 - Auth & Perm

# Tut 1 - Serialization
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0])
                           for item in LEXERS])  # Tut 1 - Serialization
STYLE_CHOICES = sorted([(item, item)
                        for item in get_all_styles()])  # Tut 1 - Serialization


class Snippet(models.Model):  # Tut 1 - Serialization
    created = models.DateTimeField(auto_now_add=True)  # Tut 1 - Serialization
    title = models.CharField(max_length=100, blank=True,
                             default='')  # Tut 1 - Serialization
    code = models.TextField()  # Tut 1 - Serialization
    linenos = models.BooleanField(default=False)  # Tut 1 - Serialization
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)  # Tut 1 - Serialization
    # Tut 1 - Serialization
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly', max_length=100)
    # Tut 4, Step 1 - Auth & Perm
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:  # Tut 1 - Serialization
        ordering = ['created']  # Tut 1 - Serialization

    # Tut 4, Step 1 - Auth & Perm
    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
