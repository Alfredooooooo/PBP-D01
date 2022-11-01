$(document).on("DOMContentLoaded", () => {
    console.log("kontenloaded");
    getAllQuestion();
});

const getAllQuestion = () => {
    $.ajax({
        url: "/recycle/json-question-all/",
        method: "GET",
        success: (data) => {
            functionGetQuestionAll(data);
        },
        error: (e) => {
            alert("Error: ", e);
        },
    });
};

const functionGetQuestionAll = (data) => {
    console.log("ini fungsi get all");
    console.log(data);

    for (let i = 0; i < data.length; i++) {
        console.log(data[i]);
        functionSetQuestionAll(data[i], data[i].pk);
    }
};

const functionSetQuestionAll = (data, pk) => {
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
