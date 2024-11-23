import requests
from flask import Flask, jsonify, session, request, render_template, send_from_directory
import concurrent.futures
import random
from datetime import datetime
from datetime import timedelta
import secrets
import string
import re
from flask_talisman import Talisman

app = Flask(__name__, static_folder='static')
Talisman(app, force_https=True)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)

frcTeams = []

regionalTeams = []

alTeams = []
akTeams = []
azTeams = []
arTeams = []
caTeams = []
coTeams = []
flTeams = []
hiTeams = []
idTeams = []
ilTeams = []
iaTeams = []
ksTeams = []
kyTeams = []
laTeams = []
mnTeams = []
msTeams = []
moTeams = []
mtTeams = []
RneTeams = []
nvTeams = []
nmTeams = []
nyTeams = []
ndTeams = []
ohTeams = []
okTeams = []
paTeams = []
sdTeams = []
tnTeams = []
utTeams = []
wvTeams = []
wiTeams = []
wyTeams = []
prTeams = []
guTeams = []
dcTeams = []
otherTeams = [] #9009

ausTeams = [] #Australia
braTeams = [] #Brazil
canTeams = [] #Canada
chiTeams = [] #China
japTeams = [] #Japan
mexTeams = [] #Mexico
turTeams = [] #Türkiye
ukTeams = [] #United Kingdom
netTeams = [] #Netherlands
taiTeams = [] #Chinese Taipei
polTeams = [] #Poland
bulTeams = [] #Bulgaria
greTeams = [] #Greece
domTeams = [] #Dominican Republic
indTeams = [] #India
argTeams = [] #Argentina
romTeams = [] #Romania
azeTeams = [] #Azerbaijan
sweTeams = [] #Sweden
fraTeams = [] #France
botTeams = [] #Botswana
ecuTeams = [] #Ecuador
surTeams = [] #Suriname
serTeams = [] #Serbia
comTeams = [] #Comoros
pakTeams = [] #Pakistan
ukrTeams = [] #Ukraine
phiTeams = [] #Philippines
gamTeams = [] #Gambia
czeTeams = [] #Czech Republic
micTeams = [] #Micronesia
kazTeams = [] #Kazakhstan
manTeams = [] #Manisia
belTeams = [] #Belize

colTeams = [] #Columbia
croTeams = [] #Croatia
zelTeams = [] #New Zealand
afgTeams = [] #Afghanistan
bosTeams = [] #Bosnia and Herzegovina
norTeams = [] #Norway
itaTeams = [] #Italy
denTeams = [] #Denmark
swiTeams = [] #Switzerland
gerTeams = [] #Germany
sinTeams = [] #Singapore
chlTeams = [] #Chile
libTeams = [] #Libya
uaeTeams = [] #United Arab Emirates
safTeams = [] #South Africa
armTeams = [] #Armenia
venTeams = [] #Venezuela
vieTeams = [] #Vietnam
zimTeams = [] #Zimbabwe
morTeams = [] #Morocco
tonTeams = [] #Tonga
inoTeams = [] #Indonesia
ethTeams = [] #Ethiopia
parTeams = [] #Paraguay
panTeams = [] #Panama
lesTeams = [] #Lesotho
barTeams = [] #Barbados
sokTeams = [] #South Korea
papTeams = [] #Papua New Guinea
saiTeams = [] #Saint Kitts and Nevis

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

team_name_mapping = {
    'alTeams': 'Alabama', 'akTeams': 'Alaska', 'azTeams': 'Arizona', 'arTeams': 'Arkansas', 'caTeams': 'California',
    'coTeams': 'Colorado', 'flTeams': 'Florida', 'hiTeams': 'Hawaii', 'idTeams': 'Idaho', 'ilTeams': 'Illinois',
    'iaTeams': 'Iowa', 'ksTeams': 'Kansas', 'kyTeams': 'Kentucky', 'laTeams': 'Louisiana', 'mnTeams': 'Minnesota',
    'msTeams': 'Mississippi', 'moTeams': 'Missouri', 'mtTeams': 'Montana', 'RneTeams': 'Nebraska', 'nvTeams': 'Nevada',
    'nmTeams': 'New Mexico', 'nyTeams': 'New York', 'ndTeams': 'North Dakota', 'ohTeams': 'Ohio', 'okTeams': 'Oklahoma',
    'paTeams': 'Pennsylvania', 'sdTeams': 'South Dakota', 'tnTeams': 'Tennessee', 'utTeams': 'Utah', 'wvTeams': 'West Virginia',
    'wiTeams': 'Wisconsin', 'wyTeams': 'Wyoming', 'prTeams': 'Puerto Rico', 'guTeams': 'Guam', 'dcTeams': 'D.C.', 'otherTeams': 'Other',
    'ausTeams': 'Australia', 'braTeams': 'Brazil', 'canTeams': 'Canada', 'chiTeams': 'China', 'japTeams': 'Japan',
    'mexTeams': 'Mexico', 'turTeams': 'Türkiye', 'ukTeams': 'United Kingdom', 'netTeams': 'Netherlands', 'taiTeams': 'Chinese Taipei',
    'polTeams': 'Poland', 'bulTeams': 'Bulgaria', 'greTeams': 'Greece', 'domTeams': 'Dominican Republic', 'indTeams': 'India',
    'argTeams': 'Argentina', 'romTeams': 'Romania', 'azeTeams': 'Azerbaijan', 'sweTeams': 'Sweden', 'fraTeams': 'France',
    'botTeams': 'Botswana', 'ecuTeams': 'Ecuador', 'surTeams': 'Suriname', 'serTeams': 'Serbia', 'comTeams': 'Comoros',
    'pakTeams': 'Pakistan', 'ukrTeams': 'Ukraine', 'phiTeams': 'Philippines', 'gamTeams': 'Gambia', 'czeTeams': 'Czech Republic',
    'micTeams': 'Micronesia', 'kazTeams': 'Kazakhstan', 'manTeams': 'Manisia', 'belTeams': 'Belize', 'colTeams': 'Columbia',
    'croTeams': 'Croatia', 'zelTeams': 'New Zealand', 'afgTeams': 'Afghanistan', 'bosTeams': 'Bosnia and Herzegovina',
    'norTeams': 'Norway', 'itaTeams': 'Italy', 'denTeams': 'Denmark', 'swiTeams': 'Switzerland', 'gerTeams': 'Germany',
    'sinTeams': 'Singapore', 'chlTeams': 'Chile', 'libTeams': 'Libya', 'uaeTeams': 'United Arab Emirates', 'safTeams': 'South Africa',
    'armTeams': 'Armenia', 'venTeams': 'Venezuela', 'vieTeams': 'Vietnam', 'zimTeams': 'Zimbabwe', 'morTeams': 'Morocco',
    'tonTeams': 'Tonga', 'inoTeams': 'Indonesia', 'ethTeams': 'Ethiopia', 'parTeams': 'Paraguay', 'panTeams': 'Panama',
    'lesTeams': 'Lesotho', 'barTeams': 'Barbados', 'sokTeams': 'South Korea', 'papTeams': 'Papua New Guinea', 'saiTeams': 'Saint Kitts and Nevis'
}

def genRandomTeam():
    with app.app_context():
        try:
            team_list = []
            session['choice'] = -1
            if session.get('selected_regions') and session.get('regional'):
                if random.choice([True, False]):
                    #regional
                    session['choice'] = random.choice(session['regional'])

                    team_list = globals()[session['choice']]
                    pass
                else:
                    #district
                    session['choice'] = random.choice(session['selected_regions'])

                    team_list = globals()[session['choice']]

            elif session.get('selected_regions') and not session.get('regional'):
                #district
                session['choice'] = random.choice(session['selected_regions'])

                team_list = globals()[session['choice']]

            else:
                #regional
                session['choice'] = random.choice(session['regional'])

                team_list = globals()[session['choice']]

            if team_list != [] and session['choice'] != -1:
                team = random.choice(team_list)
                session['curTeam'] = team[0]
                
                session['curTeamInfo'] = team[1]
                session['curTeamName'] = team[2]
                try:
                    session['curTeamCity'] = team[3].split(", ")[0]
                except:
                    session['curTeamCity'] = team[3]

                try:
                    session['curTeamState'] = team[3].split(", ")[1]
                except:
                    session['curTeamState'] = team[4]

                session['curTeamCountry'] = team[5]


            if re.search(r'team \d{1,4}', session['curTeamInfo'].lower()):
                session['curTeamInfo'] = "No Info"
                
        except:
            print("excepted")
            session['curTeam'] = -1
            session['curTeamName'] = "No Teams Loaded"
            session['curTeamInfo'] = "No Info"
            session['curTeamCity'] = "No City"
            session['curTeamState'] = "No State"
            session['curTeamCountry'] = "No Country"

def generate_unique_session_id(ip_address):
    characters = string.ascii_letters + string.digits
    while True:
        new_id = ''.join(secrets.choice(characters) for _ in range(32))
        if not is_id_in_file(new_id):
            with open('ids.txt', 'a') as f:
                f.write(f"{new_id},User-{new_id},{ip_address},0,0\n")
            return new_id

def is_id_in_file(id_to_check):
    try:
        with open('ids.txt', 'r') as f:
            ids = f.read().splitlines()
            return any(id_to_check in line for line in ids)
    except FileNotFoundError:
        return False

def update_ip_address_if_changed(session_id, new_ip_address):
    ids = []
    try:
        with open('ids.txt', 'r') as file:
            ids = file.readlines()
    except FileNotFoundError:
        pass

    with open('ids.txt', 'w') as file:
        for line in ids:
            parts = line.strip().split(',')
            if parts[0] == session_id:
                if parts[2] != new_ip_address:
                    parts[2] = new_ip_address
                file.write(','.join(parts) + '\n')
            else:
                file.write(line)

def get_session_data_by_ip(ip_address):
    try:
        with open('ids.txt', 'r') as file:
            for line in file:
                session_id, username, ip, highest_streak, highest_streak_hard = line.strip().split(',')
                if ip == ip_address:
                    return session_id, username, int(highest_streak), int(highest_streak_hard)
    except FileNotFoundError:
        pass
    return None, None, 0, 0

def get_highest_streak_by_session_id(session_id):
    try:
        with open('leaderboards.txt', 'r') as file:
            for line in file:
                sid, score = line.strip().split(',')
                if sid == session_id:
                    return int(score)
    except FileNotFoundError:
        pass
    return 0

def get_username_by_session_id(session_id):
    # This function should retrieve the username associated with the session ID
    # For simplicity, we'll assume the username is stored in the session
    # In a real application, you might need to store this mapping in a database
    if session.get('id') == session_id:
        return session.get('username', 'Unknown')
    return 'Unknown'

def startWeb():
    app.run(host='0.0.0.0', port=81, ssl_context=('cert.pem', 'key.pem'))

def get_username_by_session_id(session_id):
    try:
        with open('ids.txt', 'r') as file:
            for line in file:
                if line.startswith(session_id):
                    return line.strip().split(',')[1]
    except FileNotFoundError:
        pass
    return 'Unknown'

def getTeams():
    global regionalTeams, alTeams, akTeams, azTeams,  arTeams, caTeams, coTeams, flTeams, hiTeams, idTeams, ilTeams, iaTeams, ksTeams, kyTeams, laTeams, mnTeams, msTeams, moTeams, mtTeams, RneTeams, nvTeams, nmTeams, nyTeams, ndTeams, ohTeams, okTeams, paTeams, sdTeams, tnTeams, utTeams, wvTeams, wiTeams, wyTeams, otherTeams
    global ausTeams, braTeams, canTeams, chiTeams, japTeams, mexTeams, turTeams, ukTeams, netTeams, taiTeams, polTeams, bulTeams, greTeams, domTeams, indTeams, argTeams, romTeams, azeTeams, sweTeams, fraTeams, botTeams, ecuTeams, surTeams, serTeams, comTeams, pakTeams, ukrTeams, phiTeams, gamTeams, czeTeams, micTeams, kazTeams, manTeams, belTeams, colTeams, croTeams,zelTeams,afgTeams,bosTeams,norTeams,itaTeams,denTeams,swiTeams,gerTeams,sinTeams,chlTeams,libTeams,uaeTeams,safTeams,armTeams,venTeams,vieTeams,zimTeams,morTeams,tonTeams,inoTeams,ethTeams,parTeams,panTeams,parTeams,lesTeams,barTeams,sokTeams
    global frcTeams, fimTeams, neTeams, pnwTeams, ontTeams, chsTeams, finTeams, fncTeams, pchTeams, fitTeams, fmaTeams, isrTeams, fscTeams, papTeams,saiTeams, dcTeams

    def fetch_teams(url, team_list, pageNum=None):
        if pageNum is not None:
            url = url.format(pageNum=pageNum)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                for team in data:
                    curTeam = [team['team_number'],team['name'], team['nickname'], team['city'], team['state_prov'], team['country']]
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

    state_country_map = {
        "alabama": alTeams, "al": alTeams, "alaska": akTeams, "ak": akTeams,"arizona": azTeams, "az": azTeams,"arkansas": arTeams, "ar": arTeams,"california": caTeams, "ca": caTeams,"colorado": coTeams, "co": coTeams, "dc": dcTeams, "district of columbia": dcTeams, "florida": flTeams, "fl": flTeams,"hawaii": hiTeams, "hi": hiTeams,"idaho": idTeams, 
        "id": idTeams,"illinois": ilTeams, "il": ilTeams,"iowa": iaTeams, "ia": iaTeams,"kansas": ksTeams, "ks": ksTeams,"kentucky": kyTeams, "ky": kyTeams,"louisiana": laTeams, "la": laTeams,"minnesota": mnTeams, "mn": mnTeams,"mississippi": msTeams, "ms": msTeams,"missouri": moTeams, "mo": moTeams,
        "montana": mtTeams, "mt": mtTeams,"nebraska": RneTeams, "ne": RneTeams,"nevada": nvTeams, "nv": nvTeams,"new mexico": nmTeams, "nm": nmTeams,"new york": nyTeams, "ny": nyTeams,"north dakota": ndTeams, "nd": ndTeams,"ohio": ohTeams, "oh": ohTeams,"oklahoma": okTeams, "ok": okTeams,
        "pennsylvania": paTeams, "pa": paTeams,"south dakota": sdTeams, "sd": sdTeams,"tennessee": tnTeams, "tn": tnTeams,"utah": utTeams, "ut": utTeams,"west virginia": wvTeams, "wv": wvTeams,"wisconsin": wiTeams, "wi": wiTeams,"wyoming": wyTeams, "wy": wyTeams,"puerto rico": prTeams, "pr": prTeams,
        "guam": guTeams,"texas": fitTeams, "tx": fitTeams,"new jersey": fmaTeams, "nj": fmaTeams,"delaware": fmaTeams, "de": fmaTeams,"massachusetts": neTeams, "ma": neTeams,"vermont": neTeams, "vt": neTeams,"rhode island": neTeams, "ri": neTeams,"maine": neTeams, "me": neTeams,"maryland": chsTeams, 
        "md": chsTeams,"new hampshire": neTeams, "nh": neTeams,"connecticut": neTeams, "ct": neTeams,"michigan": fimTeams, "mi": fimTeams,"georgia": pchTeams, "ga": pchTeams,"south carolina": pchTeams, "sc": pchTeams,"north carolina": fncTeams, "nc": fncTeams,"oregon": pnwTeams, "or": pnwTeams,
        "washington": pnwTeams, "wa": pnwTeams,"indiana": finTeams, "in": finTeams,"virginia": chsTeams, "va": chsTeams,"israel": isrTeams,"turkey": turTeams, "türkiye": turTeams,"china": chiTeams, "cn": chiTeams,"chinese taipei": taiTeams, "taiwan": taiTeams,"australia": ausTeams,"canada": canTeams,
        "united kingdom": ukTeams, "uk": ukTeams, "kingdom": ukTeams,"belize": belTeams,"ukraine": ukrTeams,"federated states of micronesia": micTeams,"kazakhstan": kazTeams,"czech republic": czeTeams,"gambia": gamTeams,"philippines": phiTeams,"pakistan": pakTeams,"comoros": comTeams,"serbia": serTeams,"suriname": surTeams,
        "ecuador": ecuTeams,"botswana": botTeams,"france": fraTeams,"sweden": sweTeams,"azerbaijan": azeTeams,"romania": romTeams,"argentina": argTeams,"india": indTeams,"dominican republic": domTeams,"greece": greTeams,"bulgaria": bulTeams,"poland": polTeams,"netherlands": netTeams,
        "mexico": mexTeams,"japan": japTeams,"brazil": braTeams,"colombia": colTeams,"croatia": croTeams,"new zealand": zelTeams,"afghanistan": afgTeams,"bosnia and herzegovina": bosTeams,"bosnia-herzegovina": bosTeams,"norway": norTeams,"italy": itaTeams,"denmark": denTeams,"switzerland": swiTeams,"germany": gerTeams,
        "singapore": sinTeams,"chile": chlTeams,"libya": libTeams,"united arab emirates": uaeTeams,"south africa": safTeams,"armenia": armTeams,"venezuela": venTeams,"vietnam": vieTeams,"zimbabwe": zimTeams,"morocco": morTeams,"tonga": tonTeams,"indonesia": inoTeams,"ethiopia": ethTeams,
        "paraguay": parTeams,"panama": panTeams,"lesotho": lesTeams,"barbados": barTeams,"south korea": sokTeams,"papua new guinea": papTeams,"saint kitts and nevis": saiTeams
    }

    for team in regionalTeams:
        country = team[5].lower() if team[5] else None
        state = team[4].lower() if team[4] else None
        city = team[3].lower() if team[3] else None

        for location in [state, city, country]:
            if location in state_country_map:
                state_country_map[location].append(team)
                break
        else:
            otherTeams.append(team)


    # Remove teams from regionalTeams that appear in other region team lists
    all_other_teams = set(tuple(team) for team_list in state_country_map.values() for team in team_list)
    regionalTeams = [team for team in regionalTeams if tuple(team) not in all_other_teams]

def checkHighScores():
    leaderboard = []
    leaderboard_hard = []

    leaderboardHardFile = 'leaderboards_hard.txt'
    leaderboardFile = 'leaderboards.txt'

    # Read the leaderboard from the file
    try:
        with open(leaderboardFile, 'r') as file:
            for line in file:
                if line.strip():  # Check if the line is not empty
                    session_id, score = line.strip().split(',')
                    leaderboard.append((session_id, int(score)))
    except FileNotFoundError:
        # Handle the case where the file does not exist
        open(leaderboardFile, 'w').close()  # Create an empty file

    try:
        with open(leaderboardHardFile, 'r') as file:
            for line in file:
                if line.strip():  # Check if the line is not empty
                    session_id, score = line.strip().split(',')
                    leaderboard_hard.append((session_id, int(score)))
    except FileNotFoundError:
        # Handle the case where the file does not exist
        open(leaderboardHardFile, 'w').close()  # Create an empty file



    # Sort the leaderboard by score in descending order and keep the top 10
    leaderboard_hard = sorted(leaderboard_hard, key=lambda x: x[1], reverse=True)[:10]
    leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)[:10]

    # Check if the session's ID is already in the leaderboard
    session_id = session.get('id')
    if session_id and session.get('username'):  # Only add if username is set
        for i, (sid, score) in enumerate(leaderboard):
            if sid == session_id:
                # Update the score if the session's ID is already in the leaderboard
                leaderboard[i] = (sid, max(score, session['highest_streak']))
                break
        else:
            # Add the session's ID to the leaderboard if it's not already there
            leaderboard.append((session_id, session['highest_streak']))
            leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)[:10]

        for i, (sid, score) in enumerate(leaderboard_hard):
            if sid == session_id:
                # Update the score if the session's ID is already in the leaderboard
                leaderboard_hard[i] = (sid, max(score, session['highest_streak_hard']))
                break
        else:
            # Add the session's ID to the leaderboard if it's not already there
            leaderboard_hard.append((session_id, session['highest_streak_hard']))
            leaderboard_hard = sorted(leaderboard_hard, key=lambda x: x[1], reverse=True)[:10]

    # Write the updated leaderboard back to the file
    with open(leaderboardFile, 'w') as file:
        for sid, score in leaderboard:
            file.write(f"{sid},{score}\n")
    
    with open(leaderboardHardFile, 'w') as file:
        for sid, score in leaderboard_hard:
            file.write(f"{sid},{score}\n")

    # Update the highest streak in ids.txt
    ids = []
    try:
        with open('ids.txt', 'r') as file:
            ids = file.readlines()
    except FileNotFoundError:
        pass

    with open('ids.txt', 'w') as file:
        for line in ids:
            if line.startswith(session_id):
                parts = line.strip().split(',')
                file.write(f"{session_id},{parts[1]},{parts[2]},{session['highest_streak']},{session['highest_streak_hard']}\n")
            else:
                file.write(line)

    return leaderboard, leaderboard_hard

def updateFiles():
        # Update ids.txt
            session_id = session['id']
            ids = []
            try:
                with open('ids.txt', 'r') as file:
                    ids = file.readlines()
            except FileNotFoundError:
                pass

            with open('ids.txt', 'w') as file:
                for line in ids:
                    if line.startswith(session_id):
                        parts = line.strip().split(',')
                        file.write(f"{session_id},{parts[1]},{parts[2]},{session['highest_streak']},{session['highest_streak_hard']}\n")
                    else:
                        file.write(line)
            
            if (session['hard_mode']):
                leaderboardFile = 'leaderboards_hard.txt'
            else:
                leaderboardFile = 'leaderboards.txt'

            # Update leaderboards.txt or leaderboards_hard.txt
            leaderboard = []
            try:
                with open(leaderboardFile, 'r') as file:
                    for line in file:
                        if line.strip():
                            sid, score = line.strip().split(',')
                            leaderboard.append((sid, int(score)))
            except FileNotFoundError:
                pass

            leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)[:10]

            for i, (sid, score) in enumerate(leaderboard):
                if sid == session_id:
                    if (session['hard_mode']):
                        leaderboard[i] = (sid, session['highest_streak_hard'])
                    else:
                        leaderboard[i] = (sid, session['highest_streak'])
                    break
            else:
                if (session['hard_mode']):
                    leaderboard.append((session_id, session['highest_streak_hard']))
                else:
                    leaderboard.append((session_id, session['highest_streak']))
                leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)[:10]

            with open(leaderboardFile, 'w') as file:
                for sid, score in leaderboard:
                    file.write(f"{sid},{score}\n")




@app.route('/')
def root():
    with app.app_context():
        ip_address = request.remote_addr

        with open('banned.txt', 'r') as file:
            banned_ips = [line.strip() for line in file.readlines()]
            if ip_address in banned_ips:
                return "Page not found."
            
        if 'id' not in session:
            session_id, username, highest_streak, highest_streak_hard = get_session_data_by_ip(ip_address)
            if session_id:
                session['id'] = session_id
                session['username'] = username
                session['highest_streak'] = highest_streak
                session['highest_streak_hard'] = highest_streak_hard
            else:
                session['id'] = generate_unique_session_id(ip_address)
                session['highest_streak'] = 0
                session['highest_streak_hard'] = 0
        else:
            session_id = session['id']
            update_ip_address_if_changed(session_id, ip_address)

        # Always check the ids.txt file for the session ID
        session_id = session['id']
        ids = []
        try:
            with open('ids.txt', 'r') as file:
                ids = file.readlines()
        except FileNotFoundError:
            pass

        id_exists = False
        for line in ids:
            parts = line.strip().split(',')
            if parts[0] == session_id:
                id_exists = True
                if int(parts[3]) != session.get('highest_streak', 0):
                    session['highest_streak'] = int(parts[3])
                if int(parts[4]) != session.get('highest_streak_hard', 0):
                    session['highest_streak_hard'] = int(parts[4])
                break

        if not id_exists:
            with open('ids.txt', 'a') as file:
                file.write(f"{session_id},{session['username']},{ip_address},{session.get('highest_streak', 0)},{session.get('highest_streak_hard', 0)}\n")


        if 'dark_mode' not in session:
            session['dark_mode'] = False
        # if 'hard_mode' not in session:
        session['hard_mode'] = False
        if 'highest_streak' not in session:
            session['highest_streak'] = 0
        if 'highest_streak_hard' not in session:
            session['highest_streak_hard'] = 0
        if 'username' not in session:
            session['username'] = None
        
        session['guessedTeams'] = []
        session['currentStreak'] = 0
        session['curTeam'] = 0
        session['curTeamName'] = "Teams Not Loaded Yet"

        session['curTeamInfo'] = "No Info"
        session['curTeamCity'] = "No City"
        session['curTeamState'] = "No State"
        session['curTeamCountry'] = "No Country"

        if 'selected_regions' not in session:
            session['selected_regions'] = ['chsTeams', 'fimTeams', 'fitTeams', 'finTeams', 'isrTeams', 'fmaTeams', 'fncTeams','fscTeams', 'neTeams', 'ontTeams', 'pnwTeams', 'pchTeams']
        if 'regional' not in session or session['regional'] == False or session['regional'] == True:
            session['regional'] = ['alTeams', 'akTeams', 'azTeams', 'arTeams', 'caTeams', 'coTeams', 'flTeams', 'hiTeams', 'idTeams', 'ilTeams', 'iaTeams', 'ksTeams', 'kyTeams', 'laTeams', 'mnTeams', 
                                'msTeams', 'moTeams', 'mtTeams', 'RneTeams', 'nvTeams', 'nmTeams', 'nyTeams', 'ndTeams', 'ohTeams', 'okTeams', 'paTeams', 'sdTeams', 'tnTeams', 'utTeams', 'wvTeams', 
                                'wiTeams', 'wyTeams', 'prTeams', 'guTeams','dcTeams', 'otherTeams', 'afgTeams', 'argTeams', 'armTeams', 'ausTeams', 'azeTeams', 'barTeams', 'belTeams', 'bosTeams', 'botTeams', 'braTeams', 
                                'bulTeams', 'canTeams', 'chlTeams', 'chiTeams', 'colTeams', 'comTeams', 'croTeams', 'czeTeams', 'denTeams', 'domTeams', 'ecuTeams', 'ethTeams', 'fraTeams', 'gamTeams', 'gerTeams', 
                                'greTeams', 'indTeams', 'inoTeams', 'itaTeams', 'japTeams', 'kazTeams', 'lesTeams', 'libTeams', 'manTeams', 'mexTeams', 'micTeams', 'morTeams', 'netTeams', 'norTeams', 'pakTeams', 
                                'panTeams','papTeams', 'parTeams', 'phiTeams', 'polTeams', 'romTeams', 'safTeams','saiTeams', 'serTeams', 'sinTeams', 'sokTeams', 'surTeams', 'sweTeams', 'swiTeams', 'taiTeams', 'tonTeams', 'turTeams', 
                                'uaeTeams', 'ukTeams', 'ukrTeams', 'venTeams', 'vieTeams', 'zimTeams', 'zelTeams']

        genRandomTeam()
        return render_template('index.html', dark_mode=session.get('dark_mode', False), hard_mode=session.get('hard_mode', False), highest_streak = session['highest_streak'],highest_streak_hard = session['highest_streak_hard'], team=session['curTeamName'], info=session.get('curTeamInfo','No Info'), selected_regions=session.get('selected_regions', []), regional=session.get('regional', []), team_name_mapping=team_name_mapping, city=session.get('curTeamCity', "No City"), state=session.get('curTeamState', "No State"), country=session.get('curTeamCountry', "No Country"))

@app.errorhandler(404)
def page_not_found(e):
    ip_address = request.remote_addr
    with open('banned.txt', 'a') as file:
        file.write(f"{ip_address}\n")
    return "Page not found.", 404

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

@app.route('/hard-mode')
def hard_mode():
    session['currentStreak'] = 0
    session['hard_mode'] = not session.get('hard_mode', False)
    genRandomTeam()
    return jsonify({'status': 'success', 'newTeamName': session['curTeamName'], 'newTeamInfo': session['curTeamInfo'], 'newTeamCity': session['curTeamCity'], 'newTeamState': session['curTeamState'], 'newTeamCountry': session['curTeamCountry'], 'streak': session['currentStreak'], 'highest_streak': session['highest_streak'], 'highest_streak_hard': session['highest_streak_hard']})

@app.route('/get-hard-mode')
def is_hard_mode():
    return jsonify({'hard_mode': session.get('hard_mode', False)})

@app.route('/update-teams', methods=['POST'])
def update_teams():
    data = request.get_json()
    session['selected_regions'] = data['regions']
    session['regional'] = data['regional']
    session['currentStreak'] = 0
    session['guessedTeams'] = []
    genRandomTeam()
    return "0"

@app.route('/gen-random-team', methods=['POST'])
def gen_random_team_route():
    genRandomTeam()

    return jsonify({'status': 'success', 'newTeamName': session['curTeamName'],'newTeamInfo': session['curTeamInfo'], 'newTeamCity': session['curTeamCity'], 'newTeamState': session['curTeamState'], 'newTeamCountry': session['curTeamCountry'], 'streak': session['currentStreak'],'highest_streak': session['highest_streak'],'highest_streak_hard': session['highest_streak_hard']})

@app.route('/set-username', methods=['POST'])
def set_username():
    data = request.get_json()
    new_name = data.get('newName')
    session_id = session.get('id')

    if not new_name:
        return jsonify({'status': 'error', 'message': 'New username is required'}), 400

    session['username'] = new_name

    # Update the username and highest streak in ids.txt
    ids = []
    try:
        with open('ids.txt', 'r') as file:
            ids = file.readlines()
    except FileNotFoundError:
        pass

    with open('ids.txt', 'w') as file:
        for line in ids:
            if line.startswith(session_id):
                parts = line.strip().split(',')
                file.write(f"{session_id},{new_name},{parts[2]},{session['highest_streak']},{session['highest_streak_hard']}\n")
            else:
                file.write(line)

    return jsonify({'status': 'success'})

@app.route('/check-team', methods=['POST'])
def check_team():
    data = request.get_json()
    try:
        teamNumber = int(data['teamNumber'])
    except:
        teamNumber = -1
    
    with app.app_context():
        match = teamNumber == session.get('curTeam',0)
        if (match and teamNumber != -1):
            if teamNumber not in session['guessedTeams']:
                session['currentStreak'] += 1
                session['guessedTeams'] = session.get('guessedTeams', []) + [session['curTeam']]
        else:
            session['currentStreak'] = 0
            session['guessedTeams'] = []
            checkHighScores()

        if session['hard_mode']:
            if session['currentStreak'] > session['highest_streak_hard']:
                session['highest_streak_hard'] = session['currentStreak']
                updateFiles()
        else:
            if session['currentStreak'] > session['highest_streak']:
                session['highest_streak'] = session['currentStreak']
                updateFiles()

            
        
        correctTeamName = session.get('curTeamName',0)
        correctTeamNumber = session.get('curTeam',0)
        genRandomTeam()
        return jsonify({'match': match, 'correctTeamNumber': correctTeamNumber,'correctTeamName': correctTeamName, 'newTeamName': session.get('curTeamName', "Teams Not Loaded Yet"), 'newTeamInfo': session.get('curTeamInfo', "No Info"),'newTeamCity': session.get('curTeamCity', "No City"), 'newTeamState': session.get('curTeamState', "No State"), 'newTeamCountry': session.get('curTeamCountry', "No Country"), 'streak': session.get('currentStreak', 0),'highest_streak': session.get('highest_streak', 0),'highest_streak_hard': session.get('highest_streak_hard', 0)})

@app.route('/get-leaderboard', methods=['GET'])
def get_leaderboard():
    leaderboard, leaderboardHard = checkHighScores()
    leaderboard_with_names = []
    hard_leaderboard_with_names = []

    for session_id, score in leaderboard:
        username = get_username_by_session_id(session_id)
        leaderboard_with_names.append((username, score))

    for session_id, score in leaderboardHard:
        username = get_username_by_session_id(session_id)
        hard_leaderboard_with_names.append((username, score))
    
    return jsonify(leaderboard_with_names,hard_leaderboard_with_names)

if __name__ == '__main__':
    getTeams()
    startWeb()