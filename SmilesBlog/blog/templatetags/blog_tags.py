from __future__ import unicode_literals
from django.utils.safestring import mark_safe
from django.db.models import Count
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

from ..models import Post

import markdown
import bleach

ALLOWED_TAGS = [
    'h1','h2','h3','h4','h5','h6',
    'p','dl','dt','dd','ul','ol','li',
    'table', 'thead', 'th', 'tr','td', 'tbody',
    'b','i','strong','em','tt',
    'span','div','blockquote','code','pre',
    'hr','br',
    'a','img',
    'abbr',
    'acronym',
    'br',
]

ALLOWED_ATTRIBUTES = {
    '*': ['class', 'id'],
    'a': ['href', 'title'],
    'abbr': ['title'],
    'acronym': ['title'],
    'img': ['src', 'alt'],
}

MONTH_NAMES = (
    '',
    'January',
    'Feburary',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December')


@register.simple_tag  #Processes the data and returns a string - add (e.g. name='my_tag')
def total_posts():
    return Post.published.count()

# an inclusion_tag can render a template with context variable returned by your template tag
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish') [:count]
    return {'latest_posts': latest_posts}

@register.inclusion_tag('blog/post/list_title.html')
def show_all_posts():
    all_posts = Post.published.all().order_by('-publish')
    return {'all_posts': all_posts}

def create_archive_data(posts):
    archive_data = []
    count = {}
    mcount = {}
    for post in posts:
        year = post.publish.year
        month = post.publish.month
        if year not in count:
            count[year] = 1
            mcount[year] = {}
        else:
            count[year] += 1
        if month not in mcount[year]:
            mcount[year][month] = 1
        else:
            mcount[year][month] += 1
    for year in sorted(count.keys(), reverse=True):
        archive_data.append({'isyear': True,
                             'year': year,
                             'count': count[year],
                             })
        for month in sorted(mcount[year].keys(), reverse=True):
            archive_data.append({'isyear': False,
                                 'yearmonth': '%d/%02d' % (year, month),
                                 'monthname': MONTH_NAMES[month],
                                 'count': mcount[year][month],})
    return archive_data

@register.inclusion_tag('blog/post/posts_per_years.html')
def show_posts_per_year():
    posts = Post.published.all()
    archive_data = create_archive_data(posts)
    return {'posts':posts, 'archive_counts':archive_data,}

#add the most commented posts
@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]

#use markdown sintax in my blog posts and convert the post contents to html
# @register.filter(name='markdown')
# def markdown_format(text):
#     return mark_safe(markdown.markdown(text))

@register.filter(is_safe=True, name='markdown')
def mrkdown(value):
    html = bleach.linkify(bleach.clean(markdown.markdown(value,
    ['markdown.extensions.extra',
     'markdown.extensions.admonition',
     'markdown.extensions.tables',
     'markdown.extensions.toc(permalink=True)']),
     tags=ALLOWED_TAGS,
     attributes=ALLOWED_ATTRIBUTES))
    return mark_safe(html)
