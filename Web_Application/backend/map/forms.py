from django import forms
from crispy_forms.helper import FormHelper

class SearchForm(forms.Form):
    search = forms.CharField(label='Search Place for recommendation', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'search'

class SearchCollaborativeForm(forms.Form):
    search = forms.CharField(label='Search Place for collaborative recommendation', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'search'