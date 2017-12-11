import datetime
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

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
            #publish = datetime.datetime.today()
        )
        self.post2 = Post.objects.create(
            title = "Test Post number 2",
            slug = "test-post-number-1",
            author = self.user,
            body = "Description of the Post test 2..."
            #publish = datetime.datetime.today()
        )
        self.comment = Comment.objects.create(
            post = self.post,
            name = "CiaBella",
            email = "ciabella@gmail.com",
            body = "Great post..",
            active = True
        )
        self.now = timezone.now()

    def test_blog_list_view(self):
        resp = self.client.get(reverse('blog:post_list'))
        self.assertEqual(resp.status_code, 200)
        #self.assertEqual(self.post, resp.context['posts'])
        #self.assertIn(self.post2, resp.context['posts'])
