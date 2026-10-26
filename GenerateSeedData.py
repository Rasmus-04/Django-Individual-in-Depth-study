
import os
import django
import random
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import Post

def random_date():
    now = timezone.now()
    days_ago = random.randint(0, 30)
    random_time = timedelta(
        days=days_ago,
        seconds=random.randint(0, 86400)
    )
    return now - random_time

posts = [
    {
        "user_id": "user1",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "status": "Published",
    },
    {
        "user_id": "user2",
        "text": "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "status": "Published",
    },
    {
        "user_id": "user3",
        "text": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",
        "status": "Draft",
    },
    {
        "user_id": "user4",
        "text": "Duis aute irure dolor in reprehenderit in voluptate velit esse.",
        "status": "Published",
    },
    {
        "user_id": "user5",
        "text": "Excepteur sint occaecat cupidatat non proident, sunt in culpa.",
        "status": "Draft",
    },
    {
        "user_id": "user1",
        "text": "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio.",
        "status": "Published",
    },
    {
        "user_id": "user2",
        "text": "Nullam varius, turpis et commodo pharetra, est eros bibendum.",
        "status": "Published",
    },
    {
        "user_id": "user3",
        "text": "Praesent dapibus, neque id cursus faucibus, tortor neque egestas.",
        "status": "Draft",
    },
    {
        "user_id": "user4",
        "text": "Fusce pellentesque suscipit nibh. Integer vitae libero ac risus.",
        "status": "Published",
    },
    {
        "user_id": "user5",
        "text": "Vestibulum commodo felis quis tortor. Ut aliquam sollicitudin leo.",
        "status": "Published",
    },
]

for post_data in posts:
    created_date = random_date()

    post = Post.objects.create(**post_data)

    Post.objects.filter(pk=post.pk).update(
        created_date=created_date,
        last_edited_date=created_date
    )

print(f"Created {len(posts)} posts successfully!")

