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
from BallGame.dao.teams_dao import TeamsDAO
from BallGame.utils import create_players_db

TEST_USER = 'guest_test'

logger = logging.getLogger(__name__)


class DaoTest(TestCase):

    def setUp(self):
        # Create User
        User.objects.create_user(username=TEST_USER, password=TEST_USER)
        create_players_db()

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
        """ Can get all players """
        players_dao = PlayersDAO()
        players = players_dao.get_all_players()
        self.assertIsNotNone(players)
        self.assertTrue(len(players) > 0)
        for player in players:
            logger.info(str(player))

    def test_should_get_players_by_position(self):
        """ Get players by position """
        players_dao = PlayersDAO()
        players = players_dao.get_players_by_position('P')
        self.assertIsNotNone(players)
        self.assertTrue(len(players) > 0)
        for player in players:
            self.assertTrue(player.position == 'P')
            logger.info(str(player))

    def test_user_can_own_a_team(self):
        """ A user can have a team + cleanup """
        team_name = 'NEW TEAM'
        user_dao = UsersDAO()
        teams_dao = TeamsDAO()
        user = user_dao.find_user(TEST_USER)
        self.assertFalse(teams_dao.user_has_team(user))
        teams_dao.create_new_team(team_name, user)
        new_team = teams_dao.find_by_name(team_name)
        self.assertIsNotNone(new_team)
        self.assertEqual(new_team.name, team_name)
        # Clean up
        teams_dao.delete(new_team)
        new_team = teams_dao.find_by_name(team_name)
        self.assertIsNone(new_team)

    def test_team_can_have_players(self):
        """ User can add players to her team + cleanup """
        team_name = 'EAGLES'
        teams_dao = TeamsDAO()
        user_dao = UsersDAO()
        user = user_dao.find_user(TEST_USER)
        players_dao = PlayersDAO()
        team = teams_dao.create_new_team(team_name, user)
        pitchers = players_dao.get_players_by_position('P')
        self.assertIsNotNone(pitchers[0])
        shortstops = players_dao.get_players_by_position('SS')
        self.assertIsNotNone(shortstops[0])
        catchers = players_dao.get_players_by_position('C')
        self.assertIsNotNone(catchers[0])
        teams_dao.add_player_to_team(team, pitchers[0])
        teams_dao.add_player_to_team(team, shortstops[0])
        teams_dao.add_player_to_team(team, catchers[0])
        players_in_team = players_dao.get_players_in_team(team)
        for player in players_in_team:
            self.assertTrue(player.team == team)
            logger.info(str(player))
        self.assertEqual(len(players_in_team), 3)
        # Clean up
        logger.info("== Players in team " + team_name)
        for player in players_in_team:
            teams_dao.remove_player_from_team(player)
        logger.info("==")


