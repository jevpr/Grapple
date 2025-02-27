document.addEventListener("DOMContentLoaded", function () {
  // ✅ Get CSRF Token from the hidden input field
  function getCSRFToken() {
    const csrfInput = document.querySelector(
      "input[name='csrfmiddlewaretoken']"
    );
    return csrfInput ? csrfInput.value : "";
  }

  // ✅ Dropdown Menu Logic
  const menuToggle = document.querySelector(".logo");
  const dropdownMenu = document.querySelector(".dropdown-menu");
  const mainContent = document.querySelector("main");

  let isRotated = false; // Track rotation state

  if (menuToggle && dropdownMenu && mainContent) {
    menuToggle.addEventListener("click", function (event) {
      event.stopPropagation(); // Prevents closing on immediate click

      // Toggle logo rotation
      isRotated = !isRotated;
      menuToggle.style.transform = isRotated
        ? "rotateY(180deg)"
        : "rotateY(0deg)";

      // Toggle dropdown rolling down from behind the navbar
      dropdownMenu.classList.toggle("active");
      mainContent.classList.toggle("main-shift");
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
  }

  // ✅ Tag Selection Logic
  const tagLabels = document.querySelectorAll(".tag-label");
  const form = document.querySelector(".search-lessons");

  if (tagLabels.length > 0 && form) {
    tagLabels.forEach((label) => {
      label.addEventListener("click", function () {
        const checkbox = document.getElementById(this.getAttribute("for"));
        if (checkbox) {
          checkbox.checked = !checkbox.checked;
          this.classList.toggle("selected", checkbox.checked);
          form.submit(); // ✅ Automatically submit the form
        }
      });
    });
  }

  // ✅ Bookmarking Logic for Lesson Search Page
  const bookmarkIcons = document.querySelectorAll(".bookmark-icon");

  if (bookmarkIcons.length > 0) {
    bookmarkIcons.forEach((icon) => {
      icon.addEventListener("click", function () {
        const lessonId = this.dataset.lesson;
        const csrfToken = getCSRFToken();

        fetch(`/lesson/${lessonId}/bookmark/`, {
          method: "POST",
          headers: {
            "X-CSRFToken": csrfToken,
            "Content-Type": "application/json",
          },
          credentials: "same-origin", // Ensures session cookies are sent
        })
          .then((response) => {
            if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
          })
          .then((data) => {
            if (data.bookmarked) {
              icon.classList.remove("fa-regular");
              icon.classList.add("fa-solid");
            } else {
              icon.classList.remove("fa-solid");
              icon.classList.add("fa-regular");
            }
          })
          .catch((error) => console.error("Error:", error));
      });
    });
  }

  // ✅ Bookmarking Logic for Lesson View Page
  const bookmarkIcon = document.querySelector(".bookmark-icon");

  if (bookmarkIcon) {
    bookmarkIcon.addEventListener("click", function () {
      const lessonId = this.dataset.lesson;

      fetch(`/lesson/${lessonId}/bookmark/`, {
        method: "POST",
        headers: { "X-CSRFToken": getCSRFToken() },
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
        });
    });
  }
});
