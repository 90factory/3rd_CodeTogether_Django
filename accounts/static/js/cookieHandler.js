class CookieHandler {

    expireDate (days) {
        const expireDate = new Date();
        expireDate.setDate(expireDate.getDate()+days);
        return expireDate.toGMTString();

    };

    cookieCreate (name, value, path, expiredays) {
        const cookie = document.cookie = `${name}=${value}; expires=${expiredays}; path=${path};`
        return cookie;
    };
    
    cookieGet () {
        const cookies = document.cookie.split(';');
        const new_cookie = cookies.map( (cookie) => cookie.split("=")[0] )
        return new_cookie;
    };
    cookieDelete (names, expiredays) {

        return names.forEach( (name) => document.cookie = `${name}=""; expires=${expiredays}; path=/;` )

    };
}

export default CookieHandler
