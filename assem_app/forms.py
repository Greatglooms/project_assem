from django import forms

WORD_CHOICES=[
    ('Русское радио', 'Русское радио'),
    ('Казахское радио', 'Казахское радио'),
    ('Радио FM', 'Радио FM'),
    ('Той-думан', 'Той-думан'),
    ('Ретро радио', 'Ретро радио'),
    ('Europa +', 'Europa +'),
]

COLOR_CHOICES=[
    ('Каждый', 'Каждый'),
    ('Охотник', 'Охотник'),
    ('Желает', 'Желает'),
    ('Знать', 'Знать'),
    ('Где', 'Где'),
    ('Сидит', 'Сидит'),
    ('Фазан', 'Фазан'),
]

class RadioForm(forms.Form):
    word_choice = forms.ChoiceField(choices=WORD_CHOICES, widget=forms.RadioSelect)

class Rainbow(forms.Form):
    color_choice = forms.ChoiceField(choices=COLOR_CHOICES, widget=forms.RadioSelect)