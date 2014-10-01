from djangotoolbox.fields import ListField
from django import forms


class GenreListField(forms.CharField):

    def prepare_value(self, value):
        return ', '.join(value)

    def to_python(self, value):
        if not value:
            return []
        return [item.strip() for item in value.split(',')]
