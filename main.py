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

        regional_choices = {
            0: alTeams,
            1: akTeams,
            2: azTeams,
            3: arTeams,
            4: caTeams,
            5: coTeams,
            6: flTeams,
            7: hiTeams,
            8: idTeams,
            9: ilTeams,
            10: iaTeams,
            11: ksTeams,
            12: kyTeams,
            13: laTeams,
            14: mnTeams,
            15: msTeams,
            16: moTeams,
            17: mtTeams,
            18: RneTeams,
            19: nvTeams,
            20: nmTeams,
            21: nyTeams,
            22: ndTeams,
            23: ohTeams,
            24: okTeams,
            25: paTeams,
            26: sdTeams,
            27: tnTeams,
            28: utTeams,
            29: wvTeams,
            30: wiTeams,
            31: wyTeams,
            32: prTeams,
            33: guTeams,
            34: otherTeams,

            35: ausTeams,
            36: braTeams,
            37: canTeams,
            38: chiTeams,
            39: japTeams,
            40: mexTeams,
            41: turTeams,
            42: ukTeams,
            43: netTeams,
            44: taiTeams,
            45: polTeams, 
            46: bulTeams,
            47: greTeams,
            48: domTeams,
            49: indTeams, 
            50: argTeams, 
            51: romTeams, 
            52: azeTeams, 
            53: sweTeams, 
            54: fraTeams, 
            55: botTeams, 
            56: ecuTeams, 
            57: surTeams, 
            58: serTeams, 
            59: comTeams, 
            60: pakTeams, 
            61: ukrTeams, 
            62: phiTeams,
            63: gamTeams,
            64: czeTeams,
            65: micTeams,
            66: kazTeams,
            67: manTeams,
            68: belTeams,
            69: colTeams,
            70: croTeams,
            71: zelTeams,
            72: afgTeams,
            73: bosTeams,
            74: norTeams,
            75: itaTeams,
            76: denTeams,
            77: swiTeams,
            78: gerTeams,
            79: sinTeams,
            80: chlTeams,
            81: libTeams,
            82: uaeTeams,
            83: safTeams,
            84: armTeams,
            85: venTeams,
            86: vieTeams,
            87: zimTeams,
            88: morTeams,
            89: tonTeams,
            90: inoTeams,
            91: ethTeams,
            92: parTeams,
            93: panTeams,
            94: parTeams,
            95: lesTeams,
            96: barTeams,
            97: sokTeams
        }

        try:
            if random.choice([True, False]) and session.get('regional'):
                #regional
                session['choice'] = random.choice(session['regional'])

                team_list = globals()[session['choice']]
            else:
                #district
                session['choice'] = random.choice(session['selected_regions'])

                team_list = globals()[session['choice']]

            if team_list:
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
            session['selected_regions'] = ['chesapeake', 'michigan', 'texas', 'indiana', 'israel', 'mid-atlantic', 'northcarolina', 'newengland', 'ontario', 'pacificnorthwest', 'peachtree']
        if 'regional' not in session:
            session['regional'] = True
        
        genRandomTeam()
        return render_template('index.html', dark_mode=session.get('dark_mode', False), team=session['curTeamName'], selected_regions=session.get('selected_regions', []), regional=session.get('regional', False), city=session.get('curTeamCity', "No City"), state=session.get('curTeamState', "No State"), country=session.get('curTeamCountry', "No Country"))
    
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

    # Sort regional teams into their respective state or country
    for team in regionalTeams:
        country = team[4]
        try:
            state = team[3].lower()
        except:
            state = None
        try:
            state2 = team[2].lower()
        except:
            state2 = None

        states = [state2, country, state]
        for state in states:
            if state != None:
                match state:
                    case "alabama" | "al":
                        alTeams.append(team)
                        pass
                    case "alaska" | "ak":
                        akTeams.append(team)
                        pass
                    case "arizona" | "az":
                        azTeams.append(team)
                        pass
                    case "arkansas" | "ar":
                        arTeams.append(team)
                        pass
                    case "california" | "ca":
                        caTeams.append(team)
                        pass
                    case "colorado" | "co":
                        coTeams.append(team)
                        pass
                    case "florida" | "fl":
                        flTeams.append(team)
                        pass
                    case "hawaii" | "hi":
                        hiTeams.append(team)
                        pass
                    case "idaho" | "id":
                        idTeams.append(team)
                        pass
                    case "illinois" | "il":
                        ilTeams.append(team)
                        pass
                    case "iowa" | "ia":
                        iaTeams.append(team)
                        pass
                    case "kansas" | "ks":
                        ksTeams.append(team)
                        pass
                    case "kentucky" | "ky":
                        kyTeams.append(team)
                        pass
                    case "louisiana" | "la":
                        laTeams.append(team)
                        pass
                    case "minnesota" | "mn":
                        mnTeams.append(team)
                        pass
                    case "mississippi" | "ms":
                        msTeams.append(team)
                        pass
                    case "missouri" | "mo":
                        moTeams.append(team)
                        pass
                    case "montana" | "mt":
                        mtTeams.append(team)
                        pass
                    case "nebraska" | "ne":
                        RneTeams.append(team)
                        pass
                    case "nevada" | "nv":
                        nvTeams.append(team)
                        pass
                    case "new mexico" | "nm":
                        nmTeams.append(team)
                        pass
                    case "new york" | "ny":
                        nyTeams.append(team)
                        pass
                    case "north dakota" | "nd":
                        ndTeams.append(team)
                        pass
                    case "ohio" | "oh":
                        ohTeams.append(team)
                        pass
                    case "oklahoma" | "ok":
                        okTeams.append(team)
                        pass
                    case "pennsylvania" | "pa":
                        paTeams.append(team)
                        pass
                    case "south dakota" | "sd":
                        sdTeams.append(team)
                        pass
                    case "tennessee" | "tn":
                        tnTeams.append(team)
                        pass
                    case "utah" | "ut":
                        utTeams.append(team)
                        pass
                    case "west virginia" | "wv":
                        wvTeams.append(team)
                        pass
                    case "wisconsin" | "wi":
                        wiTeams.append(team)
                        pass
                    case "wyoming" | "wy":
                        wyTeams.append(team)
                        pass
                    case "puerto rico" | "pr":
                        prTeams.append(team)
                        pass
                    case "guam":
                        guTeams.append(team)
                        pass
                    case "texas" | "tx":
                        fitTeams.append(team)
                        pass
                    case "new jersey" | "nj":
                        fmaTeams.append(team)
                        pass
                    case "delaware" | "de":
                        fmaTeams.append(team)
                        pass
                    case "massachusetts" | "ma":
                        neTeams.append(team)
                        pass
                    case "vermont" | "vt":
                        neTeams.append(team)
                        pass
                    case "rhode island" | "ri":
                        neTeams.append(team)
                        pass
                    case "maine" | "me":
                        neTeams.append(team)
                        pass
                    case "maryland" | "md":
                        neTeams.append(team)
                        pass
                    case "new hampshire" | "nh":
                        neTeams.append(team)
                        pass
                    case "conneticut" | "ct":
                        neTeams.append(team)
                        pass
                    case "michigan" | "mi":
                        fimTeams.append(team)
                        pass
                    case "georgia" | "ga":
                        pchTeams.append(team)
                        pass
                    case "south carolina" | "sc": #Change for 2025 to be south carolina district
                        pchTeams.append(team)
                        pass
                    case "north carolina" | "nc":
                        fncTeams.append(team)
                        pass
                    case "oregon" | "or":
                        pnwTeams.append(team)
                        pass
                    case "washington" | "wa":
                        pnwTeams.append(team)
                        pass
                    case "indiana" | "in":
                        finTeams.append(team)
                        pass
                    case "virginia" | "va" if state != "west virginia":
                        chsTeams.append(team)
                        pass
                    case "Israel":
                        isrTeams.append(team)
                        pass
                    case "Turkey" | "Türkiye":
                        turTeams.append(team)
                        pass
                    case "China" | "cn":
                        chiTeams.append(team)
                        pass
                    case "Chinese Taipei" | "Taiwan":
                        taiTeams.append(team)
                        pass
                    case "Australia":
                        ausTeams.append(team)
                        pass
                    case "Canada":
                        canTeams.append(team)
                        pass
                    case "Kingdom" | "UK" | "United Kingdom":
                        ukTeams.append(team)
                        pass
                    case "Belize":
                        belTeams.append(team)
                        pass
                    case "Ukraine":
                        ukrTeams.append(team)
                        pass
                    case "Federated States of Micronesia":
                        micTeams.append(team)
                        pass
                    case "Kazakhstan":
                        kazTeams.append(team)
                        pass
                    case "Czech Republic":
                        czeTeams.append(team)
                        pass
                    case "Gambia":
                        gamTeams.append(team)
                        pass
                    case "Philippines":
                        phiTeams.append(team)
                        pass
                    case "Pakistan":
                        pakTeams.append(team)
                        pass
                    case "Comoros":
                        comTeams.append(team)
                        pass
                    case "Serbia":
                        serTeams.append(team)
                        pass
                    case "Suriname":
                        surTeams.append(team)
                        pass
                    case "Ecuador":
                        ecuTeams.append(team)
                        pass
                    case "Botswana":
                        botTeams.append(team)
                        pass
                    case "France":
                        fraTeams.append(team)
                        pass
                    case "Sweden":
                        sweTeams.append(team)
                        pass
                    case "Azerbaijan":
                        azeTeams.append(team)
                        pass
                    case "Romania":
                        romTeams.append(team)
                        pass
                    case "Argentina":
                        argTeams.append(team)
                        pass
                    case "India":
                        indTeams.append(team)
                        pass
                    case "Dominican Republic":
                        domTeams.append(team)
                        pass
                    case "Greece":
                        greTeams.append(team)
                        pass
                    case "Bulgaria":
                        bulTeams.append(team)
                        pass
                    case "Poland":
                        polTeams.append(team)
                        pass
                    case "Netherlands":
                        netTeams.append(team)
                        pass
                    case "Mexico":
                        mexTeams.append(team)
                        pass
                    case "Japan":
                        japTeams.append(team)
                        pass
                    case "Brazil":
                        braTeams.append(team)
                        pass
                    case "Colombia":
                        colTeams.append(team)
                        pass
                    case "Croatia":
                        croTeams.append(team)
                        pass
                    case "New Zealand":
                        zelTeams.append(team)
                        pass
                    case "Afghanistan":
                        afgTeams.append(team)
                        pass
                    case "Bosnia and Herzegovina":
                        bosTeams.append(team)
                        pass
                    case "Norway":
                        norTeams.append(team)
                        pass
                    case "Italy":
                        itaTeams.append(team)
                        pass
                    case "Denmark":
                        denTeams.append(team)
                        pass
                    case "Switzerland":
                        swiTeams.append(team)
                        pass
                    case "Germany":
                        gerTeams.append(team)
                        pass
                    case "Singapore":
                        sinTeams.append(team)
                        pass
                    case "Chile":
                        chlTeams.append(team)
                        pass
                    case "Libya":
                        libTeams.append(team)
                        pass
                    case "United Arab Emirates":
                        uaeTeams.append(team)
                        pass
                    case "South Africa":
                        safTeams.append(team)
                        pass
                    case "Armenia":
                        armTeams.append(team)
                        pass
                    case "Venezuela":
                        venTeams.append(team)
                        pass
                    case "Vietnam":
                        vieTeams.append(team)
                        pass
                    case "Zimbabwe":
                        zimTeams.append(team)
                        pass
                    case "Morocco":
                        morTeams.append(team)
                        pass
                    case "Tonga":
                        tonTeams.append(team)
                        pass
                    case "Indonesia":
                        inoTeams.append(team)
                        pass
                    case "Ethiopia":
                        ethTeams.append(team)
                        pass
                    case "Paraguay":
                        parTeams.append(team)
                        pass
                    case "Panama":
                        panTeams.append(team)
                        pass
                    case "Lesotho":
                        lesTeams.append(team)
                        pass
                    case "Barbados":
                        barTeams.append(team)
                        pass
                    case "South Korea":
                        sokTeams.append(team)
                        pass

            else:
                if states[0] == None and states[1] == None and states[2] == None:
                    otherTeams.append(team)
    
    # Remove teams from regionalTeams that appear in other region team lists
    all_other_teams = set(tuple(team) for team_list in [alTeams, akTeams, azTeams, arTeams, caTeams, coTeams, flTeams, hiTeams, idTeams, ilTeams, iaTeams, ksTeams, kyTeams, laTeams, mnTeams, msTeams, moTeams, mtTeams, RneTeams, nvTeams, nmTeams, nyTeams, ndTeams, ohTeams, okTeams, paTeams, sdTeams, tnTeams, utTeams, wvTeams, wiTeams, wyTeams, prTeams, ausTeams, braTeams, canTeams, chiTeams, japTeams, mexTeams, turTeams, ukTeams, netTeams, taiTeams, polTeams, bulTeams, greTeams, domTeams, indTeams, argTeams, romTeams, azeTeams, sweTeams, fraTeams, botTeams, ecuTeams, surTeams, serTeams, comTeams, pakTeams, ukrTeams, phiTeams, gamTeams, czeTeams, micTeams, kazTeams, fmaTeams, fitTeams, pnwTeams, neTeams, pchTeams, fncTeams, finTeams, isrTeams, fimTeams, ontTeams, chsTeams, guTeams, belTeams, colTeams,croTeams,zelTeams,afgTeams,bosTeams,norTeams,itaTeams,denTeams,swiTeams,gerTeams,sinTeams,chlTeams,libTeams,uaeTeams,safTeams,armTeams,venTeams,vieTeams,zimTeams,morTeams,tonTeams,inoTeams,ethTeams,parTeams, panTeams,lesTeams,barTeams,sokTeams, otherTeams] for team in team_list)
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