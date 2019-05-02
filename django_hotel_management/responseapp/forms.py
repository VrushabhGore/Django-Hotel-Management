
from django import forms

YEARS= [x for x in range(1940,2021)]

ROOM_CHOICES= [
    ('single', 'Single'),
    ('double', 'Double'),
    ('Family', 'Family'),
    ('Multiple', 'Multiple'),
    ]

class MyForm(forms.Form):
 name = forms.CharField(label='Enter your name', max_length=100)
 email = forms.EmailField(label='Enter your email', max_length=100)
 favorite_room= forms.CharField(label='What Room are you interested in?', 	  widget=forms.Select(choices=ROOM_CHOICES))
 checkin_date= forms.DateField(label='What day are you checking in?', widget=forms.SelectDateWidget(years=YEARS))
 checkout_date= forms.DateField(label='What date are you checking out?', widget=forms.SelectDateWidget(years=YEARS))
 feedback = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }))


