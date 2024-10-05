from django import forms

class NewPageForm(forms.Form):
    title = forms.CharField(label="Enter the title", required=True)
    content = forms.CharField(label="Content", widget=forms.Textarea(), required=True)


class EditPageForm(forms.Form):
    title = forms.CharField(label="Edit the title", required=False)
    content = forms.CharField(label="Edit the content", widget=forms.Textarea(), required=False)
