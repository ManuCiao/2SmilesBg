from django import template

register = template.Library()

from ..models import Post

@register.simple_tag  #Processes the data and returns a string - add (e.g. name='my_tag')
def total_posts():
    return Post.published.count()
