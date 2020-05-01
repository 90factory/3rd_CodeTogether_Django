
import Ajax from './ajax.js'
const teacherForm_Ajax = new Ajax();

$(document).ready(()=> {
    $('#teacher-form-submit').click((e) => {
        event.preventDefault()

        const formData = new FormData();

        formData.append('uploadPhoto', $('#teacher-photo')[0].files[0]);
        formData.append('teacherDesc', $('#teacher-desc').val());
        console.log(formData)

        $.ajax({
            type:'post',
            url:'/',
            data: formData,
            processData: false,
            contentType: false,
            success: (res) => {
                for(const target in result) {
                    const _result = result[target];
                    if(_result===1) { alert('등록이 완료되었습니다.') } 
                    else if(_result===0) { alert('회원정보가 존재 하지 않습니다.') }
                    else if(_result===-1) { alert('비밀번호가 일치 하지 않습니다.') }
                    else if(_result===-2) { alert('유효하지 않은 정보입니다.') }
                    else if(_result===-3) { alert('회원정보가 중복됩니다.') }
                    else if(_result===-4) { alert('회원정보가 존재 하지 않습니다.') }
                    else if(_result===-5) { alert('본인 인증에 실패했습니다.') }
                    else if(_result===-6) { alert('정보를 다시 입력하세요.') }
                    else { alert('정보를 확인 후 다시 입력하세요.') }
                }
            },
            error: (err) => {
                console.log(err)
            }
        })
    })
})
