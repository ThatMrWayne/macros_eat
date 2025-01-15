from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from food.models import *
from utils.utils import RedisHash


@receiver(post_save, sender=Food, dispatch_uid="on_food_post_save")
def food_post_save(sender, instance, created, **kwargs):
    redis_client = RedisHash()
    hash_key = f"my-food-{instance.user_id}"
    redis_client.delete(hash_key)


@receiver(post_delete, sender=Food)
def food_post_delete(sender, instance, *args, **kwargs):
    redis_client = RedisHash()
    hash_key = f"my-food-{instance.user_id}"
    redis_client.delete(hash_key)
