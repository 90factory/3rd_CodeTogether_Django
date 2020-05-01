import Ajax from './ajax.js'

// const _View = new View();
const _Ajax = new Ajax();

const swiper = new Swiper('.swiper-container', {
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
});

document.getElementById('main-login-naver').addEventListener('click', function () {
    window.location.href='/accounts/repw/'
});

const toHome = () => {
    const logos = document.querySelectorAll('.toHome');
    logos.forEach( (logo) => {
        logo.addEventListener('click', ()=> {
            location.href='/'
        })
    })
}

// 로그아웃 요청
$(document).ready(()=> {
    $('#logOut').click((e)=> {
        event.preventDefault()
        const data = {
            q : 'logOut'
        }
        console.log(data)
        _Ajax.send('get', data, '/')
    })
})

toHome();
