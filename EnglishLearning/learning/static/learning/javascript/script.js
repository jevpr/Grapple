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

//This is the script for the sign up pop up
document.addEventListener("DOMContentLoaded", function () {
  let timeLeft = 5;
  let signupBanner = document.getElementById("signup-banner");

  setTimeout(function () {
    signupBanner.style.bottom = "0";
  }, timeLeft * 1000);
});

document.addEventListener("DOMContentLoaded", function () {
  // ✅ Function to Submit the Form
  function submitSearchForm() {
    const form = document.querySelector(".search-lessons");
    if (form) {
      form.submit();
    }
  }

  // ✅ Handle Search Input "Enter" Key Event
  const searchInput = document.getElementById("search-input");
  if (searchInput) {
    searchInput.addEventListener("keypress", function (event) {
      if (event.key === "Enter") {
        event.preventDefault(); // ✅ Prevent default page reload
        submitSearchForm(); // ✅ Submit form
      }
    });
  }

  // ✅ Handle Tag Selection Click Event
  const tagLabels = document.querySelectorAll(".tag-label");
  if (tagLabels.length > 0) {
    tagLabels.forEach((label) => {
      label.addEventListener("click", function () {
        const checkbox = document.getElementById(this.getAttribute("for"));
        if (checkbox) {
          checkbox.checked = !checkbox.checked; // ✅ Toggle checkbox
          this.classList.toggle("selected", checkbox.checked); // ✅ Toggle selected class
          submitSearchForm(); // ✅ Automatically submit form
        }
      });
    });
  }
});

// This is the code for the bookmark toggle
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
