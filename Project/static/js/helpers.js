// --- for closeMessage ---
const closeMessage = (uniqueId) => {
  const message = document.getElementById(uniqueId);

  const cls1 = "opacity-0"
  console.log("closeMessage............................................");
  if (message) {
    message.classList.add(cls1);
    message.style.transform = 'scale(0.95mc)'

    setTimeout(() => {
      message.parentNode.removeChild(message);
    }, 500);
  }
}

// --- for UserInfoPopup ---
const toggleUserInfoPopup = () => {
  const userInfoPopup = document.getElementById("userInfoPopupDivInHeader");
  userInfoPopup.classList.toggle("popup_active")
}

document.addEventListener("click", (e) => {
  const userInfoPopup = document.getElementById("userInfoPopupDivInHeader");
  const userInfoPopupButton = document.getElementById("userInfoPopupButtonInHeader");

  if (!userInfoPopup?.contains(e.target) && !userInfoPopupButton?.contains(e.target)) {
    userInfoPopup?.classList?.remove("popup_active");
    return
  }
});
// --- for UserInfoPopup ---


// --- copyToClipboard and make the innerHtml to copied ---
const copyToClipboard = (event, text) => {
  console.log(event.target.innerHTML);
  navigator.clipboard.writeText(text);
  event.target.innerHTML = "Copied"
  setTimeout(() => {
    event.target.innerHTML = "Copy"
  }, 1000);

}

// --- openDeleteAccountModel ---
const openDeleteAccountModel = () => {
  const deleteAccountModel = document.getElementById("deleteAccountModel");
  deleteAccountModel.classList.remove("scale-95", "opacity-0", "pointer-events-none")
  deleteAccountModel.classList.add("!scale-100", "!opacity-100", "!pointer-events-auto")
}
// --- closeDeleteAccountModel ---
const closeDeleteAccountModel = () => {
  const deleteAccountModel = document.getElementById("deleteAccountModel");
  deleteAccountModel.classList.remove("!scale-100", "!opacity-100", "!pointer-events-auto")
  deleteAccountModel.classList.add("scale-95", "opacity-0", "pointer-events-none")
}

// --- for inputChange ---
const onInputChange = (e, buttonId, prevValue) => {
  // remove the attribute disabled from inputName when prevValue !== event.target.value
  const button = document.getElementById(buttonId)
  console.log("Button :: ", button);

  if (prevValue !== e.target.value) {
    button.removeAttribute("disabled");
  } else {
    button.setAttribute("disabled", "disabled");
  }
}

// --- for avatarInputChange ---
const onAvatarInputChange = (event, currentAvatarUrl) => {
  console.log("currentAvatarUrl : ", currentAvatarUrl);
  const file = event.target.files[0];
  const userAvatarPreview = document.getElementById("userAvatarPreview");

  if (userAvatarPreview) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = () => {
      userAvatarPreview.src = reader.result;
    };
    reader.readAsDataURL(file);

    document.getElementById("buttonForUserAvatar").removeAttribute("disabled");
  }
}

// --- for themeIconLoad ---
window.addEventListener("load", () => {
  const theme = sessionStorage.getItem("theme");
  const userPreferTheme = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";

  if ((theme && theme === "dark") && userPreferTheme === "dark") {
    // sun
    // document.documentElement.classList.add(userPreferTheme);
    document.getElementById("themeIconDiv").innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-sun" viewBox="0 0 16 16"><path d="M8 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6m0 1a4 4 0 1 0 0-8 4 4 0 0 0 0 8M8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0m0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13m8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5M3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8m10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0m-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0m9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707M4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708"/></svg>`
  }
  else {
    // moon
    document.getElementById("themeIconDiv").innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-moon-stars" viewBox="0 0 16 16"><path d="M6 .278a.77.77 0 0 1 .08.858 7.2 7.2 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277q.792-.001 1.533-.16a.79.79 0 0 1 .81.316.73.73 0 0 1-.031.893A8.35 8.35 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.75.75 0 0 1 6 .278M4.858 1.311A7.27 7.27 0 0 0 1.025 7.71c0 4.02 3.279 7.276 7.319 7.276a7.32 7.32 0 0 0 5.205-2.162q-.506.063-1.029.063c-4.61 0-8.343-3.714-8.343-8.29 0-1.167.242-2.278.681-3.286"/><path d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.73 1.73 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.73 1.73 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.73 1.73 0 0 0 1.097-1.097zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.16 1.16 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.16 1.16 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732z"/></svg>`
  }

})

// --- for toggleTheme ---
const toggleTheme = () => {
  const theme = sessionStorage.getItem("theme");
  console.log()

  if (theme === "dark") {
    sessionStorage.setItem("theme", "light");
    // moon
    document.getElementById("themeIconDiv").innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" fill="currentColor" class="bi bi-moon-stars" viewBox="0 0 16 16"><path d="M6 .278a.77.77 0 0 1 .08.858 7.2 7.2 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277q.792-.001 1.533-.16a.79.79 0 0 1 .81.316.73.73 0 0 1-.031.893A8.35 8.35 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.75.75 0 0 1 6 .278M4.858 1.311A7.27 7.27 0 0 0 1.025 7.71c0 4.02 3.279 7.276 7.319 7.276a7.32 7.32 0 0 0 5.205-2.162q-.506.063-1.029.063c-4.61 0-8.343-3.714-8.343-8.29 0-1.167.242-2.278.681-3.286"/><path d="M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.73 1.73 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.73 1.73 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.73 1.73 0 0 0 1.097-1.097zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.16 1.16 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.16 1.16 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732z"/></svg>`
    document.documentElement.classList.remove("dark");
  }
  else {
    sessionStorage.setItem("theme", "dark");
    // sun
    document.getElementById("themeIconDiv").innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-sun" viewBox="0 0 16 16"><path d="M8 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6m0 1a4 4 0 1 0 0-8 4 4 0 0 0 0 8M8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0m0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13m8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5M3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8m10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0m-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0m9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707M4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708"/></svg>`
    document.documentElement.classList.add("dark");
  }
}

// --- for toggleNavigationMenu ---
const toggleNavigationMenu = (event) => {
  const navigationMenu = document.getElementById("navigationMenu")

  if (navigationMenu.classList.contains("max-lg:opacity-0", "max-lg:-translate-y-[0.125rem]", "max-lg:pointer-events-none")) {
    event.target.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1" stroke="currentColor" class="size-3 pointer-events-none"><path stroke-linecap="round" stroke-linejoin="round" d="m4.5 18.75 7.5-7.5 7.5 7.5" /><path stroke-linecap="round" stroke-linejoin="round" d="m4.5 12.75 7.5-7.5 7.5 7.5" /></svg>`
    navigationMenu.classList.remove("max-lg:opacity-0", "max-lg:-translate-y-[0.125rem]", "max-lg:pointer-events-none");
  } else {
    event.target.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1" stroke="currentColor" class="size-3 mt-[2px] pointer-events-none"><path stroke-linecap="round" stroke-linejoin="round" d="m4.5 5.25 7.5 7.5 7.5-7.5m-15 6 7.5 7.5 7.5-7.5" /></svg>`
    navigationMenu.classList.add("max-lg:opacity-0", "max-lg:-translate-y-[0.125rem]", "max-lg:pointer-events-none");
  }

}
document.addEventListener("click", (e) => {
  const navigationMenu = document.getElementById("navigationMenu");
  const navigationMenuButton = document.getElementById("navigationMenuButton");

  if (!navigationMenu?.contains(e.target) && !navigationMenuButton?.contains(e.target)) {
    navigationMenuButton.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1" stroke="currentColor" class="size-3 mt-[2px] pointer-events-none"><path stroke-linecap="round" stroke-linejoin="round" d="m4.5 5.25 7.5 7.5 7.5-7.5m-15 6 7.5 7.5 7.5-7.5" /></svg>`
    navigationMenu.classList.add("max-lg:opacity-0", "max-lg:-translate-y-[0.125rem]", "max-lg:pointer-events-none");
  }
});
// --- for toggleNavigationMenu ---
