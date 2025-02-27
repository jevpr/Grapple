

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

//This is the code for the bookmarking function on lesson_search
document.addEventListener("DOMContentLoaded", function () {
  const tagLabels = document.querySelectorAll(".tag-label");
  const form = document.querySelector(".search-lessons");
  const bookmarkIcons = document.querySelectorAll(".bookmark-icon");

  // ✅ Toggle tag selection
  tagLabels.forEach((label) => {
    label.addEventListener("click", function () {
      const checkbox = document.getElementById(this.getAttribute("for"));
      checkbox.checked = !checkbox.checked;
      this.classList.toggle("selected", checkbox.checked);
      form.submit();
    });
  });

  // ✅ Bookmark Toggle Functionality
  bookmarkIcons.forEach((icon) => {
    icon.addEventListener("click", function () {
      const lessonId = this.dataset.lesson;

      fetch(`/lesson/${lessonId}/bookmark/`, {
        method: "POST",
        headers: { "X-CSRFToken": "{{ csrf_token }}" },
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
  });
});


//This is the script for the bookmark function in lesson_view
document.addEventListener("DOMContentLoaded", function () {
  const bookmarkIcon = document.querySelector(".bookmark-icon");

  bookmarkIcon.addEventListener("click", function () {
    const lessonId = this.dataset.lesson;

    fetch(`/lesson/${lessonId}/bookmark/`, {
      method: "POST",
      headers: { "X-CSRFToken": "{{ csrf_token }}" },
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
});