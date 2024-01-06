from django import forms

from main.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductFrom(StyleFormMixin, forms.ModelForm):

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        bad_word = ('казино', 'криптовалюта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')

        for word in bad_word:
            if cleaned_data.lower().find(word.lower()) != -1:
                raise forms.ValidationError(f'В наименовании использовано запрещенное слово: {word}')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        bad_word = ('казино', 'криптовалюта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')

        for word in bad_word:
            if cleaned_data.lower().find(word.lower()) != -1:
                raise forms.ValidationError(f'В описании использовано запрещенное слово: {word}')

        return cleaned_data


class ProductFromUser(ProductFrom):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image_preview', 'category', 'price')


class ProductFromModerator(ProductFrom):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

