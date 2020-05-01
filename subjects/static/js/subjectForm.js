

const log = console.log;

const modalmsg = document.querySelector('.modal-container');
const modalbtn = document.querySelector('#msg-ok');

modalmsg.style.display = 'none';

//모달창 확인 누를 시
const movePage = () => {
    modalbtn.addEventListener('click', ()=> {
        //강의 목록 확인할 수 있는 곳으로 
        location.href = '/'
    })
}


//강의 사진 미리 보기
const upload = document.querySelector('#lecture-photo');
const preview = document.querySelector('#result');
const preview2 = document.querySelector('#result2');

preview2.style.display = 'none';

upload.addEventListener('change',(e) => {
    const get_file = e.target.files;
    // console.log(get_file);
    const image = document.createElement('img');
    
    const reader = new FileReader();

    reader.onload = ( (aImg) => {
        // console.log(1);

        return function (e) {
            // console.log(3);
            aImg.src=e.target.result
        }
    })(image)
    
    if(get_file) {
        reader.readAsDataURL(get_file[0]);
        // console.log(2);
    }
    preview.style.display = 'none';
    preview2.style.display = '';
    preview2.appendChild(image);
})


//강의 등록 및 수정 관련 

const ul = document.querySelector('.subjectForm-lists');


const curriculumLists = {
    subjects : {},
    html : [],
    i : 0,
}

const setSendDataForm = () => {
    log(curriculumLists.subjects,'여기에 목록이 담기나 확인 필요함')
    
    const formData = new FormData();
    formData.append('lecture-title', $('#lecture-title').val());
    formData.append('lecture-photo', $('#lecture-photo')[0].files[0]);
    formData.append('lecture-price', $('#lecture-price').val());
    formData.append('lecture-lang', $("input[name='lecture-lang']:checked").val());
    formData.append('lecture-level', $("input[name='lecture-level']:checked").val());
    formData.append('lecture-desc', $('#lecture-desc').val());
    formData.append('curriculumLists', JSON.stringify(curriculumLists.subjects))
    log(formData.values(), '이러면..?')
    return formData;
}

const setSendDataCurr = () => {
    
    const subjectTitleLists = document.querySelectorAll('.subjectTitle')
    const subjectVideoLists = document.querySelectorAll('.subjectVideoLink');
    curriculumLists.subjects = {};

    log('subjectTitleLists',subjectTitleLists);

    let title = [];
    let video = [];

    subjectTitleLists.forEach( (subjectTitleList)=> {
        log(subjectTitleList.id, '제목')
        title.push(subjectTitleList.id)
    })
    subjectVideoLists.forEach( (subjectVideoList) => {
        log(subjectVideoList.innerText, '링크')
        video.push(subjectVideoList.innerText)
    })

    for ( let i = 0; i<title.length; i ++) {

        curriculumLists.subjects[title[i]]=video[i];

    }
    log(curriculumLists.subjects,'데이터세팅')
    setSendDataForm(curriculumLists.subjects);
}

const sendAjax = () => {
    const submitBtn = document.querySelector('#subjectForm-submitbtn'); 
    submitBtn.addEventListener('click', (e) => {
        e.preventDefault();

        $('#msg1').text("")
        $('#msg2').text("")
        $('#msg3').text("")
        $('#msg4').text("")
        $('#msg5').text("")
        $('#msg6').text("")
        $('#msg7').text("")

        setSendDataCurr();
        const sendData = setSendDataForm();
        log(sendData,'지금 여기에 강의목록이 안 담긴다')
        // resetData()

        $.ajax({
            type:'post',
            url:'/subjects/add/',
            data: sendData,
            processData: false,
            contentType: false,
            success: (res) => {
                    
                curriculumLists.subjects = {}
                curriculumLists.html=[]
                curriculumLists.i=0;

                // 성공 메세지 받으면

                movePage();
                    if (res['msg0']) { alert('입력폼을 작성해주세요') }
                    else if (res['msg1']) { $('#msg1').text(res['msg1'])} 
                    else if (res['msg2']){$('#msg2').text(res['msg2'])} 
                    else if (res['msg3']) {$('#msg3').text(res['msg3'])} 
                    else if (res['msg4']) {$('#msg4').text(res['msg4'])} 
                    else if (res['msg5']) {$('#msg5').text(res['msg5'])} 
                    else if (res['msg6']) {$('#msg6').text(res['msg6'])} 
                    else if (res['msg7']) {$('#msg7').text(res['msg7'])}
                    else if (res['name']) {
                        modalmsg.style.display = '';
                        $('#teacher-name').text(res['name']+'강사님!')
                        $('#modal-msg').text('📚'+res['subject_name']+'💻 강의')}
                    else{modalmsg.style.display = 'none';}
                },
                error: (err) => {
                    console.log(err)
                }
        })
        
    })
}

const removeEventHandler = (indexNum) => {
    const removeTarget = document.querySelector(`#${indexNum}`)
    log('이거는 어떻게 되어있나', removeTarget, indexNum)
    const target = curriculumLists.html.indexOf(removeTarget.outerHTML);
    curriculumLists.html.splice(target, 1);
    log(ul,'또 못찾아?')
    ul.removeChild(removeTarget);

}


const deleteEventHandler = (btns) => {
    btns.forEach( (btn) => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const indexNum = btn.value;
            removeEventHandler(indexNum)
        })
    } )
}

const printEventHandler = (subjectTitle, subjectVideo) => {
    log(subjectTitle,'렌더할 제목')
    curriculumLists.i++;
    log('새로 추가 된 i =', curriculumLists.i )
    curriculumLists.html.push(`<div class="subjectForm-container curr" id="parents${curriculumLists.i}"><li class="subjectTitle" id="${subjectTitle}"><span>제목: ❝ </span>${subjectTitle}<span> ❞</span></li><li class="subjectVideo">영상: <a class="subjectVideoLink" href="${subjectVideo}">${subjectVideo}</a></li><div><button class="deleteBtn-small" id="deleteBtn-js" value="parents${curriculumLists.i}">삭제</button></div></div>`);

    log(curriculumLists.html,('렌더시 html배열 확인'))
    log(ul,'ul 잡히나?')
    ul.innerHTML = curriculumLists.html.sort().join("");

    const btns = document.querySelectorAll('.deleteBtn-small')
    deleteEventHandler(btns)
}

const getInputDatas = () => {
    const subjectTitle = document.querySelector('#subjectTitle');
    const subjectVideo = document.querySelector('#subjectVideo');

    // log(subjectTitle.value,'추가된 강의 제목')

    printEventHandler(subjectTitle.value, subjectVideo.value);
    

    subjectVideo.value = '';
    subjectTitle.value = '';
}

const addBtnEventHandler = () => {
    // log('강의 추가 버튼')
    const addBtn = document.querySelector('#subject-btn')
    addBtn.addEventListener('click', (e) => {
        e.preventDefault();

        getInputDatas();    
    })
}

//등록이면 패스 수정이면 목록 가져오기
const getSubjectLists = () => {
    const conditionTarget = document.querySelector('.subjectTitle');
    log(conditionTarget)
    if(!conditionTarget) { log('notThing') }
    else {
        // log('강의 수정화면')
        const subjectTitleLists = document.querySelectorAll('.curr');
        const btns = document.querySelectorAll('.deleteBtn-small')
        subjectTitleLists.forEach( (subjectTitleList) => {
            log(subjectTitleList)
            const deleteBtn = subjectTitleList.lastElementChild.firstElementChild;
            

            curriculumLists.i++
            log('처음 세팅 i =', curriculumLists.i )
            subjectTitleList.id= 'parents'+curriculumLists.i;
            deleteBtn.value='parents'+curriculumLists.i;

            // subjectTitleList = subjectTitleList.innerHTML
            curriculumLists.html.push(subjectTitleList.outerHTML)
               
        } )
        log(curriculumLists.html, '수정화면 강의리스트들')
        
        deleteEventHandler(btns)
    }
    addBtnEventHandler(); 
    
    sendAjax();
}


getSubjectLists();