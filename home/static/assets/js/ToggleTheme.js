localStorage.setItem("theme" , "light");
const toggleThemeBtn = document.querySelectorAll("#toggle-theme");

toggleThemeBtn.forEach(btn =>{
    btn.addEventListener("click",function(){
        const localTheme = localStorage.theme;
        if (localTheme === "dark"){
            document.querySelector("body").classList.remove("cs_dark")
            document.querySelector("body").setAttribute("data-bs-theme", "light");
            document.querySelector("#icon-theme").setAttribute("class", "icono-moon");
            localStorage.theme = "light";
        } else {
            document.querySelector("body").setAttribute("class", "cs_dark");
            document.querySelector("#icon-theme").setAttribute("class", "icono-sun");
            localStorage.setItem("theme" , "dark");
        }
    })
})
