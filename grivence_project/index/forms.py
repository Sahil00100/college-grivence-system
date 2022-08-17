from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from.models import Student
class UserForm(forms.Form):
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')
    numbers=RegexValidator(r'^[0-9]*$','only numbers allowed')
    #form elements
    firstname=forms.CharField(max_length=100,required=True,validators=[alphanumeric],widget=forms.TextInput(attrs={'placeholder':'Firstname','class':'form-control form-control-lg'}))  
    lastname=forms.CharField(max_length=100,required=True,validators=[alphanumeric],widget=forms.TextInput(attrs={'placeholder':'Lastname','class':'form-control form-control-lg'}))  
    email=forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control form-control-lg'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control form-control-lg'}),required=True)
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password','class':'form-control form-control-lg'}),required=True)
    reg_no=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'register number','class':'form-control form-control-lg'}))
    student_class=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder':'class','class':'form-control form-control-lg'}))
    phonenumber=forms.CharField(min_length=9,max_length=10,required=True,validators=[numbers],widget=forms.TextInput(attrs={'placeholder':'phonenumber','class':'form-control form-control-lg'}))
    




    def clean_reg_no(self):
        reg_no=self.cleaned_data.get('reg_no')
        if Student.objects.filter(reg_no=reg_no).exists():
            print('Used register number')
            raise forms.ValidationError('Used register number')
                
        else:
            return reg_no


    def clean_phonenumber(self):
        phonenumber=self.cleaned_data.get('phonenumber')
        if Student.objects.filter(phonenumber=phonenumber).exists():
            print('Used phonenumber')
            raise forms.ValidationError('Used phonenumber')
                
        else:
            return phonenumber

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            print('Using this email already an account')
            raise forms.ValidationError('Using this email already an account created,use another email')
                
        else:
            return email
    
    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        
        if password1 and password2 and password1!=password2:
           print('Password incorrect! try again')
           raise forms.ValidationError('Password incorrect! try again')
        else:
            return password2
    
    
    #creating and saving  user
    def create_user(self):
        print('user')
        user=User.objects.create_user(
            username=self.clean_email(),
            first_name=self.cleaned_data.get('firstname'),
            last_name=self.cleaned_data.get('lastname'),
            email=self.clean_email(),
            password=self.clean_password2()
        )
        user.save()
        return user
    #creating student
    def create_student(self):
        student=Student(
            first_name=self.cleaned_data.get('firstname'),
            last_name=self.cleaned_data.get('lastname'),
            reg_no=self.clean_reg_no(),
            student_class=self.cleaned_data.get('student_class'),
            phonenumber=self.clean_phonenumber()

        )
        student.save()
        return student