### get a list of matches that I have played in
import requests
from requests.api import get
import json


summoner_name = "bigdac"

summoner_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-5e863ef6-d38a-4f51-9fd3-8d7481743bd4"
}


def get_summoner_url(summ):
    url_prefix = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/"
    return url_prefix + summ



def get_summoner_puuid(summoner, header):
    url = get_summoner_url(summoner)
    sort = "puuid"
    response = requests.get(url, headers = header)
    puuid = response.json()[sort]
    return puuid


def get_matches(puuid, num_matches, header):
    url_prefix = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/"
    url = url_prefix + puuid + "/ids?count=" + num_matches
    response = requests.get(url, headers = header)
    return response.json()

#returns data of match in JSON format
def get_game_data(match_id, header):
    url_prefix = "https://americas.api.riotgames.com/tft/match/v1/matches/"
    url = url_prefix + match_id
    response = requests.get(url, headers = header)
    return response.json()

# def get_game_table(match_id, header):
#     raw = get_game_data(match_id, header)
#     raw.keys()




# var = get_summoner_puuid(summoner_name, summoner_header)
# print(var)

# matches = get_matches(var,"20", summoner_header)
# print(matches)
# print(type(matches))
# print(matches[0])
# data = get_game_data(matches[0], summoner_header)
# print(data)
# print(type(data))