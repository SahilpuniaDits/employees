
var email;
var password;
var email2;
var password2;



function login2() {

    const email = document.getElementById("Lemail").value
    const password = document.getElementById("Lpassword").value
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.log(email)
    console.log(password)

    alert(csrftoken)

    fetch("http://127.0.0.1:8000/api/login/", {
        method: "post",
        body: JSON.stringify({
            'email': email,
            'password': password,
        }),
        headers: {
            "content-type": "application/json ; charset=UTF-8",
            'X-CSRFToken': csrftoken,
            'Accept': 'application/json',
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
    alert("aaaaaaaaa")
    //var leave_type = document.getElementById("leavetype").value;
    // var role = document.getElementById("role");
    // var role_type = role.options[role.selectedIndex].text;
    // console.log(role_type);
    start_date = document.getElementById("sdate").value;
    end_date = document.getElementById("edate").value;
    leave_Reason = document.getElementById("reason").value;
    leave_commet = document.getElementById("comt").value;




    fetch("http://127.0.0.1:8000/api/leaves/", {
            method: "POST",
            body: JSON.stringify({
                // leave_type: role_type,
                // leave_description: leave_description,
                startdate: start_date,
                enddate: end_date,
                reason : leave_Reason,
                comments : leave_commet
            }),
            headers: { "Content-type": "application/json; charset=UTF-8" },
        })
        .then(function(data) {
            return data.json();
        })
        .then(function(data) {
            console.log(data);
        });
}
