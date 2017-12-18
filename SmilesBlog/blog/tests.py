from datetime import datetime
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import Post, Comment

class BlogModelTests(TestCase):
    def setUp(self):
        self.user = User(0)
        self.post = Post.objects.create(
            title = "Test Post number 1",
            slug = "test-post-number-1",
            author = self.user,
            body = "Description of the Post test..."
        )
        self.comment = Comment.objects.create(
            post = self.post,
            name = "CiaBella",
            email = "ciabella@gmail.com",
            body = "Great post..",
            active = True
        )
        self.now = timezone.now()

    def test_post_creation(self):
        self.assertEqual(str(self.post), self.post.title)

    def test_post_time_creation(self):
        self.assertLess(self.post.created, self.now)
        self.assertLess(self.post.publish, self.now)
        self.assertLess(self.post.updated, self.now)

    def test_comment_creation(self):
        self.assertLess(self.comment.created, self.now)
        self.assertLess(self.comment.updated, self.now)


class BlogViewTests(TestCase):
    def setUp(self):
        self.user = User(0)
        self.post = Post.objects.create(
            title = "Test Post number 1",
            slug = "test-post-number-1",
            author = self.user,
            body = "Description of the Post test 1..."
        )
        self.post2 = Post.objects.create(
            title = "Test Post number 2",
            slug = "test-post-number-1",
            author = self.user,
            body = "Description of the Post test 2..."
            publish = datetime.today()
        )
        self.comment = Comment.objects.create(
            post = self.post,
            name = "CiaBella",
            email = "ciabella@gmail.com",
            body = "Great post..",
            active = True
        )
        self.now = timezone.now()

    def test_homepage(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_blog_list_view(self):
        resp = self.client.get(reverse('blog:post_list'))
        self.assertEqual(resp.status_code, 200)
        #self.assertEqual(self.post, resp.context['posts'])
        #self.assertIn(self.post2, resp.context['posts'])
        #self.assertTemplateUsed(resp, 'blog/post/list.html')
        #self.assertContains(resp, self.post.title)

class HomePageTests(TestCase):
    """Test whether our blog entries show up on the homepage"""

    def setUp(self):
        self.user = get_user_model().objects.create(username='Mr-X')
        self.now = datetime.today()

    def test_one_user_entry(self):
        Post.objects.create(
                            title = "Test Post number 1",
                            slug = "test-post-number-1",
                            author = self.user,
                            body = "Description of the Post test 1..."
                            publish = self.now                           )
        resp = self.client.get('/self.now.year/self.now.month/self.now.day/self.post')
        self.assertContains(resp, 'Test Post number 1')
        self.assertContains(resp, 'Description of the Post test 1...')
        self.assertContains(resp, 'Published {0} by {1}'.format(publish, author))
