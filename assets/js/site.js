document.addEventListener("DOMContentLoaded", function () {

  // --- Theme toggle ---
  const html = document.documentElement;
  const themeBtn = document.getElementById("theme-toggle");
  const savedTheme = localStorage.getItem("theme") || "light";
  html.className = savedTheme;

  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      const next = html.classList.contains("light") ? "dark" : "light";
      html.className = next;
      localStorage.setItem("theme", next);
    });
  }

  // --- Sidebar toggle ---
  const sidebar = document.getElementById("sidebar");
  const sidebarBtn = document.getElementById("sidebar-toggle");

  if (sidebarBtn && sidebar) {
    sidebarBtn.addEventListener("click", function () {
      if (window.innerWidth <= 768) {
        sidebar.classList.toggle("open");
      } else {
        sidebar.classList.toggle("hidden");
        document.getElementById("page-wrapper").style.marginLeft =
          sidebar.classList.contains("hidden") ? "0" : "";
      }
    });
  }

  // --- TOC highlight (for doc pages) ---
  const pageInner = document.querySelector(".page-inner");
  if (pageInner) {
    const headings = Array.from(pageInner.querySelectorAll("h2, h3"));
    headings.forEach(function (h, i) {
      if (!h.id) {
        h.id = h.textContent.trim().toLowerCase()
          .replace(/[^\w\u4e00-\u9fa5]+/g, "-")
          .replace(/^-+|-+$/g, "") || "section-" + i;
      }
    });
  }

  // --- Back to top on scroll ---
  const pageWrapper = document.getElementById("page-wrapper");
  if (pageWrapper) {
    pageWrapper.addEventListener("scroll", function () {
      // reserved for future use
    }, { passive: true });
  }

});
