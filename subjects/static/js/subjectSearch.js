import Ajax from './ajax.js'
import DefaultHandler from './default.js'
const subjectSearch_Ajax = new Ajax();
const Set = new DefaultHandler();


Set.hide('.modal');
//강의 검색 시
$(document).ready(()=> {
    $('#search-submit-btn').click((e)=> {
        event.preventDefault();
        const data = {
            q: $('#search-submit-keyword').val()
        }
        // const url = `/${data}`
        console.log(data);
        $('.lecture-search-items').text('');

        // document.getElementById('pre-next-btns').style.display = 'none';
        Set.reset('#search-submit-keyword')
        Set.hide('#pre-next-btns')

        subjectSearch_Ajax.send('get', data, '/subjects/search/')
        .then(function (result, status, response) {
            $(".subject-list").hide();
            console.log(result);
            for (const target in result) {
                let _result = result[target];
                if (_result==='-1') {
                    $('.modal').show();
                    const text = `검색결과가 없습니다`;
                    Set.writeText('#search-msg', text);

                    $('#ok').click((e) => {
                        $('.modal').hide();
                        $('.lecture-search-items').text('');
                        location.href='/subjects/'
                    })
                }else {
                $(".subject-list").show();
                    console.log(_result);
                    let html = '';
                    for (const _target in _result) {

                        console.log(_result)
                        console.log(_target)
                        console.log(_result[_target])
                        console.log('요기?')
                        html += `
                            <li class="subject-item">
                                <a href="/subjects/${_result[_target].id}">
                                    <figure class="subject-background-img" style="background-image: url(${_result[_target].sub_image})">
                                    <img class="subject-img" src="${_result[_target].sub_image}" alt="${_result[_target].name}">
                                    </figure>
                                    <div class="subject-info">
                                        <div class="subject-name">${_result[_target].name}</div>
                                        <div class="subject-details">
                                            <div class="subject-teacher">${_result[_target].teacher}</div>
                                            <div class="subject-difficulty">${_result[_target].difficulty}</div>
                                            <div class="subject-price"><span class="won">￦</span>${(_result[_target].price).toLocaleString()}</div>
                                        </div>
                                    </div>
                                </a>
                            </li>`;

                        // $('.subject-list').append(repeat.trim())

                        }
                        Set.render('.subject-list', html);
                    }
                }
            })
        })
    });



//pagination

//처음/마지막 버튼 동작
const first_last_Page = () => {
    document.querySelector('.first-btn').addEventListener('click', () => {
        console.log('처음으로 버튼 동작');
        const pageNum = 1;
        // 리다이렉트시 window.location.href='/subjects/subjectSearch/?page=1'
        setAjax(pageNum);
    })
    document.querySelector('.last-btn').addEventListener('click', ()=>{
        console.log('마지막으로 버튼 동작')
        const lastPageN = document.querySelectorAll('.page-num').length;
        setAjax(lastPageN);
    })
}

//현재페이지 수 구하기
const getCurrentPage = () => {
    const current = Number(location.href.split('page=')[1]);
    console.log('현재페이지 수 구하기', current);
    return current;
}

//이전/다음 버튼 동작
const pre_next_Page = () => {
    const currentPage = getCurrentPage();

    const prePage = Number(currentPage) -1;
    const nextPage = Number(currentPage) +1;

    const prebtn = document.querySelector('.pre-btn');
    const nextbtn = document.querySelector('.next-btn');

    prebtn.addEventListener('click', (prePage) => {
        setAjax(prePage);
    })
    nextbtn.addEventListener('click', (nextPage) => {
        setAjax(nextPage);
    })
}

//전체 페이지 관리
const pageBtnEventHandler = () => {
    const pagebtns = document.querySelectorAll('.page-num');
    const total = Number(pagebtns.length);
    
    pagebtns.forEach( (pagebtn) => {
        pagebtn.addEventListener('click', (e) => {
            const reqPage = Number(e.target.value);

            if ( 1<= reqPage || reqPage < (total+1)) {
                setAjax(reqPage);
            } else {
                alert('페이지를 확인하세요.')
            }
        })
    })
}

//ajax 관리
const setAjax = (pageNum) => {
    const data = { q: pageNum }
    const url = `/subjects/search/`

    subjectSearch_Ajax.send('get', data, url)
    .then( (result, status, response) => {
        $(".subject-list").hide();
        pageView(pageNum, result);
    } )
}

//데이터 출력
const pageView = (pageNum, result) => {
    $(".subject-list").show();
    let html = '';
    for (const _target in result) {
        html += `
        <li class="subject-item">
            <a href="/subjects/${result[_target].id}">
                <figure class="subject-background-img" style="background-image: url(${result[_target].sub_image})">
                <img class="subject-img" src="${result[_target].sub_image}" alt="${result[_target].name}">
                </figure>
                <div class="subject-info">
                    <div class="subject-name">${result[_target].name}</div>
                    <div class="subject-details">
                        <div class="subject-teacher">${result[_target].teacher}</div>
                        <div class="subject-difficulty">${result[_target].difficulty}</div>
                        <div class="subject-price"><span class="won">￦</span>${(result[_target].price)}</div>
                    </div>
                </div>
            </a>
        </li>`;
        document.querySelector('.subject-list').innerHTML = html.trim()
    }
}

const init = () => {
    pre_next_Page();
    pageBtnEventHandler();
}

init();