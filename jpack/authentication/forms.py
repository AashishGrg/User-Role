from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import Reporter, DepartmentHead, QualityDepartment


GENDER_TYPE = (('MALE', 'Male'),
               ('FEMALE', 'Female'),
               ('OTHER', 'Other')

               )

# class StudentForm(forms.ModelForm):

#     class Meta:
#         model = Reporter
#         fields = ( 'first_name', 'middle_name', 'last_name', 'email', 'phone', 'address',
#                     'dob','gender','signature')

# class ParentForm(forms.ModelForm):

#     class Meta:
#         model = DepartmentHead
#         fields = ('first_name', 'middle_name', 'last_name', 'email', 'phone', 'address',
#                'dob','gender','signature','department')


# class TeacherForm(forms.ModelForm):

#     class Meta:
#         model = QualityDepartment
#         fields = ('first_name', 'middle_name', 'last_name', 'email', 'phone', 'address',
#                'dob','gender','signature','department')


class UserProfileForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=False)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    phone = forms.CharField(max_length=250)
    address = forms.CharField(max_length=250)
    signature = forms.CharField(max_length=250)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None


class ReporterSignupForm(UserProfileForm):


    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'password1', 'password2', 'email', 'gender',
                  'phone', 'address', 'signature']


class DepartmentSignupForm(UserProfileForm):

    department = forms.CharField()
    # parent = forms.ModelChoiceField(
    #         queryset=ParentProfile.objects.all(),
    #         widget=autocomplete.ModelSelect2(url='authentication:parent_autocomplete')
    # )

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'password1', 'password2', 'email', 'gender',
                  'phone', 'address', 'signature','department']


class QdSignupForm(UserProfileForm):

    department = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'password1', 'password2', 'email', 'gender',
                  'phone', 'address', 'signature','department']
