#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from BallGame.dao import UsersDAO, UserAttributesDAO
from BallGame.services.user_attributes_service import create_user_attributes

TEST_USER = 'guest_test'


class DaoTest(TestCase):

    def setUp(self):
        # Create User
        User.objects.create_user(username=TEST_USER, password=TEST_USER)

    def test_should_find_an_user(self):
        """ Guest user is found """
        user_dao = UsersDAO()
        guest = user_dao.find_user(TEST_USER)
        self.assertTrue(check_password(TEST_USER, guest.password))

    def test_should_create_userattributes_if_missing(self):
        """ User Attributes are correctly created """
        user_attributes = UserAttributesDAO()
        self.assertFalse(user_attributes.userdata_exists_for(TEST_USER))
        create_user_attributes(TEST_USER)
        guest_user_data = user_attributes.get_user_attributes(TEST_USER)
        self.assertIsNotNone(guest_user_data)
        self.assertTrue(user_attributes.userdata_exists_for(TEST_USER))
        self.assertFalse(guest_user_data.has_team)
