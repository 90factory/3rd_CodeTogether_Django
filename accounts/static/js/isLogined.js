const tag = ['isLogined']

class UserType {
    constructor(type) {
        this.type=type;
    }
    show = (el) => {
        return document.querySelector(el).style.display='';
    }
    hide = (el) => {
        return document.querySelector(el).style.display='none';
    }
    changeType = () => {       
                 this.show('#toAddSubject');
                 this.hide('#toBeTeacher');
                 return this.type='teacher';
    }
    addInfo = () => {
        return document.getElementById("teacher-form").innerHTML='<object type="text/html" data="/src/html/main/teacher-form.html"></object>';
    }
}

export default UserType