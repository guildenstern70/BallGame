#
#  The Ball Game Project
#
#  Copyright (c) 2022 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import logging

from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from BallGame.dao import UsersDAO, UserAttributesDAO, PlayersDAO

TEST_USER = 'guest_test'

logger = logging.getLogger(__name__)


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
        user_dao = UsersDAO()
        self.assertFalse(user_attributes.user_attributes_exists_for(TEST_USER))
        user_dao.create_user_attributes(TEST_USER)
        guest_user_data = user_attributes.get_user_attributes(TEST_USER)
        self.assertIsNotNone(guest_user_data)
        self.assertTrue(user_attributes.user_attributes_exists_for(TEST_USER))
        self.assertFalse(guest_user_data.has_team)

    def test_should_get_all_players(self):
        players_dao = PlayersDAO()
        players = players_dao.get_all_players()
        self.assertIsNotNone(players)
        self.assertTrue(len(players) > 0)
        for player in players:
            logger.info(str(player))

    def test_should_get_players_by_position(self):
        players_dao = PlayersDAO()
        players = players_dao.get_players_by_position('P')
        self.assertIsNotNone(players)
        self.assertTrue(len(players) > 0)
        for player in players:
            self.assertTrue(player.position == 'P')
            logger.info(str(player))
