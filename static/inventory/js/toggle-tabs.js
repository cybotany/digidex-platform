document.addEventListener('DOMContentLoaded', function () {
    setInitialActiveTab();

    const tabs = document.querySelectorAll('.tab-heading');
    const tabContents = document.querySelectorAll('.tab-content');
  
    tabs.forEach(tab => {
      tab.addEventListener('click', function() {
        const target = document.querySelector(tab.dataset.tabTarget);
        const activeColor = window.getComputedStyle(tab).backgroundColor;
  
        // Remove active class from all tabs and contents
        tabs.forEach(t => {
          t.classList.remove('active');
        });
        tabContents.forEach(c => {
          c.classList.remove('active');
          c.style.backgroundColor = ""; // Reset background color
        });
  
        // Add active class to clicked tab and its content
        tab.classList.add('active');
        target.classList.add('active');
        target.style.backgroundColor = activeColor; // Apply active tab's background color to content
      });
    });
  });

  function setInitialActiveTab() {
      const initialActiveTab = document.querySelector('.tab-heading.active');
      if (initialActiveTab) {
          const target = document.querySelector(initialActiveTab.dataset.tabTarget);
          const activeColor = window.getComputedStyle(initialActiveTab).backgroundColor;
          if (target) {
              target.style.backgroundColor = activeColor;
          }
      }
  }