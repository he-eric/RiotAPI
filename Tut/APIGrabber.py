import requests
import RiotConsts as Consts

# Request summoner data 
def requestSummonerData(region, summonerName, APIKey):

    # Format the URL to correctly reflect variable names region, version, name, apikey
    URL = Consts.summoner
    URL = URL.format(region=region, version=Consts.version, name=summonerName, api_key=APIKey)
    
    # Requests.get is a function given to us my our import "requests". It basically goes to the URL we made and gives us back a JSON.
    response = requests.get(URL)
    
    return response.json()

# Request ranked data
def requestRankedData(region, ID, APIKey):
    
    URL = Consts.league
    URL = URL.format(region=region, version=Consts.version, id=ID, api_key=APIKey)
    
    response = requests.get(URL)
    return response.json()

# Request match history with accountID
def request_match_history(region, accountID, APIKey):
    
    URL = Consts.match
    URL = URL.format(region=region, version=Consts.version, accountID=accountID, api_key=APIKey)

    response = requests.get(URL)
    return response.json()

# Request game history with game id
def request_game_history(region, matchID, APIKey):
    
    URL = Consts.game
    URL = URL.format(region=region, version=Consts.version, matchid=matchID, api_key=APIKey)
    
    response = requests.get(URL)
    return response.json()

def main():
    print "main"

#This starts my program!
if __name__ == "__main__":
    main()

