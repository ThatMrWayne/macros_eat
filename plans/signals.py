from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from plans.models import *
from utils.utils import RedisHash


@receiver(post_save, sender=Plan, dispatch_uid="on_plan_post_save")
def plan_post_save(sender, instance, created, **kwargs):
    if not created:
        redis_client = RedisHash()
        hash_key = f"my-plan-{instance.user_id}"
        redis_client.delete(hash_key)


@receiver(post_delete, sender=Plan)
def plan_post_delete(sender, instance, *args, **kwargs):
    redis_client = RedisHash()
    hash_key = f"my-plan-{instance.user_id}"
    redis_client.delete(hash_key)
