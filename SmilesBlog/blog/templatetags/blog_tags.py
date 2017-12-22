from django.utils.safestring import mark_safe
from django.db.models import Count
from django import template

register = template.Library()

from ..models import Post

import time
#from calendar import month_name
import markdown

@register.simple_tag  #Processes the data and returns a string - add (e.g. name='my_tag')
def total_posts():
    return Post.published.count()

# an inclusion_tag ca render a template with context variable returned by your template tag
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish') [:count]
    return {'latest_posts': latest_posts}

@register.inclusion_tag('blog/post/list_title.html')
def show_all_posts():
    all_posts = Post.published.all().order_by('-publish')
    return {'all_posts': all_posts}

@register.inclusion_tag('blog/post/posts_per_years.html')
def show_posts_per_year():
    post = Post.published.order_by("-publish")
    #year = post.publish.year
    year =  time.localtime()[:1][0]
    posts_per_year = post.filter(publish__year=year)
    return {'year':year, 'post_list_year':posts_per_year}

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
