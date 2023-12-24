const content_section = document.querySelector('.content-section');
const loginPopUp = document.querySelector('.popup-login-btn');

loginPopUp.addEventListener('click', ()=> {
    content_section.classList.add('active-popup');
});