from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = 'Create Reporter Role'

    def handle(self, *args, **options):
        reporter_group, created = Group.objects.get_or_create(name="Reporter")

        # authentication app
        reporter_detail_perm = Permission.objects.get(codename='detail_reporterprofile')
        reporter_group.permissions.add(reporter_detail_perm)

        self.stdout.write('Successfully created Reporter role')