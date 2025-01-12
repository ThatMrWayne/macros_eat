from datetime import datetime, timezone
from django.db.models import Q


def convert_timestamp_to_utc_datetime(milli_timestamp):
    if isinstance(milli_timestamp, str):
        milli_timestamp = int(milli_timestamp)
    return datetime.fromtimestamp(milli_timestamp / 1000, tz=timezone.utc)


class CursorPaginator:
    def __init__(self, queryset, page_size, ordering_field):
        self.queryset = queryset.order_by(ordering_field)
        self.page_size = int(page_size)
        self.order_attr = ordering_field.lstrip("-")
        self.is_reversed = ordering_field.startswith("-")

    def __iter__(self):
        self._get_page_data(self.queryset)
        while self._has_next:
            yield self._current_page_data
            queryset = self._get_positional_queryset(self._current_page_data[-1])
            self._get_page_data(queryset)

    def _get_page_data(self, queryset):
        self._current_page_data = list(queryset[: self.page_size])
        self._has_next = False if not self._current_page_data else True

    def _get_position_from_instance(self, instance):
        if isinstance(instance, dict):
            attr = instance[self.order_attr]
        else:
            attr = getattr(instance, self.order_attr)
        return attr

    def _get_positional_queryset(self, instance):
        paginated_position = self._get_position_from_instance(instance)
        filter_query = (
            Q(**{self.order_attr + "__lt": paginated_position})
            if self.is_reversed
            else Q(**{self.order_attr + "__gt": paginated_position})
        )
        return self.queryset.filter(filter_query)
