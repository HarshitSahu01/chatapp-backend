base_url = 'https://harshitsahu.pythonanywhere.com/';
api_key = '';

console.log('Fetch Script connected');

function fetch_groups(api_key, func) {
    $.post(`${base_url}apis/groups`,
    {
        key: api_key
    },
     function(data, status){
    console.log("fetch_groups(): data recieved" + data.msg);    
    func(data);
  });
}

function fetch_posts(api_key, func){
    $.post(`${base_url}apis/read`,
    {
        key: api_key 
    },
    (data, status) => {
        console.log("fetch_posts(): data recieved:" + data.msg);    
        func(data);
    });
}

function make_post(content, api_key, func){
    $.post(`${base_url}apis/create`,
    {
        key: api_key, 
        content: content
    },
    (data) => {
        console.log("make_posts(): data recieved: " + data.msg);    
        func(data);
    });
}

function test_func(data) {
    console.log(data);
    a = data;
}