import Ajax from './ajax.js'
import DefaultHandler from './default.js'
import CookieHandler from './cookieHandler.js'

const deleteMember_Ajax = new Ajax();
const deleteView = new DefaultHandler();
const deleteCookie = new CookieHandler();

const log = console.log;
log('회원탈퇴')

const el = (e) => document.querySelector(e);
const infoSubmitBtn = el('#authPersonInfoBtn');

deleteView.hide('#deleteMember-complete');


const toMoveHandler = () => {
    const toMoveBtn = document.querySelector('#delete-member-ok')
    toMoveBtn.addEventListener('click', () => location.href = '/' )
}

const resultMsgHandler = () => {
    const result_msg = '탈퇴가 완료되었습니다.';
    const goobye_msg = '그동안 이용해 주셔서 감사합니다.';

    deleteView.writeText('#delete-member-notice', result_msg);
    deleteView.writeText('#sayGoobye', goobye_msg);

    toMoveHandler()
}

const resultHandler = (result) => {

    deleteView.hide('#deleteMember-toCheck');
    deleteView.show('#deleteMember-complete');
    deleteCookie.cookieDelete(deleteCookie.cookieGet(), deleteCookie.expireDate(-1));

    for (const target in result) {
        const _result = result[target];
        if(_result===1) { resultMsgHandler() } 
        else if(_result===0) { alert('회원정보가 존재 하지 않습니다.') }
        else if(_result===-1) { alert('비밀번호가 일치 하지 않습니다.') }
        else if(_result===-2) { alert('유효하지 않은 정보입니다.') }
        else if(_result===-3) { alert('회원정보가 중복됩니다.') }
        else if(_result===-4) { alert('회원정보가 존재 하지 않습니다.') }
        else if(_result===-5) { alert('본인 인증에 실패했습니다.') }
        else if(_result===-6) { alert('정보를 다시 입력하세요.') }
        else { alert('정보를 확인 후 다시 입력하세요.') }
    }

}


const ajaxHandler = (authUserInfo) => {
    const url = '/accounts/delete/'
    const post = 'post'

    console.log(authUserInfo,'보낼 데이터')
    deleteMember_Ajax.send(post, authUserInfo, url)
    .then( (result, status, response) => {
        resultHandler(result);        
    } )
}

const toVerify = (target, pattern) => {
    if(target.match(pattern)) { return true }
    else {return false}
 
}

const getUserInfo = () => {

    const authUserInfo = {
        email: '',
        pw: '',
    }

    infoSubmitBtn.addEventListener('click', (e) => {
        event.preventDefault();
    
        const Inemail = document.getElementById('email').value;
        const Inpw = document.getElementById('pw').value;
        const emailPattern = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/
        if (toVerify(Inemail, emailPattern)) {
            authUserInfo.email = Inemail;
            authUserInfo.pw = Inpw;
        
            ajaxHandler(authUserInfo);
        } else {
            alert('이메일 확인 후 다시 입력하세요')
        }
        
    
    })

}

getUserInfo();