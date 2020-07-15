from django.db import models
from multiselectfield import MultiSelectField

class TeacherModel(models.Model):

    class Meta:
        db_table = 'Teacher'

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    room_number = models.CharField(max_length=10)

class ProPic(models.Model):
    class Meta:
        db_table = 'ProPic'

    propic = models.ImageField(upload_to='pro-pics/')
    teacher = models.ForeignKey('TeacherModel', on_delete=models.CASCADE)


class PhoneModel(models.Model):

    class Meta:
        db_table = 'Phone'

    phone_number = models.CharField(max_length=20)
    teacher = models.ForeignKey('TeacherModel', on_delete=models.CASCADE)

class SubjectModel(models.Model):

    SUBJECT_CHOICES = [
        ('Computer Science', 'Computer Science'),
        ('Physics', 'Physics'),
        ('Mathematics', 'Mathematics'),
        ('History', 'History'),
        ('Geography', 'Geography'),
        ('Biology', 'Biology'),
        ('Chemistry', 'Chemistry'),
        ('English', 'English'),
        ('Arabic', 'Arabic')
    ]

    class Meta:
        db_table = 'Subject'

    subject = MultiSelectField(max_length=75, choices=SUBJECT_CHOICES, max_choices=5)
    teacher = models.ForeignKey('TeacherModel', on_delete=models.CASCADE)


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.csv']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Only .csv supported.')

class ImporterModel(models.Model):

    class Meta:
        db_table = 'ImporterFiles'

    filename = models.FileField(upload_to='csvfiles/', validators=[validate_file_extension])
