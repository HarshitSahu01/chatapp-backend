console.log("Personal script");

api_key = 'aDCOInSATXaX69eLq3PJQY8_thaOXM2n';

refresh = () => {location.reload(true)}
// setTimeout(refresh, 2000);

function populate_groups(data) {
    container = document.querySelector('.groups-container');
    for(group of data.data){
        container.innerHTML += `
        <div class="group-box">
            <span class="gb-text">${group}</span>
        </div>`;
    }
}

function populate_posts(data) {
    box = document.querySelector('.message-box');
    box.innerHTML = '';
    for(post of data.data) {
        box.innerHTML = `
            <div class="post-body ">
                <div class="post-data">
                    <span class="sender">${post.user}</span>
                    <span class="time">${post.date}</span>
                </div>
                <div class="post-content">
                    ${post.content}
                </div>
            </div>
        ` + box.innerHTML;
    }
    height = box.clientHeight;
    box.scrollTo(0, height);
}


$(document).ready(() => {
    fetch_groups(api_key, populate_groups);
    fetch_posts(api_key, populate_posts);
})

setInterval(function(){
    fetch_posts(api_key, populate_posts);
}, 1000);

function send_message(){
    msg = document.querySelector('#msg').value;
    document.querySelector('#msg').value = '';
    if (msg.trim() == "") return;
    make_post(msg, api_key, populate_posts);
}