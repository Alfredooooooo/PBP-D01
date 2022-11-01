// format django datetime format to indonesian-readable format
function formatDate(date) {
  var date_js_format = new Date(date);
  let menit= (date_js_format.getMinutes()<10?'0':'') + date_js_format.getMinutes() 
  let date_indo_format =
    date_js_format.getUTCDate() +
    "/" +
    date_js_format.getUTCMonth() +
    1 +
    "/" +
    date_js_format.getFullYear() +
    " " +
    date_js_format.getUTCHours() +
    ":" +
    menit;
  return date_indo_format;
}


function loadRecentlyViewed() {
  let recent_card_content = ``;
  $("#content-recently-viewed").html("");
  $.ajax({
    url: "/event/json-recent/",
    type: "GET",
    dataType: "json",
    success: function (dataList) {
      if (dataList === '[]') {
        recent_card_content = `
          <div class="card p-2" style="width: 16rem;">
          <div class="card-body d-flex justify-content-between text-center " style="text-align: center;">
            <h1 class="d-flex  text-center"style="font-size:1.8rem;font-weight:1000; text-align:center;color: white;">BELUM ADA EVENT YANG ANDA LIHAT:(</h1>
          </div>
          `;
      } else {
        for (let data of dataList) {
          let start_date_formatted = formatDate(data.fields.start_date);
          let finish_date_formatted = formatDate(data.fields.finish_date);
          recent_card_content += `
            <div class="">
              <div class="card p-2" style="width: 16rem; font-size: 0.1rem;">
                <div class="card-body align-item-center justify-content-center">
                  <h4 style="font-size: medium;" id="title-${data.pk}">${data.fields.title}</h4>
                  <div class="d-flex justify-content-between align-items-center">
                    <p style="font-size: small;" class="event-brief" id="brief-${data.pk}">${data.fields.brief}</p>
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
                  <button onClick="showModal(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-solid fa-circle-info"> </i> </button>
                  <button onClick="showForum(${data.pk})" class="btn btn-sm" style="font-size: small; text-align: center; width: fit-content; "><i class="fa-sharp fa-solid fa-comment-dots"> </i> </button>
                </div>
              </div>
            </div>
            `;
        }
      }

      $("#content-recently-viewed").html(recent_card_content);
    },
    error: function (response) {
      console.log("Eror: ", response);
    },
  });
}



$(document).ready(function () {
  loadRecentlyViewed();
  showModal(pk);
});

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
            <h4 class="modal-title" id="modal-judul">📅 ${data.fields.title} 📅</h4>
          </div>
          <div class="modal-body">
            <div class="date-container d-flex flex-column align-item-center">
              <div class="d-flex align-item-center">
                <p class="p-text-date" style="font-size: small; width: fit-content;"> 
                  <i class="fa-solid fa-people-roof"></i> 
                  <span id="text-penyelenggara" style="font-size: small;">Penyelenggara :</span> ${data.fields.user}</p> <br>
              </div>
              <div class="d-flex align-item-center">
                <p class="p-text-date" style="font-size: small; width: fit-content;"> 
                  <i class="fa-solid fa-circle-info"></i> 
                  <span id="text-brief" style="font-size: small;">Brief :</span>  </p> <br>
                  
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
