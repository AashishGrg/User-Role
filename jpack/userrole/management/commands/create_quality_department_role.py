from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = 'Create QD Role'

    def handle(self, *args, **options):
        qd_group, created = Group.objects.get_or_create(name="QD")

        qd_detail_perm = Permission.objects.get(
            codename='detail_qualitydepartmentprofile')
        qd_group.permissions.add(qd_detail_perm)

        self.stdout.write('Successfully created QD role')
