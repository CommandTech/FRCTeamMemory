const submitButton = document.getElementById('submit-button');
const usernameButton = document.getElementById('submit-username');
const textBox = document.getElementById('team-input');
const teamName = document.getElementById('team-name');
const teamInfo = document.getElementById('team-info');
const teamLocation = document.getElementById('team-location');
const currentStreak = document.getElementById('streak');
const highestStreak = document.getElementById('highestStreak');

const regionalCheckbox = document.getElementById('regional');
const districtCheckbox = document.getElementById('district');
const regionCheckboxes = document.querySelectorAll('#chsTeams, #fimTeams, #fitTeams, #finTeams, #isrTeams, #fmaTeams, #fncTeams, #fscTeams, #neTeams, #ontTeams, #pnwTeams, #pchTeams');
const regionalCheckboxes = document.querySelectorAll('#alTeams, #akTeams, #azTeams, #arTeams, #caTeams, #coTeams, #flTeams, #hiTeams, #idTeams, #ilTeams, #iaTeams, #ksTeams,#kyTeams, #laTeams, #mnTeams, #msTeams, #moTeams, #mtTeams, #RneTeams, #nvTeams, #nmTeams, #nyTeams, #ndTeams, #ohTeams, #okTeams, #paTeams, #sdTeams, #tnTeams, #utTeams, #wvTeams, #wiTeams, #wyTeams, #prTeams, #guTeams, #otherTeams, #ausTeams, #braTeams, #canTeams, #chiTeams, #japTeams, #mexTeams, #turTeams, #ukTeams, #netTeams, #taiTeams, #polTeams, #bulTeams, #greTeams, #domTeams, #indTeams, #argTeams, #romTeams, #azeTeams, #sweTeams, #fraTeams, #botTeams, #ecuTeams, #surTeams, #serTeams, #comTeams, #pakTeams, #ukrTeams, #phiTeams, #gamTeams, #czeTeams, #micTeams, #kazTeams, #manTeams, #belTeams, #colTeams, #croTeams, #zelTeams, #afgTeams, #bosTeams, #norTeams, #itaTeams, #denTeams, #swiTeams, #gerTeams, #sinTeams, #chlTeams, #libTeams, #uaeTeams, #safTeams, #armTeams, #venTeams, #vieTeams, #zimTeams, #morTeams, #tonTeams, #inoTeams, #ethTeams, #parTeams, #panTeams, #lesTeams, #barTeams, #sokTeams, #saiTeams,#papTeams,#dcTeams');

var hardMode = false;

document.addEventListener('DOMContentLoaded', (event) => {
    let isSubmitting = false;

    function submitForm() {
        if (isSubmitting) return;

        isSubmitting = true;
        const teamNumber = textBox.value;

        fetch('/check-team', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ teamNumber: teamNumber })
        })
        .then(response => response.json())
        .then(data => {
            const prevColor = teamName.style.color;
            currentStreak.textContent = "Streak: " + data.streak;
            highestStreak.textContent = "Highest Streak: " + data.highest_streak;
            if (data.match) {
                textBox.style.color = 'green';
                teamName.style.color = 'green';

                if (hardMode) {
                    teamName.textContent = data.correctTeamName + ' - ' + data.correctTeamNumber;
                }
            } else {
                textBox.style.color = 'red';
                teamName.style.color = 'red';
                
                if (hardMode) {
                    teamName.textContent = data.correctTeamName + ' - ' + data.correctTeamNumber;
                }else{
                    teamName.textContent = teamName.textContent + ' - ' + data.correctTeamNumber;
                }
            }

            // Wait for 2 seconds before resetting the text box and updating the team name
            setTimeout(() => {
                // Reset the text box color and value
                textBox.value = '';
                textBox.style.color = prevColor;

                // Update the team name and reset its color
                if (hardMode) {
                    teamName.textContent = "";
                }else{
                    teamName.textContent = data.newTeamName;
                }
                teamName.style.color = prevColor;

                teamLocation.textContent = data.newTeamCity + ', ' + data.newTeamState + ', ' + data.newTeamCountry;
                teamInfo.textContent = data.newTeamInfo;

                isSubmitting = false;
            }, 2000); // 2000 milliseconds = 2 seconds
        });
    }

    function updateTeams() {
        const selectedRegions = Array.from(regionCheckboxes)
            .filter(cb => cb.checked)
            .map(cb => cb.id);
        const selectedRegionals = Array.from(regionalCheckboxes)
            .filter(cb => cb.checked)
            .map(cb => cb.id);


        fetch('/update-teams', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                regions: selectedRegions,
                regional: selectedRegionals
            })
        })
        .then(response => response.json())
        .then(data => {
            reloadPage();
        })
    }

    submitButton.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent form submission
        submitForm();
    });

    textBox.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault(); // Prevent form submission
            submitForm();
        }
    });


    regionalCheckbox.addEventListener('change', () => {
        if (regionalCheckbox.checked) {
            regionalCheckboxes.forEach(cb => cb.checked = true);
        } else {
            regionalCheckboxes.forEach(cb => cb.checked = false);
        }
        updateTeams();
    });
    
    regionalCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            if (Array.from(regionalCheckboxes).some(cb => cb.checked)) {
                regionalCheckbox.checked = true;
            } else {
                regionalCheckbox.checked = false;
            }
            updateTeams();
        });
    });

    districtCheckbox.addEventListener('change', () => {
        if (districtCheckbox.checked) {
            regionCheckboxes.forEach(cb => cb.checked = true);
        }else{
            regionCheckboxes.forEach(cb => cb.checked = false);
        }
        updateTeams();
    });
    regionCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            if (Array.from(regionCheckboxes).some(cb => cb.checked)) {
                districtCheckbox.checked = true;
            }else{
                districtCheckbox.checked = false;
            }
            updateTeams();
        });
    });
});

function reloadPage() {
    fetch('/gen-random-team', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            if (hardMode) {
                teamName.textContent = "";
            }else{
                teamName.textContent = data.newTeamName;
            }
            currentStreak.textContent = "Streak: " + data.streak;
            teamLocation.textContent = data.newTeamCity + ', ' + data.newTeamState + ', ' + data.newTeamCountry;

            teamInfo.textContent = data.newTeamInfo;
        }
    })
    .catch(error => console.error('Error:', error));
}

document.getElementById('darkModeSwitch').addEventListener('change', function() {
    fetch('/dark-mode');
    document.body.classList.toggle('dark-mode');
});

document.getElementById('hardModeSwitch').addEventListener('change', function() {
    hardMode = !hardMode;
    reloadPage();
});

document.getElementById('team-input').addEventListener('input', function (e) {
    if (this.value.length > 5) {
        this.value = this.value.slice(0, 5);
    }
    let value = this.value;
    if (isNaN(parseInt(value))) {
        this.value = value.slice(0, -1);
    }
});

document.getElementById('filterButton').addEventListener('click', function() {
    var sidebar = document.getElementById('sidebar');
    var body = document.body;
    if (sidebar.classList.contains('hidden')) {
        sidebar.classList.remove('hidden');
        body.classList.add('sidebar-visible');
    } else {
        sidebar.classList.add('hidden');
        body.classList.remove('sidebar-visible');
    }
});

document.getElementById('leaderboardButton').addEventListener('click', function() {
    var leaderboard = document.getElementById('leaderboard');
    var body = document.body;
    if (leaderboard.classList.contains('hidden')) {
        leaderboard.classList.remove('hidden');
        leaderboard.classList.add('visible');
        body.classList.add('leaderboard-visible');
    } else {
        leaderboard.classList.remove('visible');
        leaderboard.classList.add('hidden');
        body.classList.remove('leaderboard-visible');
    }
});


function setName(){
    const usernameInput = document.getElementById('username-input');
    const username = usernameInput.value.trim();
    
    fetch('/set-username', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: username
        })
    })
    .then(response => response.json())
    .then(data => {
        usernameInput.value = "";
    })
}

usernameButton.addEventListener('click', (event) => {
    event.preventDefault();
    setName();
});

usernameButton.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        event.preventDefault();
        setName();
    }
});