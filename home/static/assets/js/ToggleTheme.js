
let toggleThemeBtn = document.querySelector(".btn-toggle");
let LocalTheme = localStorage.getItem("theme");

// Default
if (LocalTheme==="light") {
    document.querySelector("#icon-theme").setAttribute("class", "icono-moon");
    applyTheme('light');
  } else {
    document.querySelector("#icon-theme").setAttribute("class", "icono-sun");
    applyTheme('dark');
  }

toggleThemeBtn.addEventListener("click",function(){
  console.log("df")
  if (localStorage.theme === "dark"){
     document.querySelector("#icon-theme").setAttribute("class", "icono-moon");
     applyTheme('light');
        } else {
           document.querySelector("#icon-theme").setAttribute("class", "icono-sun");
           applyTheme('dark');
        }
})

  function applyTheme(theme) {
    localStorage.setItem('theme', theme);
    if (theme === 'dark') {
      document.body.classList.add('cs_dark');
    } else {
      document.body.classList.remove('cs_dark');
    }
  }

