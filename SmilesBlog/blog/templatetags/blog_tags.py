from django import template

register = template.Library()

from ..models import Post

@register.simple_tag  #Processes the data and returns a string - add (e.g. name='my_tag')
def total_posts():
    return Post.published.count()

# an inclusion_tag ca render a template with context variable returned by your template tag
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish') [:count]
    return {'latest_posts': latest_posts}
