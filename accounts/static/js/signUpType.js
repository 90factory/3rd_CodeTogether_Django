
const toSignUp = () => {
    const cBtn = document.querySelector('#singup-normal-btn')
    cBtn.addEventListener('click', () => {
        location.href = '/' //회원가입 폼
    })
    const nBtn = document.querySelector('#singup_naver') 
    nBtn.addEventListener('click', ()=> {
        location.href = '/' //네이버 계정으로
    })
}