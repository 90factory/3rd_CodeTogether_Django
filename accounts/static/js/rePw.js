
$(document).ready(()=> {
    $("#submit-pw-btn").click((e)=>{
        event.preventDefault();
        const pattern = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/;
        const email = document.getElementById('email').value;
        const att = document.querySelector('#att');

        let msg = '';
        if(!email.match(pattern)) {
            msg = `이메일 주소를 확인하세요`;
            att.innerText = msg;
        } else if (email.match(pattern)) {
            const data = {
                email : document.getElementById('email').value
            };
            printWaitMsg();
            console.log(data);
            att.innerText = '';
            $.ajax({
                type:"post",
                url:"/accounts/repw/",
                data:data,
                datatype: 'json',
                success: (result => {
                    console.log('성공');
                    printWaitMsg();
                    // $("#re-password-info-2").show();
                    // $("#re-password-info-1").hide();
                }),
                error: (err => {
                    console.log(err);
                })
            })
        }

    })

    const printWaitMsg = () => {
        document.querySelector('.notice-share').style.display = 'none';
        document.querySelector('#notice-share').innerText = `비밀번호가 재설정 되었습니다. 이메일을 확인해 주세요`
        document.querySelector('#submit-pw-btn').innerText = `확인`
        document.querySelector('#submit-pw-btn').addEventListener('click', ()=> {
            location.href = '/';
        })
    }

})