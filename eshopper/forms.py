from django import forms

class LoginForm(forms.Form):
	email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
	'placeholder':'EMAIL'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
	'placeholder':'PASSWORD',}))

class SignupForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
	'placeholder':'NAME'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
	'placeholder':'USERNAME'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
	'placeholder':'EMAIL'}))
	phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
	'placeholder':'PHONE NUMBER'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
	'placeholder':'PASSWORD',"autocomplete":"new-password"}))
	repassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
	'placeholder':'CONFIRM PASSWORD',}))


class AddProperty(forms.Form):
	property_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-3',
	'placeholder':'PROPERTY NAME'}))
	property_description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mb-3',
	'placeholder':'PROPERTY DESCRIPTION','rows':'6','maxlength':'1000','style':'min-width: 100%'}))
	property_rent =  forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control mb-3',
	'placeholder':'ENTER THE RENT'}))
	property_address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mb-3',
	'placeholder':'PROPERTY ADDRESS','rows':'8','maxlength':'3000','style':'min-width: 100%'}))
	property_landmark = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3',
	'placeholder':'NEAREST LANDMARK'}))
	image_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,
	'class':'form-control-file'}))

# class AddPropertyImages(forms.Form):
