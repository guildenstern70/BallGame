#
#  The Ball Game Project
#
#  Copyright (c) 2021-23 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=30, unique=True)
    user = models.OneToOneField(
        User,
        on_delete=models.DO_NOTHING,
        primary_key=False,
    )

    @classmethod
    def create(cls, name, user):
        """
        Create a new team
        """
        return cls(name=name, user=user)

