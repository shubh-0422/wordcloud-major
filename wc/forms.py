from django import forms


class textInput(forms.Form):
	text = forms.CharField(label = 'text', widget=forms.Textarea)
	typechoices = [('Type1','Square shape'), ('Type2','Heart shape'), ('Type3','Dimond shape')]
	maskType = forms.CharField(label = 'Type', widget = forms.RadioSelect(choices = typechoices))
