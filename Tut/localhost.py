import APIGrabber as API
import RiotConsts as Consts
import APIKey as Key
import json
from flask import Flask
from flask import request

app = Flask(__name__)
br = "<br/>"

# Return string format of json file
def stringify_json(jf):
    summoner_data = ""
    with open(jf) as json_file:
        data = json.load(json_file)
        for x in data:
            summoner_data += str(x)
            summoner_data = summoner_data + ": " + str(data[x]) + br
    return summoner_data

# Testing development server with APIs
# Route: http://127.0.0.1:5000
# Return: Possible links 
@app.route("/")
def hello():
    URLS = "http://127.0.0.1:5000/summoner_name?name=yourinput"+br+"Get summoner name. Yourinput is your summonername"
    return URLS

# Route: http://127.0.0.1:5000/summoner_name?name=Yabaschu
# Return: Summoner data on Yabaschu
@app.route("/summoner_name")
def getsummonername():
    
    # Get summoner name with request.args.get
    name = request.args.get('name')
    
    # Connect to Riot API and retrieve json data  
    responseJSON1 = API.requestSummonerData('na1', name, Key.APIKey)  
    responseJSON2 = API.requestRankedData('na1', responseJSON1["id"], Key.APIKey)
    responseJSON3 = API.request_match_history('na1', responseJSON1["accountId"], Key.APIKey)

    # Retrieve game history of the last game played
    responseJSON4 = API.request_game_history('na1', responseJSON3["matches"][0]["gameId"], Key.APIKey)
    
    # Create json file of summoner data for future use
    with open('data.json', 'w') as outfile:
        json.dump(responseJSON1, outfile)

    # Create json file of ranked data for future use
    with open('ranked.json', 'w') as outfile2:
        json.dump(responseJSON2, outfile2)
    
    # Create json file of match history for future use
    with open('match_history.json', 'w') as outfile3:
        json.dump(responseJSON3, outfile3)

    # Create json file of game history for future use
    with open('game_history.json', 'w') as outfile4:
        json.dump(responseJSON4, outfile4)

    # Output all summoner data
    OUTPUT = stringify_json("data.json")
    

    # Create output string to display onto website
    # OUTPUT = "Summoner name: " + responseJSON["name"]+br+"Summoner level: "+str(responseJSON["summonerLevel"])+br+'<img src="http://ddragon.leagueoflegends.com/cdn/6.24.1/img/profileicon/1.png"> '
    
    return OUTPUT
