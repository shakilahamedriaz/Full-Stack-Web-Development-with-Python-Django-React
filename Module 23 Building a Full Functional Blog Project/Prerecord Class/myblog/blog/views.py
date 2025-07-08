from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Tag, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import postForm, commentForm
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import PostForm, CommentForm


# Create your views here.
#post list view
def post_list(request):
    # category, tag, searching, pagination --> post dekhate hobe
    categoryQ = request.GET.get('category')
    tagQ = request.GET.get('tag')
    searchQ = request.GET.get('q')

    posts = Post.objects.all()

    if categoryQ:
        posts = posts.filter(category__name = categoryQ)
    if tagQ:
        posts = posts.filter(tag__name = tagQ)
    if searchQ:
        posts = posts.filter(
            Q(title__icontains = searchQ)
        | Q(content__icontains = searchQ)
        | Q(tag__name__icontains = searchQ)
        | Q(category__name__icontains = searchQ)
        ).distinct()
    

    #pagination
    paginator = Paginator(posts, 2) # per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj" : page_obj,
        "categories" : Category.objects.all(),
        "tags" : Tag.objects.all(),
        'search_query' : searchQ,
        'category_query' : categoryQ,
        'tag_query' : tagQ,
    }
    return render(request, 'blog/post_list.html', context)



def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # database e save hobe na
            comment.post = post
            comment.author = request.user
            comment.save() # database e save hobe
            return redirect('', id=post.id)
    else:
        comment_form = CommentForm()

    comments = post.comment_set.all().order_by('-created_at')
    is_liked = post.liked_users.filter(id=request.user.id).exists()
    like_count = post.liked_users.count()

    context = {
        'post': post,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'comments': comments,
        'comment_form': comment_form,
        'is_liked': is_liked,
        'like_count': like_count,
    }
    post.view_count += 1
    post.save()

    return render(request, 'blog/post_details.html', context)