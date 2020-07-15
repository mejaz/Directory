from .models import TeacherModel, PhoneModel, SubjectModel, ProPic, ImporterModel
from django.forms import ModelForm, CheckboxSelectMultiple, Form, CharField, PasswordInput


class TeacherForm(ModelForm):
    class Meta:
        model = TeacherModel
        fields = ['fname', 'lname', 'email', 'room_number']
        labels = {
            "fname": "First Name",
            "lname": "Last Name",
            "email": "Email",
            "room_number": "Room Number",
        }

class PhoneForm(ModelForm):
    class Meta:
        model = PhoneModel
        fields = ['phone_number']
        labels = {
            "phone_number": "Phone Number",
        }

class ProPicForm(ModelForm):
    class Meta:
        model = ProPic
        fields = ['propic']
        labels = {
            "propic": "Profile Picture",
        }

class SubjectForm(ModelForm):
    class Meta:
        model = SubjectModel
        fields = ['subject']
        labels = {
            "subject": "Subjects",
        }

        widgets={
            'subject': CheckboxSelectMultiple(),
        }

class ImporterForm(ModelForm):
    class Meta:
        model = ImporterModel
        fields = ['filename']
        labels = {
            "filename": "Upload CSV File",
        }
