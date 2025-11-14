// script.js
document.addEventListener("DOMContentLoaded", function () {
  const button = document.querySelector(".book-btn");
  if (button) {
    button.addEventListener("click", function () {
      alert("🎉 Thank you for choosing SmartWash Laundry!");
    });
  }

  // Example: auto-rotate header color
  const header = document.querySelector("header");
  const colors = ["#60a2e4ff", "#20B2AA", "#e2d06bff", "#47996cff"];
  let i = 0;
  setInterval(() => {
    header.style.backgroundColor = colors[i];
    i = (i + 1) % colors.length;
  }, 4000);
});
