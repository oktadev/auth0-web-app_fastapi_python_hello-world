const submitToBadger = async (button) => {
  const buttonText = button.innerText;
  button.innerText = "Loading...";
  button.disabled = true;

  await fetch('/badger', {
    method: 'POST',
    cache: 'no-cache',
  });

  window.setTimeout(() => {
    button.innerText = buttonText;
    button.disabled = false;
  }, 1000);
}

document.addEventListener("DOMContentLoaded", () => {
  const ClassName = Object.freeze({
    MOBILE_MENU_CLOSED: "mobile-nav-bar__menu--closed",
    MOBILE_NAV_BAR_TAB: "mobile-nav-bar__tab",
    MOBILE_SCROLL_LOCK: "mobile-scroll-lock",
    NAV_BAR_TAB: "nav-bar__tab"
  });

  const Icon = Object.freeze({
    CLOSE: "close",
    MENU: "menu"
  });

  const navBarButton = document.getElementById("mobile-menu-toggle-button");

  const toggleMobileMenu = () => {
    const navBarMenu = document.getElementById("mobile-menu");
    const isOpened = navBarMenu.classList.contains(ClassName.MOBILE_MENU_CLOSED);

    document.body.classList.toggle(ClassName.MOBILE_SCROLL_LOCK);
    navBarMenu?.classList.toggle(ClassName.MOBILE_MENU_CLOSED);
    navBarButton.textContent = isOpened ? Icon.CLOSE : Icon.MENU;
  };

  [ClassName.NAV_BAR_TAB, ClassName.MOBILE_NAV_BAR_TAB].forEach(navBarClass => {
    const tabs = document.getElementsByClassName(navBarClass);
    const currentTab = Array.from(tabs)
      .find(tab => {
        const href = tab.getAttribute("href");

        return window.location.pathname.startsWith(href);
      });

    currentTab?.classList.add(`${navBarClass}--active`);
  });

  navBarButton.addEventListener("click", toggleMobileMenu, false);
});