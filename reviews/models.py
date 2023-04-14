from django.db import models
from django.conf import settings
# Create your models here.

class Review(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    title   = models.CharField(max_length=50)
    content = models.TextField(null=False)
    movie   = models.CharField(max_length=50)
    image   = models.ImageField(upload_to='image/', null=True, blank=True)
    rating = models.FloatField()

    def half_star_rating(self):
        # 반올림한 별점 값을 구함
        rounded_rating = round(self.rating * 2) / 2

        # 별점 반개 문자열을 반환
        return '★' * int(rounded_rating) + '☆' * (rounded_rating % 1 == 0.5)

class Comment(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review  = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField(null=False)