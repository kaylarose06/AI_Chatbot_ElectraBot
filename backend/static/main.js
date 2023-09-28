var msgerChat = document.querySelector(".msger-chat");
var msgerInput = document.querySelector(".msger-input");
var msgerSendBtn = document.querySelector(".msger-send-btn");
messages = [];
// Initialize a flag variable to track ongoing requests
let isRequestInProgress = false;

function submitForm(event) {
  event.preventDefault();
  // Animate scrolling
  msgerChat.scrollTop = msgerChat.scrollHeight;

  var msgText = msgerInput.value;
  if (!msgText) return;

  // Check if a request is already in progress, if yes, return immediately
  if (isRequestInProgress) {
    console.log(
      "A request is already in progress. Please wait for the response."
    );
    return;
  }

  let msg1 = { name: "User", message: msgText };
  messages.push(msg1);
  updateChat(msg1);

  // Set the flag to true, indicating a request is now in progress
  isRequestInProgress = true;

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    body: JSON.stringify({ message: msgText }),
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      let msg2 = { name: "Sam", message: data.answer };
      messages.push(msg2);
      msgerInput.value = "";
      updateChat(msg2);

      // Reset the flag to false since the request is now completed
      isRequestInProgress = false;
    })
    .catch((error) => {
      console.error("Error:", error);
      let msg2 = { name: "Sam", message: "Sorry, something went wrong." };
      messages.push(msg2);
      msgerInput.value = "";
      updateChat(msg2);

      // Reset the flag to false in case of an error as well
      isRequestInProgress = false;
    });
}

function updateChat(msgText) {
  var msgHTML = "";
  msg = msgText;
  if (msg.name === "Sam") {
    msgHTML +=
      '<div class="msg left-msg"><div class="msg-bubble"><div class="msg-info"><div class="msg-info-name">Electrabot</div></div><div class="msg-text">' +
      msg.message +
      "</div></div></div>";
  } else {
    msgHTML +=
      '<div class="msg right-msg"><div class="msg-bubble"><div class="msg-info"><div class="msg-info-name">You</div></div><div class="msg-text">' +
      msg.message +
      "</div></div></div>";
  }
  msgerChat.insertAdjacentHTML("beforeend", msgHTML);
}

msgerSendBtn.addEventListener("click", submitForm);
msgerInput.addEventListener("keyup", function (event) {
  if (event.keyCode === 13 || event.code === "Enter") {
    submitForm(event);
  }
});
