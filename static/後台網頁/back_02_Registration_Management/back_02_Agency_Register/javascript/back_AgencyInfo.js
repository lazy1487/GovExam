
document.addEventListener('DOMContentLoaded', (event) => {
    const agencyIDValue = document.getElementById('AgencyID').textContent.trim();

    const hiddenAgencyIDInput = document.querySelector('input[name="hiddenAgencyID"]');
    if (hiddenAgencyIDInput) {
        hiddenAgencyIDInput.value = agencyIDValue;
        hiddenAgencyIDInput.setAttribute('value', agencyIDValue);
    }
});