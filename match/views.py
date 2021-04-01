from django.shortcuts import render
import os
from .models import Match, Participant
import urllib.request
from json import loads
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import requests


def is_os():
    # Checks where to find keys from

    if 'api_key' in os.environ:
        return os.environ["api_key"]

    else:
        from secret import api_key
        return api_key


@login_required
def match(request):

    matches = get_matches(request.user)

    def get_matchid(obj):
        return obj.matchid

    # sort list with key
    matches.sort(key=get_matchid, reverse=True)
    for i, match in enumerate(matches):

        if match.userparticipant is None:
            matches.remove(match)
        elif match.participant1.lane is None:
            print(match.userparticipant.lane)
            matches.remove(match)
    context = {"matches": matches}
    for match in matches:
        print(match.matchid)

    return render(request, 'match/matches.html', context)


def get_matches(User: object) -> list:
    # gets list of matches associated with user referenced

    return list(Match.objects.filter(user=User))


def updatedb(request):

    user = request.user
    update_database(user)

    return HttpResponse(user.summonername)


def update_database(User: object):
    # sends request to Riot API for recent matches

    with urllib.request.urlopen(f'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{User.accountId}?api_key={is_os()}') as response:
        html = response.read()
        data = loads(html)
        matches = get_matches(User)
        for i in range(5):
            verify = False
            for match in matches:
                if str(data['matches'][i]['gameId']) == str(match.matchid):
                    verify = True

            if verify is False:
                match = Match.objects.create(matchid=data['matches'][i]['gameId'], user=User)
                get_match_info(match, User)


def get_champion_name(id:str) -> str:
    # sends request to cdragon for champion associated with ID

    response = requests.get(f'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champions/{id}.json')
    data = response.json()
    return data['name']


def create_participants(data, match: object, user: object):
    # adds associated variables for all 10 participants in game, assigns userparticipant

    match.participant1 = Participant.objects.create()
    match.participant2 = Participant.objects.create()
    match.participant3 = Participant.objects.create()
    match.participant4 = Participant.objects.create()
    match.participant5 = Participant.objects.create()
    match.participant6 = Participant.objects.create()
    match.participant7 = Participant.objects.create()
    match.participant8 = Participant.objects.create()
    match.participant9 = Participant.objects.create()
    match.participant10 = Participant.objects.create()

    participants = [
        match.participant1,
        match.participant2,
        match.participant3,
        match.participant4,
        match.participant5,
        match.participant6,
        match.participant7,
        match.participant8,
        match.participant9,
        match.participant10,
        ]

    for i, participant in enumerate(participants):

        participant.summoner = data['participantIdentities'][i]['player']['summonerName']
        participant.championid = data['participants'][i]['championId']
        participant.championname = get_champion_name(participant.championid)
        participant.championicon = f'https://cdn.communitydragon.org/latest/champion/{participant.championid}/square'
        participant.win = data['participants'][i]['stats']['win']
        participant.lane = data['participants'][i]['timeline']['lane'].capitalize()
        participant.kills = data['participants'][i]['stats']['kills']
        participant.deaths = data['participants'][i]['stats']['deaths']
        participant.assists = data['participants'][i]['stats']['assists']
        # participant.spell1Id = data['participants'][i]['spell1Id']
        # participant.spell2Id = data['participants'][i]['spell2Id']

        participant.save()

        # associating a participant with the logged on user
        if participant.summoner == user.summonername:

            match.userparticipant = Participant.objects.create()
            match.userparticipant.summoner = participant.summoner
            match.userparticipant.championid = participant.championid
            match.userparticipant.championname = participant.championname
            match.userparticipant.championicon = participant.championicon
            match.userparticipant.win = participant.win
            match.userparticipant.lane = participant.lane
            match.userparticipant.kills = participant.kills
            match.userparticipant.deaths = participant.deaths
            match.userparticipant.assists = participant.assists

            # match.userparticipant.spell1Id = participant.spell1Id
            # match.userparticipant.spell2Id = participant.spell2Id

            if participant.win is True:
                match.win = 'Victory'
            else:
                match.win = 'Defeat'

            participant.is_user = True
            match.victory = match.userparticipant.win

            match.userparticipant.save()

    match.save()


def get_match_info(match, user):

    with urllib.request.urlopen(f'https://na1.api.riotgames.com/lol/match/v4/matches/{match.matchid}?api_key={is_os()}') as response:
        html = response.read()
        data = loads(html)

    # returns list of participant objects
    create_participants(data, match, user)

    match.save()
