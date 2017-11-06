from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from .models import Post
from .forms import EmailPostForm

def post_list(request):
    """Create a list of posts"""
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliverr te first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page oof results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  { 'page': page,
                    'posts': posts})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    """Create a view that displays the single post"""
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

def  post_share(request, post_id):
    # Retrieve posts by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # form was submitted if we get a POST request,
        # we assume if I get a GET request an empty form has to be displayed
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation, I can see validation errors
            # by accessing form.errors
            cd = form.cleaned_data
            # if the form data does not validaatee the cleaned_data will
            # have only the valid fields. it is a dictionary of form fields
            # and their values.
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends your reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'mn.sabatino@gmail.com', [cd['to']])
            sent = True
        else:
            form = EmailPostForm()
        return render(request, 'blog/post/share.html', {'post': post,
                                                        'form': form,
                                                        'sent': sent})
