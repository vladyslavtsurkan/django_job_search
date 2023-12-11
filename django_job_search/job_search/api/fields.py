from rest_framework import serializers


class SlugRelatedCreationField(serializers.SlugRelatedField):
    """Custom SlugRelatedField for creating non-existent objects."""
    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            instance, _ = queryset.get_or_create(**{self.slug_field: data})
            return instance
        except (TypeError, ValueError):
            self.fail('invalid')
