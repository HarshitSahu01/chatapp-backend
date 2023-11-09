refresh = () => {
    window.location.reload(true);
};

base_url = 'http://localhost:8000/';
api_key = 'aDCOInSATXaX69eLq3PJQY8_thaOXM2n'

console.log('Script connected')

// window.setTimeout(refresh, 3000);
function fetch_messages(func) {
    fetch(`${base_url}apis/read`,
        {
            method:'POST',
            mode: 'no-cors',
            body: {key:api_key}
        }    
    )
    .then(res => {return res.json();})
    .then(data => {return JSON.stringify(data)})
    .then(data => {console.log(data)});
}

function fetch_groups(func) {
    fetch(`${base_url}apis/groups`,
        {
            method:'POST',
            mode: 'no-cors',
            body: {key:api_key}
        })
    .then(function(res){console.log(res);return res.json();})
    .then(data => {return JSON.stringify(data)})
    .then(data => {console.log(data)});
}
