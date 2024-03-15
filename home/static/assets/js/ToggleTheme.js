localStorage.setItem("theme" , "light");
const toggleThemeBtn = document.querySelectorAll("#toggle-theme");
toggleThemeBtn.forEach(btn =>{
    btn.addEventListener("click",function(){
        const localTheme = localStorage.theme;
        if (localTheme === "dark"){
            // document.documentElement.classList.remove("dark");
            document.querySelector("body").setAttribute("data-bs-theme", "light");
            document.querySelector("#icon-theme").setAttribute("class", "icono-moon");
            localStorage.theme = "light";
        } else {
            // document.documentElement.classList.add("dark");
            document.querySelector("body").setAttribute("data-bs-theme", "dark");
            document.querySelector("#icon-theme").setAttribute("class", "icono-sun");
            localStorage.setItem("theme" , "dark");
        }
    })
})
