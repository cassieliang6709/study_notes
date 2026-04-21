document.addEventListener("DOMContentLoaded", function () {
  const html = document.documentElement;
  const body = document.body;
  const themeBtn = document.getElementById("theme-toggle");
  const sidebar = document.getElementById("sidebar");
  const sidebarBtn = document.getElementById("sidebar-toggle");
  const backdrop = document.getElementById("sidebar-backdrop");
  const pageInner = document.querySelector(".page-inner");
  const tocRail = document.getElementById("toc-rail");
  const tocNav = document.getElementById("toc-nav");

  const savedTheme = localStorage.getItem("theme") || "light";
  html.classList.remove("light", "dark");
  html.classList.add(savedTheme);

  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      const nextTheme = html.classList.contains("light") ? "dark" : "light";
      html.classList.remove("light", "dark");
      html.classList.add(nextTheme);
      localStorage.setItem("theme", nextTheme);
    });
  }

  function setBackdrop(open) {
    if (!backdrop) {
      return;
    }
    backdrop.hidden = !open;
  }

  function closeMobileSidebar() {
    if (!sidebar || window.innerWidth > 900) {
      return;
    }
    sidebar.classList.remove("open");
    setBackdrop(false);
  }

  if (sidebarBtn && sidebar) {
    sidebarBtn.addEventListener("click", function () {
      if (window.innerWidth <= 900) {
        const nextOpen = !sidebar.classList.contains("open");
        sidebar.classList.toggle("open", nextOpen);
        setBackdrop(nextOpen);
      } else {
        body.classList.toggle("sidebar-collapsed");
      }
    });
  }

  if (backdrop) {
    backdrop.addEventListener("click", closeMobileSidebar);
  }

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      closeMobileSidebar();
    }
  });

  window.addEventListener("resize", function () {
    if (window.innerWidth > 900) {
      if (sidebar) {
        sidebar.classList.remove("open");
      }
      setBackdrop(false);
    }
  });

  if (!pageInner) {
    return;
  }

  const headings = Array.from(pageInner.querySelectorAll("h2, h3")).filter(function (heading) {
    return heading.textContent.trim().length > 0;
  });

  headings.forEach(function (heading, index) {
    if (!heading.id) {
      const slug = heading.textContent
        .trim()
        .toLowerCase()
        .replace(/[^\w\u4e00-\u9fff\s-]/g, "")
        .replace(/\s+/g, "-")
        .replace(/-+/g, "-");
      heading.id = slug || "section-" + index;
    }
  });

  if (!tocRail || !tocNav || headings.length < 2) {
    return;
  }

  tocRail.hidden = false;
  const links = headings.map(function (heading) {
    const link = document.createElement("a");
    link.href = "#" + heading.id;
    link.textContent = heading.textContent.trim();
    link.className = "toc-link depth-" + heading.tagName.substring(1);
    tocNav.appendChild(link);
    return link;
  });

  const observer = new IntersectionObserver(
    function (entries) {
      const visible = entries
        .filter(function (entry) {
          return entry.isIntersecting;
        })
        .sort(function (a, b) {
          return a.boundingClientRect.top - b.boundingClientRect.top;
        });

      if (visible.length === 0) {
        return;
      }

      const activeId = visible[0].target.id;
      links.forEach(function (link) {
        link.classList.toggle("is-active", link.getAttribute("href") === "#" + activeId);
      });
    },
    {
      rootMargin: "-20% 0px -65% 0px",
      threshold: [0, 1]
    }
  );

  headings.forEach(function (heading) {
    observer.observe(heading);
  });

  pageInner.querySelectorAll("a[href^='#']").forEach(function (anchor) {
    anchor.addEventListener("click", closeMobileSidebar);
  });
});
