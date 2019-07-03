from __future__ import unicode_literals
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models


class UserRole(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_roles', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    started_at = models.DateTimeField(default=datetime.now)
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'user: {}\'s role : {}'.format(self.user, self.group)

    class Meta:
        unique_together = ('user', 'group')
