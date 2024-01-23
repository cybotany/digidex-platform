function toggleJournalEntry() {
  console.log("Toggle function called");
  var journalEntry = document.getElementById('journalEntry');
  var toggleIcon = document.getElementById('toggleIcon');

  if (journalEntry.style.display === 'none' || journalEntry.style.display === '') {
      journalEntry.style.display = 'block';
      toggleIcon.classList.add('rotate-icon');
  } else {
      journalEntry.style.display = 'none';
      toggleIcon.classList.remove('rotate-icon');
  }
}
