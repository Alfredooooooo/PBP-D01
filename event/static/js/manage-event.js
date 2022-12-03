function loadTaskData() {
    let eventTableRow = ''
    $("#event-table-body").append('');
    $.ajax({
      url: "/event/json-manager/", 
      type: "GET",
      dataType: "json",
      success: function (dataList){
        
        for (let data of dataList){
          eventTableRow +=`
            <tr id="event-${data.pk}">
            <td data-href="/forum/${data.pk}" >${ data.fields.create_date }</td>
            <td data-href="/forum/${data.pk}" id="title-${data.pk}">${ data.fields.title }</td>
            <td data-href="/forum/${data.pk}" id="brief-${data.pk}" >${ data.fields.brief }</td>
            <td data-href="/forum/${data.pk}" id="description-${data.pk}" >${ data.fields.description }</td>
            <td data-href="/forum/${data.pk}" id="start_date-${data.pk}">${ data.fields.start_date }</td>
            <td data-href="/forum/${data.pk}" id="finish_date-${data.pk}">${ data.fields.finish_date }</td>
            <td> <a id="button-edit-event-${data.pk}" onClick="editEvent(${data.pk})" class="btn btn-primary btn-warning ">Edit</a> <a id="button-delete-event-${data.pk}" onClick="deleteEvent(${data.pk})" class="btn btn-primary btn-danger">Delete</a> </td>
            </tr>
            `
          ;
        }
        $("#event-table-body").html(eventTableRow);
      },
      error: function(response){
        console.log('Eror: ', response);
      }
    });
  } 

  $(document).on("submit", "#createEventForm", function(e) {
    e.preventDefault();
    $.ajax ({
        url: "/event/add-event/",
        type: "POST",
        dataType:"json",
        data: {
            title:$("#title").val(),
            brief:$("#brief").val(),
            description:$("#description").val(),
            start_date:$("#start_date").val(),
            finish_date:$("#finish_date").val(),
        },
        success: function(data) {
            loadTaskData();
        }
    })
})

// function editEvent(pk){
    
//     let title=$(`title-${pk}`).text()
//     let brief=$(`brief-${pk}`).text()
//     let description=$(`description-${pk}`).text()
//     let start_date=$(`start_date-${pk}`).text()
//     let finish_date=$(`finish_date-${pk}`).text()

//     $("#title-edit").val(title)
//     $("#brief-edit").val(brief)
//     $("#description-edit").val(description)
//     $("#start_date-edit").val(start_date)
//     $("#finish_date-edit").val(finish_date)

//     $("#editEventModal").modal('show')
// }

function deleteEvent(pk){
    $.ajax({
        url: `/event/delete-event/${pk}/`,
        type: "DELETE",
        credentials: "include",
        success: function(data) {
            $(`#event-${pk}`).remove()
        }
    })
  }

$(document).ready(function () {
    loadTaskData();
    $('#example').DataTable({
        responsive:true 
    });
});



function closeModal(){
    $("#createEventForm").trigger('reset');
    $('#createEventModal').modal("hide")
  }


document.addEventListener("DOMContentLoaded", () =>{
    const rows = document.querySelectorAll("td[data-href]");

    rows.forEach(row =>{
        row.addEventListener("click", () =>{
            window.location.href = row.dataset.href;
        });
    });
});