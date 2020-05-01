const log = console.log;

//마치기 버튼 클릭시 어디로...? 마이페이지가 좋을 듯!
const exitPage = () => {
    const exit = document.querySelector('.exitPage');
    exit.addEventListener('click', () => {
        location.href = '/';
    }) 
}

const changeVideo = (link) => {
    const object = document.querySelector('object');
    object.data = link;
}


const getVideoLink = () => {
    const subjectlists = document.querySelectorAll('li');
    subjectlists.forEach( (subject) => {
        subject.addEventListener('click', (e)=> {
            const link = `${e.target.id}`;
            changeVideo(link);
        })
    } )
}

const subjectLearningInit = () => {
    getVideoLink()
}

subjectLearningInit();