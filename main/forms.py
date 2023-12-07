from django import forms

from main.models import Product, Version


class ProductFrom(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'image_preview', 'category', 'price')

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


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

