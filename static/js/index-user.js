$(document).on("DOMContentLoaded", () => {
    console.log("kontenloaded");
    getQuestion();
});

$("#formCreateQuestion").on("submit", (e) => {
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: "create-question/",
        data: $("#formCreateQuestion").serialize(),
        success: (data) => {
            console.log(data);
            $("#questionModal").modal("hide");
            functionSetQuestionUser(data, data.fields.id);
        },
        error: (e) => {
            alert("Error: ", e);
        },
    });
});

const editQuestion = function (pk) {
    console.log("edit bro 1");
    // let bgk = thisElement.parents(".card-body")
    // let bgk2 = thisElement.parents(".card-body")
    let title = $(`#${pk}`).find(".card-title").text();
    let description = $(`#${pk}`).find(".card-text").text();

    $("#formEditQuestion input[name='title']").val(title);
    $("#formEditQuestion textarea[name='description']").val(description);
    console.log(
        "This is " + $("#formEditQuestion textarea[name='description']").val()
    );
    $("#editQuestionModal").show();
    formEditQuestionSubmit(pk);
};

const formEditQuestionSubmit = (pk) => {
    console.log("edit bro 2");
    $("#formEditQuestion").on("submit", (e) => {
        e.preventDefault();
        let dt = $("#formEditQuestion").serialize();
        $.ajax({
            url: `recycle/edit-question/${pk}/`,
            type: "POST",
            data: dt,
            success: (response) => {
                $("#editQuestionModal").modal("hide");
                $(`#${pk}`).find(".card-title").text(response.fields.title);
                $(`#${pk}`)
                    .find(".card-text")
                    .text(response.fields.description);
            },
            error: (e) => {
                alert("Error: ", e);
            },
        });
    });
};

const deleteQuestion = (pk) => {
    console.log("delete bro");
    $.ajax({
        url: `recycle/delete-question/${pk}/`,
        type: "DELETE",
        success: (data) => {
            console.log("success deleting");
            $("#appendCard").html("");
            getQuestion();
        },
        error: (e) => {
            alert("Error: ", e);
        },
    });
};

const getQuestion = () => {
    $.ajax({
        url: "/recycle/json-question-user/",
        method: "GET",
        success: (data) => {
            functionGetQuestionUser(data);
        },
        error: (e) => {
            alert("Error: ", e);
        },
    });

    $.ajax({
        url: "/recycle/json-question-notuser/",
        method: "GET",
        success: (data) => {
            functionGetQuestionNotUser(data);
        },
        error: (e) => {
            alert("Error: ", e);
        },
    });
};

const functionGetQuestionUser = (data) => {
    console.log("ini fungsi get user");
    for (let i = 0; i < data.length; i++) {
        functionSetQuestionUser(data[i], data[i].pk);
    }
};

const functionGetQuestionNotUser = (data) => {
    console.log("ini fungsi get not user");
    console.log(data);

    for (let i = 0; i < data.length; i++) {
        functionSetQuestionNotUser(data[i], data[i].pk);
    }
    // $('#appendInfo').append(
    //     `<div class="container">
    //         <div class="h6">Ada pertanyaan untuk kami?</div>
    //         <p>Klik icon dibawah untuk menambahkan pertanyaanmu!</p>
    //         <a href="{% url 'recycle:createquestion' %}" data-bs-toggle="modal" data-bs-target="#questionModal" style="text-decoration: none; color: inherit;"><i class="fa-solid fa-square-plus fa-spin" style="--fa-animation-duration: 15s;"></i></a>
    //     </div>`
    // )
};

const functionSetQuestionUser = (data, pk) => {
    let d = new Date(data.fields.date.substring(0, 10));
    const date = d.toDateString() + ", " + data.fields.date.substring(11, 19);
    $("#appendCard").append(`
    <div class="card shadow bg-body rounded mx-2 my-2" id="${pk}" style="width: 50rem">
        <div class="card-header bg-success bg-opacity-50">
            <span style="float: left;">${date}</span>
            <button class="findButton" onclick="editQuestion(${pk})" data-bs-toggle="modal" data-bs-target="#editQuestionModal" style="all: unset; float: right; cursor: pointer;"><i class="fa-solid fa-pen"></i></button>
            <button onclick="deleteQuestion(${pk})" style="all: unset; float: right; cursor: pointer; margin-right: 1em;"><i class="fa-solid fa-trash-can"></i></button>
        </div>
        <div class="card-body">
            <h5 class="card-title">${data.fields.title}</h5>
            <p class="card-text">${data.fields.description}</p>
        </div>
        <div class="card-footer text-muted">
            This post was created by you
        </div>
    </div>
    `);
};

const functionSetQuestionNotUser = (data, pk) => {
    let d = new Date(data.fields.date.substring(0, 10));
    const date = d.toDateString() + ", " + data.fields.date.substring(11, 19);
    $("#appendCard").append(`
    <div class="card shadow bg-body rounded mx-2 my-2" id="${pk}" style="width: 50rem"> 
        <div class="card-header bg-success bg-opacity-50">
            Question from user ${data.fields.user}
        </div>
        <div class="card-body">
            <h5 class="card-title">${data.fields.title}</h5>
            <p class="card-text">${data.fields.description}</p>
        </div>
    </div>
    `);
};
