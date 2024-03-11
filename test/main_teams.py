import unittest
from logic.teams import Teams
from infra.api_wrapper import APIWrapper


class TeamsTest(unittest.TestCase):
    def setUp(self):
        api_key = '46e29623-4a45-46d5-83ca-8acc2be72534'
        self.my_api = APIWrapper(api_key)
        self.teams_api = Teams(self.my_api)

    def test_get_all_teams_status(self):
        response = self.teams_api.get_all_teams()
        self.assertIsNotNone(response, "API request did not return data.")
        self.assertIn('data', response)

    def test_team_details(self):
        team_id = 1
        response = self.teams_api.get_team_by_id(team_id)
        self.assertIsNotNone(response, "API request did not return data.")
        self.assertEqual(response['city'], "Atlanta")
        self.assertEqual(response['name'], "Hawks")


if __name__ == '__main__':
    unittest.main()
