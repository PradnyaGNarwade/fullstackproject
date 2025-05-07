document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("toggleModeBtn");
  
    toggleBtn.addEventListener("click", function () {
      // Toggle a class on the <body>
      document.body.classList.toggle("dark-mode");
  
      // Optional: Update button text
      if (document.body.classList.contains("dark-mode")) {
        toggleBtn.textContent = "Toggle Light Mode";
      } else {
        toggleBtn.textContent = "Toggle Dark Mode";
      }
    });
  });
  