

//This is the code for the menu dropdown 
document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.querySelector(".logo");
  const dropdownMenu = document.querySelector(".dropdown-menu");
  const mainContent = document.querySelector("main");

  let isRotated = false; // Track rotation state

  menuToggle.addEventListener("click", function (event) {
    event.stopPropagation(); // Prevents closing on immediate click

    // Toggle logo rotation
    isRotated = !isRotated;
    menuToggle.style.transform = isRotated
      ? "rotateY(180deg)"
      : "rotateY(0deg)";

    // Toggle dropdown rolling down from behind the navbar
    if (!dropdownMenu.classList.contains("active")) {
      dropdownMenu.classList.add("active");
      mainContent.classList.add("main-shift");
    } else {
      dropdownMenu.classList.remove("active");
      mainContent.classList.remove("main-shift");
    }
  });

  // Close dropdown when clicking outside
  document.addEventListener("click", function (event) {
    if (
      !menuToggle.contains(event.target) &&
      !dropdownMenu.contains(event.target)
    ) {
      dropdownMenu.classList.remove("active");
      mainContent.classList.remove("main-shift");
      isRotated = false; // Reset rotation state
      menuToggle.style.transform = "rotateY(0deg)";
    }
  });
});


document.addEventListener("DOMContentLoaded", function () {
  // ✅ Function to Get CSRF Token
  function getCSRFToken() {
    const csrfInput = document.querySelector(
      "input[name='csrfmiddlewaretoken']"
    );
    if (!csrfInput) {
      console.error(
        "CSRF token input not found! Make sure {% csrf_token %} is present in your HTML."
      );
    }
    return csrfInput ? csrfInput.value : "";
  }

  // ✅ Select ALL bookmark icons on the page
  function attachBookmarkListeners() {
    const bookmarkIcons = document.querySelectorAll(".bookmark-icon");

    bookmarkIcons.forEach((icon) => {
      icon.addEventListener("click", function () {
        const lessonId = this.dataset.lesson;
        const bookmarkUrl = this.dataset.url;
        const csrfToken = getCSRFToken();

        fetch(bookmarkUrl, {
          method: "POST",
          headers: {
            "X-CSRFToken": csrfToken,
            "Content-Type": "application/json",
          },
          credentials: "same-origin",
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.bookmarked) {
              this.classList.remove("fa-regular");
              this.classList.add("fa-solid");
            } else {
              this.classList.remove("fa-solid");
              this.classList.add("fa-regular");
            }
          })
          .catch((error) => console.error("Error:", error));
      });
    });
  }

  // ✅ Attach bookmark listeners when page loads
  attachBookmarkListeners();
});
