import Ajax from '../js/ajax.js'

const updateTeacher_Ajax = new Ajax();

const submitBtn = document.querySelector('#teacher-form-submit');

// 강사 사진 미리보기
const upload = document.querySelector('#teacher-photo');
const preview0 = document.querySelector('#result');
const preview = document.querySelector('#result2')

preview.style.display = 'none';

upload.addEventListener('change', function (e) {

    const get_file = e.target.files;
    console.log('파일 잘 담겼나 확인', get_file)
    
    const image = document.createElement('img');

    const reader = new FileReader();

    reader.onload = (function (aImg) {
        console.log(1);

        return function (e) {
            console.log(3);
            aImg.src=e.target.result
        }
    })(image)
    if(get_file) {
        reader.readAsDataURL(get_file[0])
        console.log(2);
    }
    preview0.style.display = 'none';
    preview.style.display = '';
    preview.appendChild(image);
   
})



//정보 보내기
submitBtn.addEventListener('click', (e) => {
    event.preventDefault();

    const formData = new FormData();

    formData.append('teacherName', $('#name').val());
    formData.append('teacherPhone', $('#phone').val());
    formData.append('currentTeacherPw', $('#pw').val());
    formData.append('teacherPw', $('#notice-pw').val());
    formData.append('uploadPhoto', $('#teacher-photo')[0].files[0]);
    formData.append('teacherDesc', $('#teacher-desc').val());
    console.log('서버에 보낼 formdata',formData);

    $.ajax({
        type:'post',
        url:'/',
        data: formData,
        processData: false,
        contentType: false,
        success: (result) => {
            for (const target in result) {
                const _result = result[target];
                if(_result === 1) { alert('정보 수정이 완료되었습니다.'); location.href='/' }
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