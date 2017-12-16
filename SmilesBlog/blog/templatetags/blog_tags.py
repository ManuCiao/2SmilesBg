from django.utils.safestring import mark_safe
from django.db.models import Count
from django import template

register = template.Library()

from ..models import Post

import markdown

@register.simple_tag  #Processes the data and returns a string - add (e.g. name='my_tag')
def total_posts():
    return Post.published.count()

# an inclusion_tag ca render a template with context variable returned by your template tag
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish') [:count]
    return {'latest_posts': latest_posts}

#add the most commented posts
@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


#use markdown sintax in my blog posts and convert the post contents to html
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
