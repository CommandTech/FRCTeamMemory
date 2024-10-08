document.addEventListener('DOMContentLoaded', (event) => {
    const submitButton = document.getElementById('submit-button');
    const textBox = document.getElementById('team-input');
    const teamName = document.getElementById('team-name');

    const regionalCheckbox = document.getElementById('regional');
    const districtCheckbox = document.getElementById('district');
    const regionCheckboxes = document.querySelectorAll('#chesapeake, #michigan, #texas, #indiana, #isreal, #mid-atlantic, #northcarolina, #newengland, #ontario, #pacificnorthwest, #peachtree');

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
            if (data.match) {
                textBox.style.color = 'green';
                teamName.style.color = 'green';
            } else {
                textBox.style.color = 'red';
                teamName.style.color = 'red';
                teamName.textContent = teamName.textContent + ' - ' + data.correctTeamNumber;
            }

            // Wait for 2 seconds before resetting the text box and updating the team name
            setTimeout(() => {
                // Reset the text box color and value
                textBox.value = '';
                textBox.style.color = 'black';

                // Update the team name and reset its color
                teamName.textContent = data.newTeamName;
                teamName.style.color = 'black';

                isSubmitting = false;
            }, 2000); // 2000 milliseconds = 2 seconds
        });
    }

    function updateTeams() {
        const selectedRegions = Array.from(regionCheckboxes)
            .filter(cb => cb.checked)
            .map(cb => cb.id);

        fetch('/update-teams', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                regions: selectedRegions,
                regional: regionalCheckbox.checked
            })
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
    districtCheckbox.addEventListener('change', () => {
            if (districtCheckbox.checked) {
                regionCheckboxes.forEach(cb => cb.checked = true);
            }else{
                regionCheckboxes.forEach(cb => cb.checked = false);
            }
            updateTeams();
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
            const teamName = document.getElementById('team-name');
            teamName.textContent = data.newTeamName;
        }
    })
    .catch(error => console.error('Error:', error));
}

document.getElementById('darkModeSwitch').addEventListener('change', function() {
    fetch('/dark-mode');
    document.body.classList.toggle('dark-mode');
});