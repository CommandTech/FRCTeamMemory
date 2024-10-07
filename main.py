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
        print('length: ' + str(len(session.get('selected_regions',[]))))
        session['chioices'] = 0
        if session.get('selected_regions',[]):
            session['chioices'] += len(session.get('selected_regions',[]))
        if session.get('regional', False):
            session['chioices'] += 1
        print(session.get('chioices', 0))
        
        team_choices = {
            0: regionalTeams,
            1: fimTeams,
            2: neTeams,
            3: pnwTeams,
            4: ontTeams,
            5: chsTeams,
            6: finTeams,
            7: fncTeams,
            8: pchTeams,
            9: fitTeams,
            10: fmaTeams,
            11: isrTeams,
            12: fscTeams
        }

        try:
            session['choice'] = random.randrange(0, session.get('choices', 0))
            team_list = team_choices.get(session['choice'], [])

            if team_list:
                team = random.choice(team_list)
                session['curTeam'] = team[0]
                session['curTeamName'] = team[1]
        except:
                session['curTeam'] = -1
                session['curTeamName'] = "No Teams Loaded"
        
        

@app.route('/')
def root():
    with app.app_context():
        print("\n\n\n\n\n\n")
        session['dark_mode'] = False
        session['authenticated'] = False
        
        session['chioices'] = 0
        session['teams'] = []
        session['curTeam'] = 0
        session['curTeamName'] = "Teams Not Loaded Yet"
        session['selected_regions'] = []
        session['active'] = []
        session['inactive'] = []
        session['regional'] = []
        genRandomTeam()
        return render_template('index.html', dark_mode=session.get('dark_mode', False), team=session.get('curTeamName', "Teams Not Loaded Yet"))

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
                    curTeam = [team['team_number'], team['nickname']]
                    team_list.append(curTeam)

    urls = [
        "https://www.thebluealliance.com/api/v3/teams/{pageNum}/simple?X-TBA-Auth-Key=zhTqFG7csJoif1sNXt3aZngy0LB1X4LxMgTfXBvPscNG0P9FifZCa2uGJcUk2gKW",
        "https://www.thebluealliance.com/api/v3/teams/2024/{pageNum}/simple?X-TBA-Auth-Key=zhTqFG7csJoif1sNXt3aZngy0LB1X4LxMgTfXBvPscNG0P9FifZCa2uGJcUk2gKW"
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
    session['active'] = data['active']
    session['inactive'] = data['inactive']
    session['regional'] = data['regional']
    genRandomTeam()
    return "0"

@app.route('/gen-random-team', methods=['POST'])
def gen_random_team_route():
    genRandomTeam()
    return jsonify({'status': 'success', 'newTeam': session['curTeam']})

def startWeb():
    app.run(host='0.0.0.0', port=80)


if __name__ == '__main__':
    getTeams()
    startWeb()