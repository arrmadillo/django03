from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/index.html', context)


@login_required
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form' : form,
    }
    return render(request, 'reviews/create.html', context)


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    count = comments.count()
    context = {
        'review': review,
        'comments': comments,
        'comment_form': comment_form,
        'count': count,
    }
    return render(request, 'reviews/detail.html', context)


@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        if request.method == "POST":
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                form.save()
                return redirect('reviews:detail', review_pk)
        else:
            form = ReviewForm(instance=review)
    else:
        return redirect('reviews:index')
    context = {
        'review': review,
        'form': form,
    }
    return render(request, 'reviews/update.html', context)


@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('reviews:index')


# 댓글생성
@login_required
def create_comment(request, review_pk):
    if request.method == 'POST':
        review = Review.objects.get(pk=review_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return redirect('reviews:detail', review_pk)
        else:
            # 유효성
            context = {
                'review': review,
                'comment_form': comment_form,
            }
            return render(request,'reviews/detail.html', context)


# 댓글삭제
@login_required
def delete_comment(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.user == comment.user:
        comment.delete()

    return redirect('reviews:detail', review_pk)


@require_POST
def likes(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
        else:
            review.like_users.add(request.user)
        return redirect('reviews:detail', review_pk)
    return redirect('accouts:login')