
var email1;
var password1;

var email2;
var password2;

function login2() {

    email1 = document.getElementById("Lemail").value
    password1 = document.getElementById("Lpassword").value

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    console.log(email1)
    console.log(password1)

    alert(csrftoken)

    fetch("/api/login/", {
        method: "POST",
        body: JSON.stringify({
            email: email1,
            password: password1
        }),
        headers: {
            "content-type": "application/json ; charset=UTF-8",
            'X-CSRFToken': csrftoken

        },

    })
        .then(function (data) {
            console.log(data);
            alert(data.status)
            a = data.status;

            if (a == 200) {
                window.location.href = "https://www.youtube.com/";

            }

            else {
                alert("enter correct username or password...")
            }
        })

}




function signup() {
    email2 = document.getElementById("Semail").value
    password2 = document.getElementById("Spassword").value

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    console.log(email2)
    console.log(password2)
    alert(csrftoken)

    console.log("arpan")


    fetch("http://127.0.0.1:8000/api/register",
        {

            method: "POST",
            body: JSON.stringify({
                email: email2,
                password: password2,

            }),
            headers: {

                "content-type": "application/json ; charset=UTF-8",
                'X-CSRFToken': csrftoken
            },

        })
        .then(function (data) {
            console.log(data);
            return data.json();
        })
        .then(function (data) {
            console.log(data);
            alert("qwertyuio")

            location.href = "http://127.0.0.1:8000/login/";
        })




}
var start_date;
var end_date;
var leave_Reason;
var leave_commet;



function leavesfatch() {

    start_date = document.getElementById("sdate").value;
    end_date = document.getElementById("edate").value;
    leave_Reason = document.getElementById("reason").value;
    leave_commet = document.getElementById("comt").value;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch("http://127.0.0.1:8000/api/applyleaves/", {
        method: "POST",
        body: JSON.stringify({
            startdate: start_date,
            enddate: end_date,
            reason: leave_Reason,
            comments: leave_commet
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
            'X-CSRFToken': csrftoken
        },
    })
        .then(function (data) {
            return data.json();
        })
        .then(function (data) {
            console.log(data);
            fetchData();
        });
}



var html = "";

function fetchData() {

    var html = "";

    // alert("************************")
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


    fetch(`http://127.0.0.1:8000/api/leavesget/`, {
        // method: "GET",
        headers: {
            "Content-type": "application/json; charset=UTF-8",
            'X-CSRFToken': csrftoken


        },
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            data.forEach((data) => {
                console.log(data);
                var id = data.id;
                console.log(id);
                html += `
                        <tr>
                            <td>${data.id}</td>
                            <td>${data.startdate}</td>
                            <td>${data.enddate}</td>
                            <td>${data.reason}</td>
                            <td>${data.comments}</td>
                                       
                                         
                                        <td>
                                        
                                                <button type="button"  class="btn btn-danger  appoin" data-id="${data.id}" data-toggle="modal" data-target="#exampleModal2">
                                                    <i class="fa fa-pencil text-warning" ></i>
                                                </button>
                                           

                                           
                                              <a href = "">
                                                <button type="button" class="btn mx-1" onclick = "deleteCategory(${id})">
                                                    <i class="fa fa-trash text-danger"></i>
                                                </button>
                                                </a>
                                        </td>
                          </tr> `;


            });
            document.getElementById("table1").innerHTML = html;

        })

}

fetchData();



function deleteCategory(id) {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(`http://127.0.0.1:8000/api/delete/${id}`, {
        method: "DELETE",
        headers: {
            "Content-type": "application/json; charset=UTF-8",
            'X-CSRFToken': csrftoken
        },
    })
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            alert("Do you want to Delete this data?");
            showCategory();
            console.log(data)

        });
}



