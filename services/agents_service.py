from api.riot import Riot

class AgentsService():

    def get_agents(self):
        #TODO: cache and retrieve data
        riot_content = Riot().get_content()
        return riot_content['characters']