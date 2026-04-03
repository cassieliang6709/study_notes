document.addEventListener("DOMContentLoaded", function () {
  const article = document.getElementById("article-content");
  const tocPanel = document.getElementById("toc-panel");
  const tocNav = document.getElementById("toc-nav");
  const backToTop = document.querySelector(".back-to-top");

  if (article && tocPanel && tocNav && !document.body.classList.contains("page-home")) {
    const headings = Array.from(article.querySelectorAll("h2, h3")).filter((heading) => {
      return heading.textContent && heading.textContent.trim().length > 0;
    });

    if (headings.length >= 2) {
      const list = document.createElement("ul");

      headings.forEach((heading, index) => {
        if (!heading.id) {
          const slug = heading.textContent
            .trim()
            .toLowerCase()
            .replace(/[^\w\u4e00-\u9fa5]+/g, "-")
            .replace(/^-+|-+$/g, "");
          heading.id = slug || "section-" + index;
        }

        const item = document.createElement("li");
        item.className = heading.tagName.toLowerCase() === "h3" ? "toc-subitem" : "toc-item";

        const link = document.createElement("a");
        link.href = "#" + heading.id;
        link.textContent = heading.textContent.trim();
        link.dataset.target = heading.id;

        item.appendChild(link);
        list.appendChild(item);
      });

      tocNav.appendChild(list);
      tocPanel.hidden = false;

      const links = Array.from(tocNav.querySelectorAll("a[data-target]"));
      const observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            const id = entry.target.getAttribute("id");
            const link = tocNav.querySelector('a[data-target="' + id + '"]');

            if (link && entry.isIntersecting) {
              links.forEach(function (item) {
                item.classList.remove("is-active");
              });
              link.classList.add("is-active");
            }
          });
        },
        {
          rootMargin: "-20% 0px -65% 0px",
          threshold: [0.2, 0.6]
        }
      );

      headings.forEach(function (heading) {
        observer.observe(heading);
      });
    }
  }

  if (backToTop) {
    const toggleBackToTop = function () {
      if (window.scrollY > 480) {
        backToTop.classList.add("is-visible");
      } else {
        backToTop.classList.remove("is-visible");
      }
    };

    toggleBackToTop();
    window.addEventListener("scroll", toggleBackToTop, { passive: true });
  }
});
