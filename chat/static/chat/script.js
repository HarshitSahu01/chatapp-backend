refresh = () => {
    window.location.reload(true);
};

base_url = 'http://localhost:8000/';
api_key = 'aDCOInSATXaX69eLq3PJQY8_thaOXM2n'

console.log('Script connected')

function fetch_groups(api_key, func) {
    $.post(`${base_url}apis/groups`,
    {
        key: api_key
    },
     function(data, status){
    console.log("fetch_groups(): data recieved");    
    func(data);
  });
}

function fetch_posts(api_key, func){
    $.post(`${base_url}apis/read`,
    {
        key: api_key 
    },
    (data, status) => {
        console.log("fetch_posts(): data recieved");    
        func(data);
    });
}

function make_post(content, api_key, func){
    $.post(`${base_url}apis/create`,
    {
        key: api_key, 
        content: content
    },
    (data, status) => {
        console.log("fetch_posts(): data recieved");    
        func(data);
    });
}

function func(data) {
    alert(data.msg);
    a = data;
}