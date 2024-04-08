
// On page load or when changing themes, best to add inline in `head` to avoid FOUC
; (() => {
    const theme = sessionStorage.getItem("theme");
    const userPreferTheme = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";

    if (theme) {
        document.documentElement.classList.add(theme);
    }
    else {
        sessionStorage.setItem("theme", userPreferTheme);
        document.documentElement.classList.add(userPreferTheme);
    }
})()