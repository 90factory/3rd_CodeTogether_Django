class Ajax {
    constructor(sendData, url) {
        this.sendData = sendData
        this.url = url
    }
    send (type, sendData, url) { return (
        $.ajax({
            type: type,
            url: url,
            data: sendData,
            dataType: 'json',
            success: (data) => {
                 new Promise (res => {
                    console.log('export 파일');
                    setTimeout(()=> {
                        res(data)}, 200
                    )
                })
            },
            error: (err) => {
                console.log(err, 'error')
            }
        }))
    }
}

export default Ajax;