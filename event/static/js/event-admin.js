// format django datetime format to indonesian-readable format
function formatDate(date) {
    var date_js_format = new Date(date);
    let menit= (date_js_format.getMinutes()<10?'0':'') + date_js_format.getMinutes() 
    let month =date_js_format.getMonth() +  1 
    let date_indo_format =
      date_js_format.getDate() +
      "/" +
      month +
      "/" +
      date_js_format.getFullYear() +
      " " +
      date_js_format.getHours() +
      ":" +
      menit;
    return date_indo_format;
  }
  
  function loadYourEvent(){
    let your_card_content=``;
    $.ajax({
      url: "/event/json-your/",
      type: "GET",
      dataType: "json",
      success: function (dataList) {
        if (dataList.length >=1) {
          document.getElementById("button-hidden").style.display="";
          $("#input-your-content").html("");
  
          for (let data of dataList) {
            let start_date_formatted = formatDate(data.fields.start_date);
            let finish_date_formatted = formatDate(data.fields.finish_date);
            let brief= data.fields.brief
            if(brief.length>30){
              brief= brief.slice(0,27) +"..."
            }
            your_card_content += `
              <div class="" id="event-${data.pk}">
                <div class="card p-2" style="width: 16rem; font-size: 0.1rem;">
                  <div class="card-body align-items-center justify-content-center">
                    <h4 style="font-size: medium;" id="title-${data.pk}">${data.fields.title}</h4>
                    <div class="d-flex justify-content-center align-items-center">
                      <p style="font-size: small;" class="event-brief" id="brief-${data.pk}">${brief}</p>
                    </div>
  
                    <div class="date-container d-flex flex-row align-items-center">
                      <div class="d-flex align-item-center">
                        <p class="p-text-date" style="font-size: small; width: fit-content;"> <i class="fa-regular fa-calendar"></i> <span id="text-mulai" style="font-size: small;">Start :</span>
                          ${start_date_formatted}</p> <br>
                      </div>
  
                      <div class="d-flex align-item-center">
                        <p class="p-text-date" style="font-size: small; width: fit-content;"> <i class="fa-regular fa-calendar-xmark"></i> <span id="text-selesai" style="font-size: small; width: fit-content;">Finish :</span> 
                        ${finish_date_formatted}</p>
                      </div>
                    </div>
                  </div>
  
                  <div class="card-command-button d-flex justify-content-around align-item-center">
                    <button onClick="deleteEvent(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-solid fa-trash-can"></i></button>
                    <button onClick="showModal(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-solid fa-circle-info"> </i> </button>
                    <button onClick="showForum(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-sharp fa-solid fa-comment-dots"> </i> </button>
                  </div>
                </div>
              </div>
              `;
          }
          
        } else {
          document.getElementById("button-hidden").style.display="";
          your_card_content = `
            <div class="null-text">
              <h1>Anda Belum Memiliki Event. Tekan tombol (+) diatas untuk menambahkan Event Baru.</h1>
            </div>
            `;
        }
  
        $("#input-your-content").html(your_card_content);
      },
      error: function (response) {
        console.log("Eror: ", response);
      },
    });
  
  }
  function deleteEvent(pk){
    $.ajax({
      type: "DELETE",
      url: `/event/delete-event/${pk}`,
      success: (data) => {
          loadYourEvent();
          loadRecentlyViewed();
          loadNowEvent();
          loadFutureEvent();
          loadPastEvent();
      },
      error: (e) => {
          alert("Error: ", e);
      },
  });
  
  }
  
  
  $("#formCreateEvent").on("submit", (e) => {
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: "/event/add-event/",
        data: $("#formCreateEvent").serialize(),
        success: (data) => {
            console.log(data);
            loadYourEvent();
            loadRecentlyViewed();
            loadNowEvent();
            loadFutureEvent();
            loadPastEvent();
        },
        error: (e) => {
            alert("Error: ", e);
        },
    });
    $("#createEventModal").modal("hide");
    $("#formCreateEvent").trigger("reset");
  });
  
  
  function loadRecentlyViewed() {
    let recent_card_content = ``;
    $.ajax({
      url: "/event/json-recent/",
      type: "GET",
      dataType: "json",
      success: function (dataList) {
        if(dataList.length>=1){
          for (let data of dataList) {
            let start_date_formatted = formatDate(data.fields.start_date);
            let finish_date_formatted = formatDate(data.fields.finish_date);
            let brief= data.fields.brief
            if(brief.length>30){
              brief= brief.slice(0,27) +"..."
            }
            recent_card_content += `
            <div class="" id="event-${data.pk}">
            <div class="card p-2" style="width: 16rem; font-size: 0.1rem;">
              <div class="card-body align-item-center justify-content-center">
                <h4 style="font-size: medium;" id="title-${data.pk}">${data.fields.title}</h4>
                <div class="d-flex justify-content-between align-items-center">
                  <p style="font-size: small;" class="event-brief" id="brief-${data.pk}">${brief}</p>
                </div>

                <div class="date-container d-flex flex-row align-item-center">
                  <div class="d-flex align-item-center">
                    <p class="p-text-date" style="font-size: small; width: fit-content;"> <i class="fa-regular fa-calendar"></i> <span id="text-mulai" style="font-size: small;">Start :</span>
                      ${start_date_formatted}</p> <br>
                  </div>

                  <div class="d-flex align-item-center">
                    <p class="p-text-date" style="font-size: small; width: fit-content;"> <i class="fa-regular fa-calendar-xmark"></i> <span id="text-selesai" style="font-size: small; width: fit-content;">Finish :</span> 
                    ${finish_date_formatted}</p>
                  </div>
                </div>
              </div>

              <div class="card-command-button d-flex justify-content-around align-item-center">
                <button onClick="deleteEvent(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-solid fa-trash-can"></i></button>
                <button onClick="showModal(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-solid fa-circle-info"> </i> </button>
                <button onClick="showForum(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-sharp fa-solid fa-comment-dots"> </i> </button>
              </div>
            </div>
          </div>
              `;
          }
  
        }
        else {
          recent_card_content = `
          <div class="null-text">
          <h1>
          Belum ada Event yang Anda lihat saat ini. ☹️
          </h1>
          </div>
          `;
        }
  
        $("#input-recent-content").html(recent_card_content);
      },
      error: function (response) {
        console.log("Eror: ", response);
      },
    });
  }
  
  function loadNowEvent() {
    let now_card_content = ``;
    $.ajax({
      url: "/event/json-all/",
      type: "GET",
      dataType: "json",
      success: function (dataList) {
        if (dataList.length<1) {
          now_card_content = `
            <div class="null-text">
            <h1>
            Belum ada Event yang berlangsung saat ini. ☹️
            </h1>
            </div>
            `;
        } else {
          for (let data of dataList) {
            let now_date =new Date();
            let start_date= new Date(data.fields.start_date);
            let finish_date= new Date(data.fields.finish_date);
            let start_date_formatted = formatDate(data.fields.start_date);
            let finish_date_formatted = formatDate(data.fields.finish_date);
            let brief= data.fields.brief

            if(brief.length>30){
              brief= brief.slice(0,27) +"..."
            }
            if(start_date<=now_date && finish_date>=now_date){
              now_card_content += `
              <div class="" id="event-${data.pk}">
                <div class="card p-2" style="width: 16rem; font-size: 0.1rem;">
                  <div class="card-body align-item-center justify-content-center">
                    <h4 style="font-size: medium;" id="title-${data.pk}">${data.fields.title}</h4>
                    <div class="d-flex justify-content-between align-items-center">
                      <p style="font-size: small;" class="event-brief" id="brief-${data.pk}">${brief}</p>
                    </div>
  
                    <div class="date-container d-flex flex-row align-item-center">
                      <div class="d-flex align-item-center">
                        <p class="p-text-date" style="font-size: small; width: fit-content;"> <i class="fa-regular fa-calendar"></i> <span id="text-mulai" style="font-size: small;">Start :</span>
                          ${start_date_formatted}</p> <br>
                      </div>
  
                      <div class="d-flex align-item-center">
                        <p class="p-text-date" style="font-size: small; width: fit-content;"> <i class="fa-regular fa-calendar-xmark"></i> <span id="text-selesai" style="font-size: small; width: fit-content;">Finish :</span> 
                        ${finish_date_formatted}</p>
                      </div>
                    </div>
                  </div>
  
                  <div class="card-command-button d-flex justify-content-around align-item-center">
                    <button onClick="deleteEvent(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-solid fa-trash-can"></i></button>
                    <button onClick="showModal(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-solid fa-circle-info"> </i> </button>
                    <button onClick="showForum(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-sharp fa-solid fa-comment-dots"> </i> </button>
                  </div>
                </div>
              </div>
              `;
            }
          }
  
          if(now_card_content == ``){
            now_card_content = `
            <div class="null-text">
            <h1>
            Belum ada Event yang berlangsung saat ini. ☹️
            </h1>
            </div>
            `;
          }
        }
  
        $("#input-now-content").html(now_card_content);
      },
      error: function (response) {
        console.log("Eror: ", response);
      },
    });
  }
  
  function loadFutureEvent() {
    let future_card_content = ``;
    $.ajax({
      url: "/event/json-all/",
      type: "GET",
      dataType: "json",
      success: function (dataList) {
        if (dataList.length<1) {
          future_card_content = `
            <div class="null-text">
            <h1>
            Belum ada Event di waktu mendatang ☹️
            </h1>
            </div>
            `;
        } else {
          for (let data of dataList) {
            let now_date =new Date();
            let start_date= new Date(data.fields.start_date);
            let finish_date= new Date(data.fields.finish_date);
            let start_date_formatted = formatDate(data.fields.start_date);
            let finish_date_formatted = formatDate(data.fields.finish_date);
            let brief= data.fields.brief

            if(brief.length>30){
              brief= brief.slice(0,25) +"..."
            }
            if(start_date>now_date){
              future_card_content += `
              <div class="" id="event-${data.pk}">
                <div class="card p-2" style="width: 16rem; font-size: 0.1rem;">
                  <div class="card-body align-item-center justify-content-center">
                    <h4 style="font-size: medium;" id="title-${data.pk}">${data.fields.title}</h4>
                    <div class="d-flex justify-content-between align-items-center">
                      <p style="font-size: small;" class="event-brief" id="brief-${data.pk}">${brief}</p>
                    </div>
  
                    <div class="date-container d-flex flex-row align-item-center">
                      <div class="d-flex align-item-center">
                        <p class="p-text-date" style="font-size: small; width: fit-content;"> <i class="fa-regular fa-calendar"></i> <span id="text-mulai" style="font-size: small;">Start :</span>
                          ${start_date_formatted}</p> <br>
                      </div>
  
                      <div class="d-flex align-item-center">
                        <p class="p-text-date" style="font-size: small; width: fit-content;"> <i class="fa-regular fa-calendar-xmark"></i> <span id="text-selesai" style="font-size: small; width: fit-content;">Finish :</span> 
                        ${finish_date_formatted}</p>
                      </div>
                    </div>
                  </div>
  
                  <div class="card-command-button d-flex justify-content-around align-item-center">
                    <button onClick="deleteEvent(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-solid fa-trash-can"></i></button>
                    <button onClick="showModal(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-solid fa-circle-info"> </i> </button>
                    <button onClick="showForum(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-sharp fa-solid fa-comment-dots"> </i> </button>
                  </div>
                </div>
              </div>
              `;
            }
          }
  
          if(future_card_content == ``){
            future_card_content = `
            <div class="null-text">
            <h1>
            Belum ada Event di waktu mendatang ☹️
            </h1>
            </div>
            `;
          }
        }
  
        $("#input-future-content").html(future_card_content);
      },
      error: function (response) {
        console.log("Eror: ", response);
      },
    });
  }
  
  function loadPastEvent() {
    let past_card_content = ``;
    $.ajax({
      url: "/event/json-all/",
      type: "GET",
      dataType: "json",
      success: function (dataList) {
        if (dataList.length<1) {
          past_card_content = `
            <div class="null-text">
            <h1>
            Belum ada Event telah selesai ☹️
            </h1>
            </div>
            `;
        } else {
          for (let data of dataList) {
            let now_date =new Date();
            let start_date= new Date(data.fields.start_date);
            let finish_date= new Date(data.fields.finish_date);
            let start_date_formatted = formatDate(data.fields.start_date);
            let finish_date_formatted = formatDate(data.fields.finish_date);
            let brief= data.fields.brief

            if(brief.length>30){
              brief= brief.slice(0,27) +"..."
            }
            if(finish_date<=now_date){
              past_card_content += `
              <div class="" id="event-${data.pk}">
                <div class="card p-2" style="width: 16rem; font-size: 0.1rem;">
                  <div class="card-body align-item-center justify-content-center">
                    <h4 style="font-size: medium;" id="title-${data.pk}">${data.fields.title}</h4>
                    <div class="d-flex justify-content-between align-items-center">
                      <p style="font-size: small;" class="event-brief" id="brief-${data.pk}">${brief}</p>
                    </div>
  
                    <div class="date-container d-flex flex-row align-item-center">
                      <div class="d-flex align-item-center">
                        <p class="p-text-date" style="font-size: small; width: fit-content;"> <i class="fa-regular fa-calendar"></i> <span id="text-mulai" style="font-size: small;">Start :</span>
                          ${start_date_formatted}</p> <br>
                      </div>
  
                      <div class="d-flex align-item-center">
                        <p class="p-text-date" style="font-size: small; width: fit-content;"> <i class="fa-regular fa-calendar-xmark"></i> <span id="text-selesai" style="font-size: small; width: fit-content;">Finish :</span> 
                        ${finish_date_formatted}</p>
                      </div>
                    </div>
                  </div>
  
                  <div class="card-command-button d-flex justify-content-around align-item-center">
                    <button onClick="deleteEvent(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-solid fa-trash-can"></i></button>
                    <button onClick="showModal(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-solid fa-circle-info"> </i> </button>
                    <button onClick="showForum(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-sharp fa-solid fa-comment-dots"> </i> </button>
                  </div>
                </div>
              </div>
              `;
            }
          }
  
          if(past_card_content == ``){
            past_card_content = `
            <div class="null-text">
            <h1>
            Belum ada Event yang telah selesai ☹️
            </h1>
            </div>
            `;
          }
        }
  
        $("#input-past-content").html(past_card_content);
      },
      error: function (response) {
        console.log("Eror: ", response);
      },
    });
  }
  
  
  
  
  $(document).ready(function () {
    loadYourEvent();
    loadRecentlyViewed();
    loadNowEvent();
    loadFutureEvent();
    loadPastEvent();
  });
  
  function showCreateEventForm(){
    $("#createEventModal").modal("show");
  }
  
  function showForum(pk){
    window.location.href=`/forum/${pk}/`;
  }
  
  
  function showModal(pk) {
    let modal_content=""
    $.ajax({
      url: `/event/show/${pk}/`,
      type: "GET",
      dataType: "json",
      success: function (dataList) {
        $("input-isi-modal").html("");
        if (dataList == []) {
            modal_content += `
            Can't find data :(
            `;
        } else {
          for (let data of dataList) {
            let start_date_formatted = formatDate(data.fields.start_date);
            let finish_date_formatted = formatDate(data.fields.finish_date);
            modal_content += `
            <div class="modal-content"> 
          <div class="modal-header">
            <h4 class="modal-title" id="modal-judul">Detail Event</h4>
          </div>
          <div class="modal-body">
            <div class="date-container d-flex flex-column align-item-center">
            <div class="d-flex align-item-center">
            <p class="p-text-date" style="font-size: small; width: fit-content;"> 
              <span id="text-brief" style="font-size: small;">📅Judul📅</span>  </p> <br>
          </div>
          <div class="d-flex align-item-start">
          <p class="p-text-date" style="font-size: small; width: fit-content;"> 
          ${data.fields.title}</p> <br>
        </div>
              <div class="d-flex align-item-center">
                <p class="p-text-date" style="font-size: small; width: fit-content;"> 
                  <i class="fa-solid fa-circle-info"></i> 
                  <span id="text-brief" style="font-size: small;">Deskripsi singkat :</span>  </p> <br>
                  
              </div>
              <div class="d-flex align-item-start">
                <p class="p-text-date" style="font-size: small; width: fit-content;"> 
                ${data.fields.brief}</p> <br>
              </div>
              <div class="d-flex align-item-center">
                <p class="p-text-date" style="font-size: small; width: fit-content;"> 
                  <i class="fa-solid fa-rectangle-list"></i>
                  <span id="text-deskripsi" style="font-size: small;">Deskripsi :</span> </p> <br>
              </div>
              <div class="d-flex align-item-start">
                <p class="p-text-date" style="font-size: small; width: fit-content;"> 
                ${data.fields.description}</p> <br>
              </div>
              
              <div class="d-flex align-item-center">
                <p class="p-text-date" style="font-size: small; width: fit-content;"> 
                  <i class="fa-regular fa-calendar"></i>
                  <span id="text-mulai" style="font-size: small;">Waktu dimulai :</span>${start_date_formatted}</p> <br>
              </div>
            <div class="d-flex align-item-center">
                <p class="p-text-date" style="font-size: small; width: fit-content;">
                   <i class="fa-regular fa-calendar-xmark"></i> 
                   <span id="text-selesai" style="font-size: small;">Waktu selesai :</span> ${finish_date_formatted}</p> <br>
              </div>
            </div>
          </div>
          <div class="modal-footer d-flex justify-content-end align-item-end flex-column">
            <button type="button" class="btn btn-secondary btn-danger" onClick="closeModal()" id="btn-close-modal" data-dismiss="modal">Close</button>
          </div>
        </div>
              `;
  
          }
  
        }
  
        $("#input-isi-modal").html(modal_content);
        loadRecentlyViewed();
      },
      error: function (response) {
        console.log("Eror: ", response);
      },
    });
    $("#exampleModal").modal("show");
  }
  
  function closeModal() {
    $("#exampleModal").modal("hide");
  }
  