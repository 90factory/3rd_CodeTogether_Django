
class DefaultHandler {
    
    el (el) {
        document.querySelector(el);
    };
    hide (el) {
        document.querySelector(el).style.display = 'none';
    };
    show (el) {
        document.querySelector(el).style.display = '';
    };
    getValue (el) {
        document.querySelector(el).value;
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