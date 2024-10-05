from django import forms

class NewPageForm(forms.Form):
    title = forms.CharField(label="Enter the title", required=True)
    content = forms.CharField(label="Content", widget=forms.Textarea(), required=True)
