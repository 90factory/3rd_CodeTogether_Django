
import Ajax from './ajax.js'

const signUpForm_Ajax = new Ajax();

const log = console.log;
document.getElementById('signUpForm-notice').style.display = 'none';


const getUserInfo = () => {

    const signUpData = {
        name: '',
        phone: '',
        currentPw:'',
        newPw: '',
        newPwCheck: '',
    }
    
    signUpData.name = document.querySelector('#name').value;
    signUpData.phone = document.querySelector('#phone').value;
    signUpData.currentPw = document.querySelector('#currentPw').value;
    signUpData.newPw = document.querySelector('#pw').value;
    signUpData.newPwCheck = document.querySelector('#pwcheck').value;

    console.log(signUpData);
    return signUpData;

}



const sendAjax = () => {
    const submitBtn = document.querySelector('#signup-form-submit');
    log(submitBtn, '버튼 잡힘?')
    submitBtn.addEventListener('click', (e) => {
        event.preventDefault()
        const signUpdateData = getUserInfo();
        log(getUserInfo(), '보낼 데이터 ajax 안입니다.')
        
        signUpForm_Ajax.send('post', signUpdateData, '/accounts/update/')
        .then(function (result, status, response) {
            for (const target in result) {
                const _result = result[target];
                if(_result === 1) {
                    document.getElementById('signUpForm-notice').style.display = '';
                    document.getElementById('signUp-form-notice').innerText = '회원가입이 완료되었습니다.'
                    document.getElementById('signUp-form-ok').addEventListener('click', function () {
                    window.location.href='/'
                    })
                }
                else if(_result===0) { alert('회원정보가 존재 하지 않습니다.') }
                else if(_result===-1) { alert('비밀번호가 일치 하지 않습니다.') }
                else if(_result===-2) { alert('유효하지 않은 정보입니다.') }
                else if(_result===-3) { alert('회원정보가 중복됩니다.') }
                else if(_result===-4) { alert('회원정보가 존재 하지 않습니다.') }
                else if(_result===-5) { alert('본인 인증에 실패했습니다.') }
                else if(_result===-6) { alert('정보를 다시 입력하세요.') }
                else { alert('정보를 확인 후 다시 입력하세요.') }

            }

        })
    })
}

sendAjax();