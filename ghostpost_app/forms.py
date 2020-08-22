from django import forms
from ghostpost_app.models import Ghostpost

thechoices = (("1", "BOAST"),
("2","ROAST"))

class Createghostpost(forms.Form):
    text = forms.CharField(max_length=280)
    isboast = forms.ChoiceField(choices=thechoices)
    

class Upvote(forms.Form):
    pass    