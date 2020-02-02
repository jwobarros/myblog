from django.test import TestCase
from model_mommy import mommy   
from blog.models import Post, Tag, Comment, Subscriber
# Create your tests here.

class TagTestCase(TestCase):
    def setUp(self):
        self.django_tag = mommy.make(Tag, name="Django")
        self.python_tag = mommy.make(Tag, name="Python")

    def test_tag_creation(self):
        """Test Tag creation"""
        self.assertEqual(self.django_tag.__str__(), 'Django')
        self.assertEqual(self.python_tag.__str__(), 'Python')


class PostTestCase(TestCase):
    def setUp(self):
        self.tag = mommy.make(Tag, name="Django")
        self.post = mommy.make(Post, title="Django project")
        self.post.tags.set([self.tag])
    
    def test_post_creation(self):
        """Test post creation"""
        self.assertEqual(self.post.title, 'Django project')

class CommentTestCase(TestCase):
    def setUp(self):
        self.tag = mommy.make(Tag, name="Django")
        self.post = mommy.make(Post, title="Django")
        self.post.tags.set([self.tag])
        self.comment = mommy.make(Comment, 
            post=self.post,
            name="Johnnatan Barros",
            email="johnnatan.barros@outlook.com",
            body="Testing comment model."
        )

    def test_comments_creation(self):
        """Test Tag creation"""
        self.assertEqual(self.comment.name, 'Johnnatan Barros')
        self.assertEqual(self.comment.email, 'johnnatan.barros@outlook.com')
        self.assertEqual(self.comment.body, 'Testing comment model.')


class SubscriberTestCase(TestCase):
    def setUp(self):
        self.subscriber = mommy.make(Subscriber, email="johnnatan.barros@outlook.com")

    def test_subscription(self):
        """Test subscription"""
        self.assertEqual(self.subscriber.active, True)

    def test_unsubscription(self):
        """Test unsubscription"""
        self.subscriber.unsubscribe()
        self.assertEqual(self.subscriber.active, False)