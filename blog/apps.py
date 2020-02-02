from django.apps import AppConfig
from watson import search as watson

class BlogConfig(AppConfig):
    name = 'blog'
    def ready(self):
        Post = self.get_model("Post")
        watson.register(Post)
