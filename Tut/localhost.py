import APIGrabber as API
import RiotConsts as Consts
from flask import Flask
from flask import request

app = Flask(__name__)
br = "<br/>"

# Testing development server with APIs
# Route: http://127.0.0.1:5000
# Return: Possible links 
@app.route("/")
def hello():
    URLS = "http://127.0.0.1:5000/summoner_name?name=yourinput"+br+"Get summoner name. Yourinput is your summonername"
    return URLS

# Route: http://127.0.0.1:5000/summoner_name?name=userinput
# Return: Summoner name
@app.route("/summoner_name")
def getsummonername():
    name = request.args.get('name')
    responseJSON = API.requestSummonerData('na1', name, Consts.APIKey)  
    OUTPUT = "Summoner name: " + responseJSON["name"]+br+"Summoner level: "+str(responseJSON["summonerLevel"])+br+'<img src="http://ddragon.leagueoflegends.com/cdn/6.24.1/img/profileicon/1.png"> '
    return OUTPUT
