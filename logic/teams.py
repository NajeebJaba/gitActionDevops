from infra.api_wrapper import APIWrapper
class Teams(APIWrapper):

    def __init__(self, api_object):
        super().__init__()
        self.my_api = api_object

    def get_all_teams(self): #https://www.balldontlie.io/api/v1/teams
        result = self.my_api.api_get_request('https://api.balldontlie.io/v1/teams')
        if result is not None:
            return result.json()
        return None

    def get_team_by_id(self, team_id):
        result = self.my_api.api_get_request(f'https://www.balldontlie.io/api/v1/teams/{team_id}')
        if result is not None:
            return result.json()
        return None
