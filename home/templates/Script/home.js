const navOpenBtn= document.querySelector('.nav-icon');
const menuNav =document.querySelector('.menuNav');
const overlay = document.querySelector('.overlay');
const closeNav = document.querySelector('.close-nav');


// Mobile Menu
function closeNavMenu(){
    menuNav.classList.remove('right-0');
    menuNav.classList.add('-right-64');
    overlay.classList.add('hidden');
}

navOpenBtn.addEventListener("click" ,function () { 
    menuNav.classList.add('right-0');
    menuNav.classList.remove('-right-64');
    overlay.classList.remove('hidden');
    overlay.addEventListener('click',closeNavMenu);
  
 })


closeNav.addEventListener('click',closeNavMenu);
