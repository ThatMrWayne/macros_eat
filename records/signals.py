from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from records.models import *
from utils.utils import RedisHash


@receiver(post_save, sender=Record, dispatch_uid="on_record_post_save")
def record_post_save(sender, instance, created, **kwargs):
    redis_client = RedisHash()
    hash_key = f"my-record-{instance.user_id}"
    field_key = f"{instance.user_id}-{int(instance.created_at.timestamp()*1000)}"
    redis_client.hdel(hash_key, field_key)


@receiver(post_save, sender=Intakes, dispatch_uid="on_intake_post_save")
def intake_post_save(sender, instance, created, **kwargs):
    redis_client = RedisHash()
    record = instance.record
    record_timestamp = int(record.created_at.timestamp()*1000)
    hash_key = f"my-record-{record.user_id}"
    field_key = f"{record.user_id}-{record_timestamp}"
    redis_client.hdel(hash_key, field_key)


@receiver(post_delete, sender=Intakes)
def intake_post_delete(sender, instance, *args, **kwargs):
    redis_client = RedisHash()
    record = instance.record
    record_timestamp = int(record.created_at.timestamp()*1000)
    hash_key = f"my-record-{record.user_id}"
    field_key = f"{record.user_id}-{record_timestamp}"
    redis_client.hdel(hash_key, field_key)
