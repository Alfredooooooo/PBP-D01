const info = document.getElementById("info")

const CSRF_TOKEN  = document.getElementById("CSRF_TOKEN").content
const username = document.getElementById("username").content
const logged_in = document.getElementById("logged_in").content
const forum_id = document.getElementById("forum_id").content
const comment_text = document.getElementById("comment_text").innerHTML

async function addClasses() {
  const comments = document.getElementsByName("comment_text")
  for(let i=0; i<comments.length; i++){
    comments[i].placeholder="Comment"
    comments[i].className="form-control m-2"
  }
}

async function getComments() {
  return fetch(`/forum/json/${forum_id}/`).then((res) => res.json())
}

async function refreshComments() {

      const comments = await getComments()
      let htmlString = ``
      comments.forEach((item) => {
        htmlString += `\n<div id="comment${item.pk}" class="card shadow-lg comment">`
        htmlString += `\n<div class="card-header text-white" style="background-color: #359f92;">
            <div class="fw-bold">${item.fields.username}</div>`
        const date = new Date(`${item.fields.datetime}`)
        htmlString += `<div style="text-align:right">${date}</div>
        </div>`
        htmlString += `<div class="card-body">`
        if(item.fields.parent != null){
          htmlString += `\n<a class="card-text" href="#comment${item.fields.parent_pk}">Replying to ${item.fields.parent_username}</a>`
        }
        htmlString += `\n<p class="card-text">${item.fields.comment_text}</p>`
        htmlString += `\n<p class="card-text" align="right">`
        if(logged_in == `True`){
          htmlString += `\n<input id="button${item.pk}" type="button" class="btn btn-primary" value="Reply" onclick="toggleForm(${item.pk})">`
        }
        if(`${item.fields.username}` == username){
          htmlString += `\n<input type="button" class="btn btn-danger" value="Delete" onclick="deleteComment(${item.pk})">`
        }
        htmlString += `\n</p>`
        htmlString += `\n</div></div><br>`
        htmlString += `\n<form class="reply" method="POST" id="form${item.pk}" onsubmit="return false;">`
        htmlString += `\n<input type="hidden" name="csrfmiddlewaretoken" value="${CSRF_TOKEN}">`
        htmlString += `\n${comment_text}`
        htmlString += `\n<input type="submit" value="Send" onclick="addComment(${item.pk})" class="m-2 btn btn-success">`
        htmlString += `\n</form>`
        htmlString += `<br>`
      })
      
      document.getElementById("comments").innerHTML = htmlString
      addClasses()
      toggleForm(0, 1)
}

function addComment(id) {
  fetch(`/forum/add/${forum_id}/${id}/`, {
        method: "POST",
        body: new FormData(document.querySelector(`#form${id}`))
    }).then((res) => {
      if(res.redirected){
        window.location.href = res.url
      }
      refreshComments()
    })
  return false
}

function deleteComment(id) {
  fetch(`/forum/delete/${id}/`, {
        method: "POST",
        body: new FormData(document.querySelector(`#form${id}`))
    }).then(refreshComments)
  return false
}

function toggleForm(id, zero=0) {
  const reply = document.getElementById(`form${id}`)
  const button = document.getElementById(`button${id}`)
  if ((reply.style.display == "none" || reply.style.display == "") && zero==0){
    reply.style.display = "block";
    reply.style.visibility = "visible";
    setTimeout(function(){reply.style.height = "100px";}, 1);
    button.value = "Hide";
  }
  else {
    reply.style.height = "0px";
    reply.style.visibility = "hidden";
    setTimeout(function(){reply.style.display = "none";}, 400);
    if(id == 0){
      button.value = "Add a new comment";
    }
    else{
      button.value = "Reply";
    }
  }
  return false
}

refreshComments()