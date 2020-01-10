from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

# Create your models here.

class Tag(models.Model):
    """Model definition for Tag."""

    name = models.CharField(verbose_name="Nome", max_length=50, unique=True)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.name


class Post(models.Model):
    """Model definition for Post."""

    title = models.CharField(verbose_name="Titulo", max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True)
    summary = models.TextField(verbose_name="Resumo")
    image = models.FileField(upload_to='uploads/%Y/%m/%d/')
    content =  RichTextField(verbose_name="Conteúdo")
    tags = models.ManyToManyField(Tag, related_name="tags")
    public = models.BooleanField(verbose_name="Postagem pública", default=False)
    created_at = models.DateField(verbose_name="Postado em", auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']
    
    def get_related(self):
        related = Post.objects.filter(tags__in=self.tags.all())
        return related

    def __str__(self):
        """Unicode representation of Post."""
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, verbose_name="Autor")
    email = models.EmailField(verbose_name="E-mail")
    body = models.TextField(verbose_name="Conteúdo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Comentado em")
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Subscriber(models.Model):
    """Model definition for subscriber."""

    email = models.EmailField(verbose_name="E-mail", unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        """Meta definition for subscriber."""

        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        """Unicode representation of subscriber."""
        return self.email

    def unsubscribe(self):
        self.active = False
