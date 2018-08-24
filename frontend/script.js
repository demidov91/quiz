function getServerUrl(){
    return document.getElementsByClassName('js-serverUrl')[0].value;
}

var query = new URLSearchParams(window.location.search);
const auth_key = query.get("auth_key");
const socket = new WebSocket("ws://" + getServerUrl() + "/player?auth_key=" + auth_key);
socket.addEventListener('message', function (event) {
    console.log('Message from server ', event.data);
});

