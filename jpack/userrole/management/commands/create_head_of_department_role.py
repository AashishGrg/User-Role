from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = 'Create Head Of Department Role'

    def handle(self, *args, **options):
        hod_group, created = Group.objects.get_or_create(name="HOD")
        hod_detail_perm = Permission.objects.get(codename='detail_departmentprofile')
        hod_group.permissions.add(hod_detail_perm)

        self.stdout.write('Successfully created HOD role')