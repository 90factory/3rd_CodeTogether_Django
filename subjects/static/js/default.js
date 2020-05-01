
class DefaultHandler {
    
    hide (el) {
        document.querySelector(el).style.display = 'none';
    };
    show (el) {
        document.querySelector(el).style.display = '';
    };
    reset (el) {
        document.querySelector(el).value = '';
    };
    writeText (el, text) {
        document.querySelector(el).innerText = text;
    };
    render (el, html) {
        document.querySelector(el).innerHTML = html.trim();
    };
}

export default DefaultHandler