from django import forms


class Search_weblog(forms.Form):
    search_view = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'جستجو کنید...'})
    )
