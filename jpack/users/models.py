from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.utils.text import slugify

GENDER = (('MALE', 'male'),
          ('FEMALE', 'female'))


class Profile(models.Model):
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=25, choices=GENDER)
    phone = models.CharField(max_length=250, blank=True)
    address = models.CharField(max_length=250)
    dob = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    signature = models.CharField(max_length=200)
    satus = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def get_full_name(self):
        return '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)



class Reporter(Profile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reporter_profile')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    class Meta:
        permissions = (
            ('view_reporterprofile', 'View ReporterProfile'),
            ('detail_reporterprofile', 'Detail ReporterProfile'),

        )

    def __str__(self):
        return self.get_full_name()



class DepartmentHead(Profile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    department = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    class Meta:
        permissions = (
            ('view_departmentprofile', 'View DepartmentProfile'),
            ('detail_departmentprofile', 'Detail DepartmentProfile'),

        )

    def __str__(self):
        return self.get_full_name()


class QualityDepartment(Profile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    department = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    class Meta:
        permissions = (
            ('view_qualitydepartmentprofile', 'View QualityDepartmentProfile'),
            ('detail_qualitydepartmentprofile', 'Detail QualityDepartmentProfile')


        )

    def __str__(self):
        return self.get_full_name()


def delete_user(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()


post_delete.connect(delete_user, sender=DepartmentHead)
post_delete.connect(delete_user, sender=QualityDepartment)
post_delete.connect(delete_user, sender=Reporter)