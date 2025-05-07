
    // Wait for the page to load
document.addEventListener("DOMContentLoaded", function () {
    // DOM references
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const emailError = document.getElementById("emailError");
    const passwordError = document.getElementById("passwordError");
    const form = document.getElementById("signupForm");
  
    // Email validation logic
    emailInput.addEventListener("input", function () {
      const emailValue = emailInput.value.trim();
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  
      if (emailValue === "") {
        emailError.textContent = "Email is required.";
      } else if (!emailPattern.test(emailValue)) {
        emailError.textContent = "Invalid email format.";
      } else {
        emailError.textContent = "";
      }
    });
  
    // Password validation logic
    passwordInput.addEventListener("input", function () {
      const passwordValue = passwordInput.value;
  
      if (passwordValue.length < 6) {
        passwordError.textContent = "Password must be at least 6 characters.";
      } else {
        passwordError.textContent = "";
      }
    });
  
    // Prevent form submit if errors exist
    form.addEventListener("submit", function (e) {
      if (emailError.textContent !== "" || passwordError.textContent !== "") {
        e.preventDefault();
        alert("Please fix the errors before submitting.");
      }
    });
  });
  