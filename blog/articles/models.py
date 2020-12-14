from django.db import models

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='d')
    thumbnail = models.ImageField(default='default.png', blank=True)
    # add thumbnail later
    # add author later

    def __str__(self):
        return self.title

    def snippit(self):
        return self.body[:47] + "..." if len(self.body) > 50 else self.body[:50]
