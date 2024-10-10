import requests
from flask import Flask, jsonify, session, redirect, url_for, request, render_template, send_from_directory
import threading
import concurrent.futures
import random
from datetime import datetime
from datetime import timedelta

app = Flask(__name__, static_folder='static')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)

frcTeams = []

regionalTeams = []

fimTeams = []

neTeams = []

pnwTeams = []

ontTeams = []

chsTeams = []

finTeams = []

fncTeams = []

pchTeams = []

fitTeams = []

fmaTeams = []

isrTeams = []

fscTeams = []

districtKeys = [f"{datetime.now().year}fim", f"{datetime.now().year}ne",f"{datetime.now().year}pnw", f"{datetime.now().year}ont", f"{datetime.now().year}chs", f"{datetime.now().year}fin",f"{datetime.now().year}fnc",f"{datetime.now().year}pch", f"{datetime.now().year}fit",
                 f"{datetime.now().year}fma", f"{datetime.now().year}isr", f"{datetime.now().year}fsc"]

def genRandomTeam():
    with app.app_context():
        team_choices = {
            0: chsTeams,
            1: fimTeams,
            2: fitTeams,
            3: finTeams,
            4: isrTeams,
            5: fmaTeams,
            6: fncTeams,
            7: fscTeams,
            8: neTeams,
            9: ontTeams,
            10: pnwTeams,
            11: pchTeams
        }

        try:
            if session['regional'] and session['selected_regions'] == []:
                team_list = regionalTeams
            elif random.choice([True, False]) and session.get('regional'):
                #regional
                team_list = regionalTeams
            else:
                #district
                while True:
                    session['choice'] = random.randrange(0, 11)
                    temp = ''
                    match (session['choice']):
                        case 0:
                            temp = 'chesapeake'
                            pass
                        case 1:
                            temp = 'michigan'
                            pass
                        case 2:
                            temp = 'texas'
                            pass
                        case 3:
                            temp = 'indiana'
                            pass
                        case 4:
                            temp = 'isreal'
                            pass
                        case 5:
                            temp = 'mid-atlantic'
                            pass
                        case 6:
                            temp = 'northcarolina'
                            pass
                        case 7:
                            temp = 'southcarolina'
                            pass
                        case 8:
                            temp = 'newengland'
                            pass
                        case 9:
                            temp = 'ontario'
                            pass
                        case 10:
                            temp = 'pacificnorthwest'
                            pass
                        case 11:
                            temp = 'peachtree'
                            pass

                    if temp in session.get('selected_regions', []):
                        break
                    elif session['selected_regions'] == []:
                        break
                
                if session['selected_regions'] == []:
                    session['curTeam'] = -1
                    session['curTeamName'] = "No Teams Loaded"
                    team_list = []
                else:
                    team_list = team_choices.get(session['choice'], [])

            if team_list:
                team = random.choice(team_list)
                session['curTeam'] = team[0]
                session['curTeamName'] = team[1]
                print(team[2].split(", ")[0])
                print(team[2].split(", ")[1])
                session['curTeamCity'] = team[2].split(", ")[0]
                session['curTeamState'] = team[2].split(", ")[1]
        except:
            session['curTeam'] = -1
            session['curTeamName'] = "No Teams Loaded"
            session['curTeamCity'] = "No City"
            session['curTeamState'] = "No State"
        
        

@app.route('/')
def root():
    with app.app_context():
        if 'dark_mode' not in session:
            session['dark_mode'] = False
        
        session['curTeam'] = 0
        session['curTeamName'] = "Teams Not Loaded Yet"

        session['curTeamCity'] = "No City"
        session['curTeamState'] = "No State"

        if 'selected_regions' not in session:
            session['selected_regions'] = ['chesapeake', 'michigan', 'texas', 'indiana', 'isreal', 'mid-atlantic', 'northcarolina', 'newengland', 'ontario', 'pacificnorthwest', 'peachtree']
        if 'regional' not in session:
            session['regional'] = True
        
        genRandomTeam()
        return render_template('index.html', dark_mode=session.get('dark_mode', False), team=session['curTeamName'], selected_regions=session.get('selected_regions', []), regional=session.get('regional', False), city=session.get('curTeamCity', "No City"), state=session.get('curTeamState', "No State"))

@app.route('/check-team', methods=['POST'])
def check_team():
    data = request.get_json()
    try:
        teamNumber = int(data['teamNumber'])
    except:
        teamNumber = -1
    
    with app.app_context():
        match = teamNumber == session.get('curTeam',0)
        correctTeamNumber = session.get('curTeam',0)
        genRandomTeam()
        return jsonify({'match': match, 'correctTeamNumber': correctTeamNumber, 'newTeamName': session.get('curTeamName', "Teams Not Loaded Yet")})

@app.route('/script.js')
def script():
    return send_from_directory('', 'static/script.js')

@app.route('/style.css')
def styleSecond():
    return send_from_directory('', 'static/style.css')

@app.route('/dark-mode')
def dark_mode():
    session['dark_mode'] = not session.get('dark_mode', False)
    return "0"

def getTeams():
    global frcTeams, fimTeams, neTeams, pnwTeams, ontTeams, chsTeams, finTeams, fncTeams, pchTeams, fitTeams, fmaTeams, isrTeams, fscTeams, regionalTeams

    def fetch_teams(url, team_list, pageNum=None):
        if pageNum is not None:
            url = url.format(pageNum=pageNum)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                for team in data:
                    curTeam = [team['team_number'], team['nickname'], team['city'] + ", " + team['state_prov']]
                    team_list.append(curTeam)

    urls = [
        "https://www.thebluealliance.com/api/v3/teams/{pageNum}/simple?X-TBA-Auth-Key=zhTqFG7csJoif1sNXt3aZngy0LB1X4LxMgTfXBvPscNG0P9FifZCa2uGJcUk2gKW",
        f"https://www.thebluealliance.com/api/v3/teams/{datetime.now().year}/{{pageNum}}/simple?X-TBA-Auth-Key=zhTqFG7csJoif1sNXt3aZngy0LB1X4LxMgTfXBvPscNG0P9FifZCa2uGJcUk2gKW"
    ]

    district_urls = [
        f"https://www.thebluealliance.com/api/v3/district/{districtKey}/teams/simple?X-TBA-Auth-Key=zhTqFG7csJoif1sNXt3aZngy0LB1X4LxMgTfXBvPscNG0P9FifZCa2uGJcUk2gKW"
        for districtKey in districtKeys
    ]

    district_teams = [
        fimTeams, neTeams, pnwTeams, ontTeams, chsTeams, finTeams, fncTeams, pchTeams, fitTeams, fmaTeams, isrTeams, fscTeams
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in urls:
            for pageNum in range(20):  # Create 20 threads for each URL
                futures.append(executor.submit(fetch_teams, url, frcTeams, pageNum))
        for url, team_list in zip(district_urls, district_teams):
            futures.append(executor.submit(fetch_teams, url, team_list))
        concurrent.futures.wait(futures)

    regionalTeams = [team for team in frcTeams if team not in fimTeams + neTeams + pnwTeams + ontTeams + chsTeams + finTeams + fncTeams + pchTeams + fitTeams + fmaTeams + isrTeams + fscTeams]


@app.route('/update-teams', methods=['POST'])
def update_teams():
    data = request.get_json()
    session['selected_regions'] = data['regions']
    session['regional'] = data['regional']
    genRandomTeam()
    return "0"

@app.route('/gen-random-team', methods=['POST'])
def gen_random_team_route():
    genRandomTeam()
    return jsonify({'status': 'success', 'newTeamName': session['curTeamName'], 'newTeamCity': session['curTeamCity'], 'newTeamState': session['curTeamState']})

def startWeb():
    app.run(host='0.0.0.0', port=81)


if __name__ == '__main__':
    getTeams()
    startWeb()