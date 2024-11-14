import requests
from flask import Flask, jsonify, session, request, render_template, send_from_directory
import concurrent.futures
import random
from datetime import datetime
from datetime import timedelta

app = Flask(__name__, static_folder='static')

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
    'wiTeams': 'Wisconsin', 'wyTeams': 'Wyoming', 'prTeams': 'Puerto Rico', 'guTeams': 'Guam', 'otherTeams': 'Other',
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
    'lesTeams': 'Lesotho', 'barTeams': 'Barbados', 'sokTeams': 'South Korea'
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
                session['curTeamName'] = team[1]
                session['curTeamCity'] = team[2].split(", ")[0]

                try:
                    session['curTeamState'] = team[2].split(", ")[1]
                except:
                    session['curTeamState'] = team[3]

                session['curTeamCountry'] = team[4]

        except:
            print("excepted")
            session['curTeam'] = -1
            session['curTeamName'] = "No Teams Loaded"
            session['curTeamCity'] = "No City"
            session['curTeamState'] = "No State"
            session['curTeamCountry'] = "No Country"
        
        

@app.route('/')
def root():
    with app.app_context():
        if 'dark_mode' not in session:
            session['dark_mode'] = False
        
        session['curTeam'] = 0
        session['curTeamName'] = "Teams Not Loaded Yet"

        session['curTeamCity'] = "No City"
        session['curTeamState'] = "No State"
        session['curTeamCountry'] = "No Country"

        if 'selected_regions' not in session:
            session['selected_regions'] = ['chsTeams', 'fimTeams', 'fitTeams', 'finTeams', 'isrTeams', 'fmaTeams', 'fncTeams','fscTeams', 'neTeams', 'ontTeams', 'pnwTeams', 'pchTeams']
        if 'regional' not in session:
            session['regional'] = ['alTeams', 'akTeams', 'azTeams', 'arTeams', 'caTeams', 'coTeams', 'flTeams', 'hiTeams', 'idTeams', 'ilTeams', 'iaTeams', 'ksTeams', 'kyTeams', 'laTeams', 'mnTeams', 
                                'msTeams', 'moTeams', 'mtTeams', 'RneTeams', 'nvTeams', 'nmTeams', 'nyTeams', 'ndTeams', 'ohTeams', 'okTeams', 'paTeams', 'sdTeams', 'tnTeams', 'utTeams', 'wvTeams', 
                                'wiTeams', 'wyTeams', 'prTeams', 'guTeams', 'otherTeams', 'ausTeams', 'braTeams', 'canTeams', 'chiTeams', 'japTeams', 'mexTeams', 'turTeams', 'ukTeams', 'netTeams', 'taiTeams', 
                                'polTeams', 'bulTeams', 'greTeams', 'domTeams', 'indTeams', 'argTeams', 'romTeams', 'azeTeams', 'sweTeams', 'fraTeams', 'botTeams', 'ecuTeams', 'surTeams', 'serTeams', 'comTeams', 
                                'pakTeams', 'ukrTeams', 'phiTeams', 'gamTeams', 'czeTeams', 'micTeams', 'kazTeams', 'manTeams', 'belTeams', 'colTeams', 'croTeams', 'zelTeams', 'afgTeams', 'bosTeams', 'norTeams', 
                                'itaTeams', 'denTeams', 'swiTeams', 'gerTeams', 'sinTeams', 'chlTeams', 'libTeams', 'uaeTeams', 'safTeams', 'armTeams', 'venTeams', 'vieTeams', 'zimTeams', 'morTeams', 'tonTeams', 
                                'inoTeams', 'ethTeams', 'parTeams', 'panTeams', 'lesTeams', 'barTeams', 'sokTeams']

        genRandomTeam()
        return render_template('index.html', dark_mode=session.get('dark_mode', False), team=session['curTeamName'], selected_regions=session.get('selected_regions', []), regional=session.get('regional', []), team_name_mapping=team_name_mapping, city=session.get('curTeamCity', "No City"), state=session.get('curTeamState', "No State"), country=session.get('curTeamCountry', "No Country"))
    
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
        return jsonify({'match': match, 'correctTeamNumber': correctTeamNumber, 'newTeamName': session.get('curTeamName', "Teams Not Loaded Yet"), 'newTeamCity': session.get('curTeamCity', "No City"), 'newTeamState': session.get('curTeamState', "No State"), 'newTeamCountry': session.get('curTeamCountry', "No Country")})

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
    global regionalTeams, alTeams, akTeams, azTeams,  arTeams, caTeams, coTeams, flTeams, hiTeams, idTeams, ilTeams, iaTeams, ksTeams, kyTeams, laTeams, mnTeams, msTeams, moTeams, mtTeams, RneTeams, nvTeams, nmTeams, nyTeams, ndTeams, ohTeams, okTeams, paTeams, sdTeams, tnTeams, utTeams, wvTeams, wiTeams, wyTeams, otherTeams
    global ausTeams, braTeams, canTeams, chiTeams, japTeams, mexTeams, turTeams, ukTeams, netTeams, taiTeams, polTeams, bulTeams, greTeams, domTeams, indTeams, argTeams, romTeams, azeTeams, sweTeams, fraTeams, botTeams, ecuTeams, surTeams, serTeams, comTeams, pakTeams, ukrTeams, phiTeams, gamTeams, czeTeams, micTeams, kazTeams, manTeams, belTeams, colTeams, croTeams,zelTeams,afgTeams,bosTeams,norTeams,itaTeams,denTeams,swiTeams,gerTeams,sinTeams,chlTeams,libTeams,uaeTeams,safTeams,armTeams,venTeams,vieTeams,zimTeams,morTeams,tonTeams,inoTeams,ethTeams,parTeams,panTeams,parTeams,lesTeams,barTeams,sokTeams
    global frcTeams, fimTeams, neTeams, pnwTeams, ontTeams, chsTeams, finTeams, fncTeams, pchTeams, fitTeams, fmaTeams, isrTeams, fscTeams

    def fetch_teams(url, team_list, pageNum=None):
        if pageNum is not None:
            url = url.format(pageNum=pageNum)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                for team in data:
                    curTeam = [team['team_number'], team['nickname'], team['city'], team['state_prov'], team['country']]
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
        "alabama": alTeams, "al": alTeams, "alaska": akTeams, "ak": akTeams,"arizona": azTeams, "az": azTeams,"arkansas": arTeams, "ar": arTeams,"california": caTeams, "ca": caTeams,"colorado": coTeams, "co": coTeams,"florida": flTeams, "fl": flTeams,"hawaii": hiTeams, "hi": hiTeams,"idaho": idTeams, 
        "id": idTeams,"illinois": ilTeams, "il": ilTeams,"iowa": iaTeams, "ia": iaTeams,"kansas": ksTeams, "ks": ksTeams,"kentucky": kyTeams, "ky": kyTeams,"louisiana": laTeams, "la": laTeams,"minnesota": mnTeams, "mn": mnTeams,"mississippi": msTeams, "ms": msTeams,"missouri": moTeams, "mo": moTeams,
        "montana": mtTeams, "mt": mtTeams,"nebraska": RneTeams, "ne": RneTeams,"nevada": nvTeams, "nv": nvTeams,"new mexico": nmTeams, "nm": nmTeams,"new york": nyTeams, "ny": nyTeams,"north dakota": ndTeams, "nd": ndTeams,"ohio": ohTeams, "oh": ohTeams,"oklahoma": okTeams, "ok": okTeams,
        "pennsylvania": paTeams, "pa": paTeams,"south dakota": sdTeams, "sd": sdTeams,"tennessee": tnTeams, "tn": tnTeams,"utah": utTeams, "ut": utTeams,"west virginia": wvTeams, "wv": wvTeams,"wisconsin": wiTeams, "wi": wiTeams,"wyoming": wyTeams, "wy": wyTeams,"puerto rico": prTeams, "pr": prTeams,
        "guam": guTeams,"texas": fitTeams, "tx": fitTeams,"new jersey": fmaTeams, "nj": fmaTeams,"delaware": fmaTeams, "de": fmaTeams,"massachusetts": neTeams, "ma": neTeams,"vermont": neTeams, "vt": neTeams,"rhode island": neTeams, "ri": neTeams,"maine": neTeams, "me": neTeams,"maryland": neTeams, 
        "md": neTeams,"new hampshire": neTeams, "nh": neTeams,"conneticut": neTeams, "ct": neTeams,"michigan": fimTeams, "mi": fimTeams,"georgia": pchTeams, "ga": pchTeams,"south carolina": pchTeams, "sc": pchTeams,"north carolina": fncTeams, "nc": fncTeams,"oregon": pnwTeams, "or": pnwTeams,
        "washington": pnwTeams, "wa": pnwTeams,"indiana": finTeams, "in": finTeams,"virginia": chsTeams, "va": chsTeams,"israel": isrTeams,"turkey": turTeams, "türkiye": turTeams,"china": chiTeams, "cn": chiTeams,"chinese taipei": taiTeams, "taiwan": taiTeams,"australia": ausTeams,"canada": canTeams,
        "united kingdom": ukTeams, "uk": ukTeams,"belize": belTeams,"ukraine": ukrTeams,"federated states of micronesia": micTeams,"kazakhstan": kazTeams,"czech republic": czeTeams,"gambia": gamTeams,"philippines": phiTeams,"pakistan": pakTeams,"comoros": comTeams,"serbia": serTeams,"suriname": surTeams,
        "ecuador": ecuTeams,"botswana": botTeams,"france": fraTeams,"sweden": sweTeams,"azerbaijan": azeTeams,"romania": romTeams,"argentina": argTeams,"india": indTeams,"dominican republic": domTeams,"greece": greTeams,"bulgaria": bulTeams,"poland": polTeams,"netherlands": netTeams,
        "mexico": mexTeams,"japan": japTeams,"brazil": braTeams,"colombia": colTeams,"croatia": croTeams,"new zealand": zelTeams,"afghanistan": afgTeams,"bosnia and herzegovina": bosTeams,"norway": norTeams,"italy": itaTeams,"denmark": denTeams,"switzerland": swiTeams,"germany": gerTeams,
        "singapore": sinTeams,"chile": chlTeams,"libya": libTeams,"united arab emirates": uaeTeams,"south africa": safTeams,"armenia": armTeams,"venezuela": venTeams,"vietnam": vieTeams,"zimbabwe": zimTeams,"morocco": morTeams,"tonga": tonTeams,"indonesia": inoTeams,"ethiopia": ethTeams,
        "paraguay": parTeams,"panama": panTeams,"lesotho": lesTeams,"barbados": barTeams,"south korea": sokTeams
    }

    for team in regionalTeams:
        country = team[4].lower() if team[4] else None
        state = team[3].lower() if team[3] else None
        city = team[2].lower() if team[2] else None

        for location in [city, state, country]:
            if location in state_country_map:
                state_country_map[location].append(team)
                break
        else:
            otherTeams.append(team)

    print(sokTeams)
    # Remove teams from regionalTeams that appear in other region team lists
    all_other_teams = set(tuple(team) for team_list in state_country_map.values() for team in team_list)
    regionalTeams = [team for team in regionalTeams if tuple(team) not in all_other_teams]

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
    return jsonify({'status': 'success', 'newTeamName': session['curTeamName'], 'newTeamCity': session['curTeamCity'], 'newTeamState': session['curTeamState'], 'newTeamCountry': session['curTeamCountry']})

def startWeb():
    app.run(host='0.0.0.0', port=81)


if __name__ == '__main__':
    getTeams()
    startWeb()