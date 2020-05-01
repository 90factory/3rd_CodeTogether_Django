
import Ajax from './ajax.js'


const signUpForm_Ajax = new Ajax();


document.getElementById('signUpForm-notice').style.display = 'none';

const validationthings = {
    name: false,
    email: false,
    phone: false,
    pw: false,
}


const signUpData = {
    name: '',
    phone: '',
    email: '',
    pw: '',
    pwCheck: '',
}
// 가입폼 검증


document.querySelector('#name').addEventListener('change', function () {
    const inName = document.querySelector('#name').value;
    console.log(inName.length);
    const el = document.querySelector('#notice-name')
    if(inName.length<2) {
        validationthings.name = false
        el.style.color = 'red'
        el.innerText=`두 글자 이상 입력하세요`;
    } else {
        validationthings.name = true
        signUpData.name=inName;
        console.log(signUpData.name)
        console.log(validationthings.name)
        el.innerText='';
    }
})

document.querySelector('#phone').addEventListener('change', function () {
    const inPhone = document.querySelector('#phone').value;
    const el = document.querySelector('#notice-phone')
    const pattern = /^01(0|1|[6-9]?)-?([0-9]{3,4})-?([0-9]{4})$/;

    if(inPhone.match(pattern)) {
        validationthings.phone = true
        signUpData.phone=inPhone;
        el.innerHTML = '';
    } else if (!inPhone.match(pattern)) {
        el.innerText=`핸드폰 번호를 확인하세요`;
        el.style.color = 'red'
        validationthings.phone = false
    }
})

document.querySelector('#email').addEventListener('change', function () {
    const inEmail = document.querySelector('#email').value;
    const el = document.querySelector('#notice-email')
    const authEmail = document.querySelector('#email-check-result')
    const pattern = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/;
    if (inEmail.match(pattern)) {
        el.innerText=`중복 확인하세요`;
        el.style.color = 'red'
        $('#emailcheck').click((e) => {
            el.innerText=``;
            event.preventDefault()
            signUpForm_Ajax.send('post', {'email':`${inEmail}`}, '/accounts/email_check/')
            .then(function(result, status, response) {
                for (const target in result) {
                    if(result[target] === 1) {
                        validationthings.email = true
                        signUpData.email=inEmail;
                        el.innerText='';
                        authEmail.innerText='가입 가능한 이메일입니다';
                    }
                    else {
                        authEmail.innerText=`이미 가입 된 이메일입니다`
                        authEmail.style.color='red'
                        validationthings.email = false
                    }
                }
            })
        })
    }   else if (!inEmail.match(pattern)) {
        el.innerText=`이메일 주소를 확인하세요`;
        el.style.color = 'red'
        validationthings.email = false
    }
})


document.querySelector('#pwcheck').addEventListener('change', function () {
    const inPw = document.querySelector('#pw').value;
    const inPwcheck = document.querySelector('#pwcheck').value;
    const el = document.querySelector('#notice-pw')
    if (inPw === inPwcheck) {
        el.innerText = '비밀번호가 일치합니다';
        validationthings.pw = true
        signUpData.pwCheck=inPwcheck;
        signUpData.pw=inPw;
    } else {
        el.innerText=`비밀번호가 일치하지 않습니다`;
        el.style.color = 'red'
        validationthings.pw = false
    }
})

// 폼 제출
$('#signup-form-submit').click((e)=> {
    console.log(signUpData)
    event.preventDefault()
    console.log('submit-btn')
    if (validationthings.name && validationthings.phone && validationthings.email && validationthings.pw === true) {
        signUpForm_Ajax.send('post', signUpData, '/accounts/signup/')
        .then(function (result, status, response) {
            for (const target in result) {
                if(result[target]===1) {
                    if(result[target]===1) {
                    document.getElementById('signUpForm-notice').style.display = '';
                    document.getElementById('signUp-form-notice').innerText = '회원가입이 완료되었습니다.'
                    document.getElementById('signUp-form-ok').addEventListener('click', function () {
                    window.location.href='/'
                    })
                }
                }
                else {
                    alert('가입이 불가합니다')
                }
            }
        })
    } else {
        alert('입력란을 확인하세요')
    }
})