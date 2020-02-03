


// more about json
// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON
let requestURL = "../assets/data.json"
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
    const data = request.response;
    console.log(data)

    
    window.addEventListener('resize', () => {
        console.log('resized')
    });

  }
