from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "Blog Newest Post"
    link = "/rss/feed"
    description = "Best Blog Ever!"

    def items(self):
        return Post.objects.filter(status=True)

    def item_title(self, item):
        return item.title # pyright: ignore[reportAttributeAccessIssue]

    def item_description(self, item):
        return item.content[:100]  # pyright: ignore[reportAttributeAccessIssue]

    