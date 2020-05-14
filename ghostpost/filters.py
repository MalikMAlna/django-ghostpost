import django_filters
from .models import Post


class PostFilter(django_filters.FilterSet):

    POST_TYPE_CHOICES = (
        ('boasts', 'Boasts'),
        ('roasts', 'Roasts'),
    )

    POST_KARMA_CHOICES = (
        ('most_karma', 'Most Karma'),
        ('least_karma', 'Least Karma'),
    )

    ordering_b_or_r = django_filters.ChoiceFilter(
        label="Post Type",
        choices=POST_TYPE_CHOICES,
        method="filter_by_post_type",
    )

    ordering_karma = django_filters.ChoiceFilter(
        label="Total Karma",
        choices=POST_KARMA_CHOICES,
        method='filter_by_total_karma',
    )

    class Meta:
        model = Post
        fields = {'content': ['icontains'], }

    def filter_by_post_type(self, queryset, name, value):
        if value == 'boasts':
            expression = Post.objects.filter(b_or_r=True)
        elif value == 'roasts':
            expression = Post.objects.filter(b_or_r=False)
        return expression

    def filter_by_total_karma(self, queryset, name, value):
        for post in Post.objects.all():
            post.total_votes = post.up_vote + post.down_vote
            if value == 'most_karma':
                expression = Post.objects.filter(up_vote=post.up_vote)
            elif value == 'least_karma':
                expression = Post.objects.filter(down_vote=post.down_vote)
        return expression
