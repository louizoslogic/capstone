import urllib.request
import requests
from json import loads
from secret import api_key
summonername = 'plippins'

class Person:
    name = 'John'

John = Person()

x = John

if x == John:
    print('this will work')

# response = requests.get('https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champions/120.json')

# data=response.json()
# print(data['name'])

# with urllib.request.urlopen('https://cdn.communitydragon.org/latest/champion/1/square') as response:
#     html = response.read()
#     data = loads(html)
#     print(data)


# with urllib.request.urlopen(f'https://na1.api.riotgames.com/lol/match/v4/matches/3806770516?api_key={api_key}') as response:
#     html = response.read()
#     data = loads(html)
#     print(data['participants'][0])

    # "participants": [
    #     {
    #         "participantId": 1,
    #         "teamId": 100,
    #         "championId": 55,
    #         "spell1Id": 14,
    #         "spell2Id": 4,
    #         "stats": {
    #             "participantId": 1,
    #             "win": true,
    #             "item0": 1054,
    #             "item1": 2031,
    #             "item2": 3153,
    #             "item3": 4636,
    #             "item4": 3020,
    #             "item5": 0,
    #             "item6": 3340,
    #             "kills": 10,
    #             "deaths": 4,
    #             "assists": 9,
    #             "largestKillingSpree": 3,
    #             "largestMultiKill": 2,
    #             "killingSprees": 3,
    #             "longestTimeSpentLiving": 557,
    #             "doubleKills": 2,
    #             "tripleKills": 0,
    #             "quadraKills": 0,
    #             "pentaKills": 0,
    #             "unrealKills": 0,
    #             "totalDamageDealt": 65483,
    #             "magicDamageDealt": 43267,
    #             "physicalDamageDealt": 21239,
    #             "trueDamageDealt": 976,
    #             "largestCriticalStrike": 0,
    #             "totalDamageDealtToChampions": 16387,
    #             "magicDamageDealtToChampions": 10896,
    #             "physicalDamageDealtToChampions": 5090,
    #             "trueDamageDealtToChampions": 400,
    #             "totalHeal": 3029,
    #             "totalUnitsHealed": 1,
    #             "damageSelfMitigated": 7557,
    #             "damageDealtToObjectives": 3191,
    #             "damageDealtToTurrets": 616,
    #             "visionScore": 11,
    #             "timeCCingOthers": 1,
    #             "totalDamageTaken": 17985,
    #             "magicalDamageTaken": 7223,
    #             "physicalDamageTaken": 8762,
    #             "trueDamageTaken": 2000,
    #             "goldEarned": 9422,
    #             "goldSpent": 8225,
    #             "turretKills": 1,
    #             "inhibitorKills": 0,
    #             "totalMinionsKilled": 84,
    #             "neutralMinionsKilled": 10,
    #             "neutralMinionsKilledTeamJungle": 2,
    #             "neutralMinionsKilledEnemyJungle": 4,
    #             "totalTimeCrowdControlDealt": 30,
    #             "champLevel": 13,
    #             "visionWardsBoughtInGame": 1,
    #             "sightWardsBoughtInGame": 0,
    #             "wardsPlaced": 7,
    #             "wardsKilled": 1,
    #             "firstBloodKill": false,
    #             "firstBloodAssist": false,
    #             "firstTowerKill": false,
    #             "firstTowerAssist": false,
    #             "firstInhibitorKill": false,
    #             "firstInhibitorAssist": true,
    #             "combatPlayerScore": 0,
    #             "objectivePlayerScore": 0,User.accountId
    #             "playerScore2": 0,
    #             "playerScore3": 1,
    #             "playerScore4": 0,
    #             "playerScore5": 0,
    #             "playerScore6": 0,
    #             "playerScore7": 0,
    #             "playerScore8": 0,
    #             "playerScore9": 0,
    #             "perk0": 8010,
    #             "perk0Var1": 274,
    #             "perk0Var2": 0,
    #             "perk0Var3": 0,
    #             "perk1": 9111,
    #             "perk1Var1": 968,
    #             "perk1Var2": 380,
    #             "perk1Var3": 0,
    #             "perk2": 9105,
    #             "perk2Var1": 13,
    #             "perk2Var2": 10,
    #             "perk2Var3": 0,
    #             "perk3": 8014,
    #             "perk3Var1": 474,
    #             "perk3Var2": 0,User.accountId
    #             "perk5Var2": 4,
    #             "perk5Var3": 0,
    #             "perkPrimaryStyle": 8000,
    #             "perkSubStyle": 8100,
    #             "statPerk0": 5008,
    #             "statPerk1": 5008,
    #             "statPerk2": 5002
    #         },
    #         "timeline": {
    #             "participantId": 1,
    #             "creepsPerMinDeltas": {
    #                 "10-20": 3.4000000000000004,
    #                 "0-10": 4.4
    #             },
    #             "xpPerMinDeltas": {
    #                 "10-20": 478.3,
    #                 "0-10": 464.6
    #             },
    #             "goldPerMinDeltas": {
    #                 "10-20": 479.5,
    #                 "0-10": 299.70000000000005
    #             },
    #             "csDiffPerMinDeltas": {
    #                 "10-20": -1,
    #                 "0-10": -1.6
    #             },
    #             "xpDiffPerMinDeltas": {
    #                 "10-20": 74.10000000000002,
    #                 "0-10": 58.10000000000002t.urlopen(f'https://na1.api.riotgames.co
    #             },
    #             "damageTakenPerMinDeltas": {
    #                 "10-20": 956,
    #                 "0-10": 413.8
    #             },
    #             "damageTakenDiffPerMinDeltas": {
    #                 "10-20": 266.5999999999999,
    #                 "0-10": 120.5
    #             },
    #             "role": "SOLO",
    #             "lane": "MIDDLE"
    #         }
    #     },


# with urllib.request.urlopen(f'https://na1.api.riotgames.com/lol/match/v4/matches/3806770516?api_key={api_key}') as response:
#     html = response.read()
#     data = loads(html)
#     print(data['participantIdentities'][0])

#         {
#             "participantId": 1,
#             "player": {
#                 "platformId": "NA1",
#                 "accountId": "9ekiif047-yzSyZmxMk-6oU-7SSVVsCn5VsWkPe9qfnG53rd2KaixVkV",
#                 "summonerName": "CookREE",
#                 "summonerId": "PCeIgfuoZM5kBw50fEHQ0sghQbgW1CNuyeK_6UakytrwwLlg",
#                 "currentPlatformId": "NA1",
#                 "currentAccountId": "9ekiif047-yzSyZmxMk-6oU-7SSVVsCn5VsWkPe9qfnG53rd2KaixVkV",
#                 "matchHistoryUri": "/v1/stats/player_history/NA1/2448282165930496",
#                 "profileIcon": 4847
#             }
#         },        participants = [
