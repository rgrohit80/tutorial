from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippet', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)


class Publishers(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Author(models.Model):
    a_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.a_name


class Book(models.Model):
    title = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publishers, related_name='pubs', on_delete=models.CASCADE)
    Author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


class team(models.Model):
    team_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    SPECA = (('TDS', 'Tech data stewards'),
             ('BAU', 'Business as usual'),
             ('ODS', 'Operational data store'))
    spec = models.CharField(max_length=50, choices=SPECA, default='others')

    def __str__(self):
        return self.team_name


class Resource(models.Model):
    name = models.CharField(max_length=50)
    team = models.ManyToManyField(team)
    level = [('12', 'ASE'), ('11', 'SE'), ('10', 'SSE')]
    LEVEL = models.CharField(max_length=50, choices=level, default='Others')
    Feedback = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name == 'Rohit':
            return 'you can not have him here'
        else:
            super().save(*args, **kwargs)


class Emp(Resource):
    local_name = models.CharField(max_length=50)
    sal = models.IntegerField()


class ParkingLot(models.Model):
    owner = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    space = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_num = models.TextField()
    type = (('small', 'car -bike - mini tesla'),
            ('medium', 'med trucks - water tanker'),
            ('big', 'trucks'))
    type = models.CharField(max_length=23, choices=type, default='others')

    def __str__(self):
        return self.vehicle_num


class Actor(models.Model):
    name = models.CharField(max_length=33, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    actor = models.ForeignKey('Actor', null=True, on_delete=models.SET_NULL)
    movie = models.CharField(max_length=44)
    director = models.CharField(max_length=22)

    def __str__(self):
        return self.movie


class Bookie(models.Model):
    bookie_id = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=33)
    help_text = "Please use the following format: <em>YYYY-MM-DD</em>."

    def __str__(self):
        return self.name    