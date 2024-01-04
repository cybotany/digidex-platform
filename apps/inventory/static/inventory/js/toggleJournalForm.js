function toggleJournalForm() {
    var form = document.getElementById('journalForm');
    var icon = document.getElementById('toggleIcon');

    if (form.style.display === 'none') {
        form.style.display = 'block';
        icon.classList.add('rotate-icon');
    } else {
        form.style.display = 'none';
        icon.classList.remove('rotate-icon');
    }
}
