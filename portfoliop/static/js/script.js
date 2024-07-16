document.addEventListener("DOMContentLoaded", function (event) {
  var elements = document.querySelectorAll(".fade-animate");
  elements.forEach(function (el) {
    el.classList.add("fadeIn");
  });
});
