from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Post, Comment

class PostModelTests(TestCase):
    def test_post_creation(self):
        user = User(0)
        post = Post.objects.create(
            title = "Test Post number 1",
            slug = "test-post-number-1",
            author = user,
            body = "Description of the Post test..."
        )
        now = timezone.now()
        self.assertLess(post.created, now)
        self.assertLess(post.publish, now)
        self.assertLess(post.updated, now)

class CommentModelTests(TestCase):
    def test_comment_creation(self):
        user = User(0)
        post = Post.objects.create(
            title = "Test Post number 1",
            slug = "test-post-number-1",
            author = user,
            body = "Description of the Post test..."
        )
        comment = Comment.objects.create(
            post = post,
            name = "CiaBella",
            email = "ciabella@gmail.com",
            body = "Great post..",
            active = True
        )
        now = timezone.now()
        self.assertLess(comment.created, now)
        self.assertLess(comment.updated, now)
