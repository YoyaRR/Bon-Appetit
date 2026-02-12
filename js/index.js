(function () {
  const menuToggle = document.getElementById("mobile-menu");
  const mainNav = document.getElementById("main-nav");

  if (!menuToggle || !mainNav) return;

  menuToggle.addEventListener("click", function (e) {
    e.preventDefault();
    e.stopPropagation();
    if (window.innerWidth <= 768) {
      mainNav.classList.toggle("show");
      menuToggle.setAttribute(
        "aria-expanded",
        mainNav.classList.contains("show"),
      );
    }
  });

  // Cerrar el menú cuando se hace clic en un enlace
  mainNav.addEventListener("click", function (e) {
    if (e.target.closest("a")) {
      mainNav.classList.remove("show");
      menuToggle.setAttribute("aria-expanded", false);
    }
  });

  // Cerrar el menú si se hace clic fuera
  document.addEventListener("click", function (e) {
    if (
      window.innerWidth <= 768 &&
      !mainNav.contains(e.target) &&
      !menuToggle.contains(e.target)
    ) {
      mainNav.classList.remove("show");
      menuToggle.setAttribute("aria-expanded", false);
    }
  });

  // Manejar el scroll
  let lastScrollTop = 0;
  window.addEventListener("scroll", function () {
    if (window.innerWidth <= 768) {
      const st = window.pageYOffset || document.documentElement.scrollTop;
      if (st > lastScrollTop && mainNav.classList.contains("show")) {
        // Scrolling DOWN y el menú está abierto
        mainNav.classList.remove("show");
        menuToggle.setAttribute("aria-expanded", false);
      }
      lastScrollTop = st <= 0 ? 0 : st;
    }
  });

  // Manejar cambios de tamaño de ventana
  window.addEventListener("resize", function () {
    if (window.innerWidth > 768) {
      mainNav.classList.remove("show");
      menuToggle.setAttribute("aria-expanded", false);
    }
  });
})();
