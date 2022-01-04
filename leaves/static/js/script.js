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

    fetch("http://127.0.0.1:8000/api/login/", {
        method: "post",
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
