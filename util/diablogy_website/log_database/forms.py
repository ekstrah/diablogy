from django import forms

CHOICES = (
    ('beta', 'Beta'),
    ('techfossguru', 'Techfossguru',)
)


class KeyspaceForm(forms.Form):
    keyspace = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices = CHOICES,
    )

