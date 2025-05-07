// Wait until the DOM is loaded
document.addEventListener("DOMContentLoaded", function () {
    const textarea = document.getElementById("message");
    const charCount = document.getElementById("charCount");
    const maxLength = textarea.getAttribute("maxlength");
  
    // Event listener for real-time character count
    textarea.addEventListener("input", function () {
      const currentLength = textarea.value.length;
      charCount.textContent = `${currentLength} / ${maxLength}`;
    });
  });
  