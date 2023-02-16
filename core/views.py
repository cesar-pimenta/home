from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm
# Create your views here.
from django.core.mail import send_mail

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'core/post/list.html', {'page':page,'posts':posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    # List of similar posts
    # post_tags_ids = post.tags.values_list('id', flat=True)
    # similar_posts = Post.published.filter(tags__in=post_tags_ids)\
    #                               .exclude(id=post.id)
    # similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
    #                             .order_by('-same_tags','-publish')[:4]

    return render(request,
                  'core/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                #    'similar_posts': similar_posts
                })


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            try:
                send_mail(subject, message, 'cesar-pimenta@live.com', [cd['to']])
                sent = True
            except:
                sent = True
    else:
        form = EmailPostForm()
        
    return render(request, 'core/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})