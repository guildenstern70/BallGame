#
#  The Ball Game Project
#
#  Copyright (c) 2021 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#

from django.db import models
from django.contrib.auth import get_user_model


# User Attributes
class UserAttributes(models.Model):
    has_team = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)

