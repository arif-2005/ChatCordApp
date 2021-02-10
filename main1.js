var websocket = new WebSocket("ws://127.0.0.1:6789/");
const chatMessages = document.querySelector('#mainChatBody');
const body = document.querySelector('#chatcordChat');
var uname = prompt("Your name:");
var chatInputText = document.getElementById("chatInputText");
var available_user = document.getElementById("chatUserStats");

chatMessages.scrollTop = chatMessages.scrollHeight;
//send greets message to the server
websocket.onopen = function(evt) { onOpen(evt) };
function onOpen(evt)
  {
    //websocket.onmessage = function(r){web = Json.parse(e.data);webid =data.webid}
    websocket.send(JSON.stringify({username:uname,roomId:"15",message:"™™~π™™",time:"",msgType:"text"}));
}
//send message to the server
function sendData() {
  // Get text Message from dom
  let msg = document.getElementById("chatInputText").value;
  msg = msg.trim();
  document.getElementById("chatInputText").value = "";
  document.getElementById("chatInputText").focus();
  document.getElementById("chatInputText").style.height='18px';
  if (msg != ""){
    websocket.send(JSON.stringify({username:uname,roomId:"15",message:msg,time:"",msgType:"text"}));
  console.log("Message sent: " + msg)
  }
}

function InputFocus() {
    document.getElementById('footer').style.display="none";
chatMessages.scrollTop = chatMessages.scrollHeight;
}
function InputBlur() {
    console.log("InputBlur")
    document.getElementById('footer').style.display="block";
}

// receive message from the server
websocket.onmessage = function (event) {
      //data = JSON.parse(event.data);
  data = JSON.parse(event.data);
      console.log(data);
      available_user.innerText = data.available_user + " Users Online";
  addmessage();
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

  //<div class="othersChat">
	  //<h5 class="chatVictim"><b>Rohit</b></h5>
	  //<div class="chatMessage"><p>Hello Arif!!!How are you..are you doing great!</p></div>
	  //<p class="chatTime">12:31 AM</p>
  //</div>

function addmessage(){
  if (data.username == uname){
    chatclass = "myChat";
    chatuname = "You";
  } else {
    chatclass = "othersChat";
    chatuname = data.username;
  }
  if (data.username == "ChatCord"){
    chatclass = "botchat";
    chatuname = data.username;
  }
  const div = document.createElement('div');
  div.classList.add(chatclass);

  const h5 = document.createElement('h5');
  h5.classList.add('chatVictim');

  const b = document.createElement('b');
  b.innerText = chatuname;

  h5.appendChild(b);

  const messageDiv = document.createElement('div');
  messageDiv.classList.add('chatMessage');

  if (data.msgType == "text"){
  const getmessage = document.createElement('p');
  getmessage.innerText = data.message;

  messageDiv.appendChild(getmessage);
  }
  if (data.msgType == "img"){
  const getmessage = document.createElement('img');
  getmessage.setAttribute("src",data.message)

  messageDiv.appendChild(getmessage);
  }
  if (data.msgType == "video"){
  const getmessage = document.createElement('p');
  getmessage.innerText = data.message;

  messageDiv.appendChild(getmessage);
  }

  const chattime = document.createElement('p');
  chattime.classList.add('chatTime');
  chattime.innerText = data.time;

  div.appendChild(h5);
  div.appendChild(messageDiv);
  div.appendChild(chattime);
  document.querySelector('#mainChatBody').appendChild(div)


}





//Textarea resizing
function expandTextarea(id) {
    document.getElementById(id).addEventListener('keyup', function() {
        this.style.overflow = 'auto';
        this.style.height = 0;
        this.style.height = this.scrollHeight + 'px';
        $('body').scrollTop = '100px';//body.scrollHeight;
    }, false);
}
expandTextarea('chatInputText');




function getImageBtn(){
    document.getElementById("get-image").click();
}
// Get Image from the dom
var imagebase64 = "";  
function encodeImageFileAsURL(element) {  
    var file = element.files[0];  
    var reader = new FileReader();  
    reader.onloadend = function() {  
        imagebase64 = reader.result;  
        console.log(imagebase64);
        websocket.send(JSON.stringify({username:uname,roomId:"15",message:imagebase64,time:"",msgType:"img"}));

    }  
    reader.readAsDataURL(file);  
}  