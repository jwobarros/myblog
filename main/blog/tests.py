from django.test import TestCase
from blog.models import Post, Tag, Comment, Subscriber
# Create your tests here.

class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="Django")
        Tag.objects.create(name="Python")

    def test_tag_creation(self):
        """Test Tag creation"""
        django = Tag.objects.get(name="Django")
        python = Tag.objects.get(name="Python")
        self.assertEqual(django.__str__(), 'Django')
        self.assertEqual(python.__str__(), 'Python')


class PostTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="Django")
        django_tag = Tag.objects.get(name="Django")
        Post.objects.create(
            title="Django",
            summary="Como iniciar seus projetos usando Django.",
            image="C:\\Users\\johnnatan.barros\\Pictures\\IMG_0628.jpeg",
            content="Como iniciar seus projetos usando Django.",
        ).tags.set([django_tag])

    def test_post_creation(self):
        """Test post creation"""
        django_post = Post.objects.get(title="Django")
        self.assertEqual(django_post.title, 'Django')
        self.assertEqual(django_post.summary, 'Como iniciar seus projetos usando Django.')
        self.assertEqual(django_post.content, 'Como iniciar seus projetos usando Django.')


class CommentTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="Django")
        Tag.objects.create(name="Python")

        django_tag = Tag.objects.get(name="Django")
        python_tag = Tag.objects.get(name="Python")

        Post.objects.create(
            title="Django",
            summary="Como iniciar seus projetos usando Django.",
            image="C:\\Users\\johnnatan.barros\\Pictures\\IMG_0628.jpeg",
            content="Como iniciar seus projetos usando Django.",
        ).tags.set([django_tag, python_tag])

        post = Post.objects.get(title="Django")
        
        Comment.objects.create(
            post=post,
            name="Johnnatan Barros",
            email="johnnatan.barros@outlook.com",
            body="Testing comment model."
        )
        

    def test_comments_creation(self):
        """Test Tag creation"""
        comment = Comment.objects.get(name="Johnnatan Barros")        
        self.assertEqual(comment.name, 'Johnnatan Barros')
        self.assertEqual(comment.email, 'johnnatan.barros@outlook.com')
        self.assertEqual(comment.body, 'Testing comment model.')


class SubscriberTestCase(TestCase):
    def setUp(self):
        Subscriber.objects.create(email="johnnatan.barros@outlook.com")

    def test_subscription(self):
        """Test subscription"""
        subscriber = Subscriber.objects.get(email="johnnatan.barros@outlook.com")
        self.assertEqual(subscriber.active, True)

    def test_unsubscription(self):
        """Test unsubscription"""
        subscriber = Subscriber.objects.get(email="johnnatan.barros@outlook.com")
        subscriber.unsubscribe()
        self.assertEqual(subscriber.active, False)