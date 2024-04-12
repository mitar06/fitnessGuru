const autoDismissToastMessages = (messagesContainer) => {
    if(!messagesContainer){
        return;
    }
    messagesContainer.classList.add('opacity-0');
    messagesContainer.classList.add('hidden');

    return;
}

document.addEventListener('DOMContentLoaded', () => {
    const messagesContainer = document.getElementById("messages-container");
    setTimeout(function(){
        autoDismissToastMessages(messagesContainer);
    } , 2000);
});