
import DefaultHandler from '../js/default.js'
const initHandlers = new DefaultHandler();

//초기화면 - 모달 숨김
initHandlers.hide('.modal-container');
initHandlers.show('.teacher-form-entire');

const submitBtn = document.querySelector('#teacher-form-submit');

// 강사 사진 미리보기
const upload = document.querySelector('#teacher-photo');
const preview0 = document.querySelector('#result');
const preview = document.querySelector('#result2')

initHandlers.hide('#result2');

upload.addEventListener('change', function (e) {

    const get_file = e.target.files;
    console.log('파일 잘 담겼나 확인', get_file)
    
    const image = document.createElement('img');

    const reader = new FileReader();

    reader.onload = ( (aImg) => {
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
    initHandlers.hide('#result')
    initHandlers.show('#result2')

    preview.appendChild(image);
   
})

//정보 보내기
submitBtn.addEventListener('click', (e) => {
    event.preventDefault();

    const formData = new FormData();

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
                if(_result===1) { 
                    initHandlers.show('.modal-container');
                    initHandlers.hide('.teacher-form-entire');
                    toGetPhoto(_result)
                    toMove();
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
        },
        error: (err) => {
            console.log(err)
        }
    })
})

const toGetPhoto = (_result) => {
    for(const _target in _result) {
        thumbnail(_result[_target].sub_image)
    }
} 

const thumbnail = (image) => {
    const figure = document.querySelector('.teacher-background-photo');
    const img = document.querySelector('.teacher-img');
   
    figure.style = `background-image: url(${image})`
    img.src=`${image}`

    console.log(img);
    console.log(figure)
}

const toMove = () => {
    console.log(document.querySelector('.modal-btn-yes'))
    document.querySelector('.modal-btn-yes').addEventListener('click', () => {
        location.href = '/subjects/add/'
    })
    document.querySelector('.modal-btn-no').addEventListener('click', () => {
        location.href = '/' //홈으로 주의: 로그인 된 상태여야 함
    })
}

