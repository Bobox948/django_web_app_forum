document.addEventListener('DOMContentLoaded', function() { // making sure the doam is loaded first, after that we can locate elements by ID easily



  document.getElementById('reply').addEventListener('click', reply)
  document.getElementById('close').addEventListener('click', close)
  
  
  })
  
  
  function reply() {
      var container = document.querySelector('.post') //selecting the post class
      // removing all the childs made, in order to have only one. If this wasn't here, on every reply function click, there will be many children
      while (container.hasChildNodes()) {
          container.removeChild(container.firstChild);
         }
       
      var b1 = document.createElement('div');
      container.appendChild(b1); // creating a div and adding it under the container element
      b1.innerHTML = '<form method="post"><textarea rows="5" cols="50" maxlength="500" id="name"></textarea><button id="save1" type="button" onclick="save()">Save</button></form>'
      // on reply click function, a form with textarea appears with a save button activating the save function
  
  
  }
    
  
  function save(){
  
      
      var content = document.getElementById('name').value // retrieving the value of the element with the "name" id (which is in the form freshly openned on the reply function click above)
  
      var title = document.getElementById('title').innerHTML // retrieving the innerHTML to get the title
  
      fetch('forum/post', { // this is the path we've also created in the urls.py
         
          method: 'POST',
          body: JSON.stringify({
          content: content, // we sending the content and the title
          title: title
  
          })
        })
        .then(response => response.json())
        .then(result => {
          document.getElementById('name').outerHTML = "<div></div>"  // once the sending is done, the save button, the reply button and the textarea all disappears.
          document.getElementById('save1').outerHTML = "<div></div>" 
          document.getElementById('reply').outerHTML = "<div></div>"
  
  
          var container2 = document.querySelector('.post')
          var b2 = document.createElement('div');
          container2.append(b2);
          b2.innerHTML = `<div>Post successfully made!</div>`
        });
  
        
        }
  
  
  function close() {
      var title = document.getElementById('title').innerHTML
      fetch('forum/close', {
         
        method: 'POST',
        body: JSON.stringify({
        title: title
  
        })
      })
      .then(response => response.json())
      .then(result => {
        this.outerHTML= "<div></div>"
        document.getElementById('reply').outerHTML = "<div></div>"
        document.getElementById('title').innerHTML = `[CLOSED] ${title}` // when the function close is activated, the innterHTML puts [CLOSED] in front of the tile variable
  
      });
  
  
  
    }