var email ;
var password;
var email2;
var password2;

function login(){
    email = document.getElementById("Lemail").value
    password = document.getElementById("Lpassword").value
    
    console.log(email)
    console.log(password)

    fetch("http://127.0.0.1:8000/api/login/", {

        method: "POST",
        body: JSON.stringify({
            email: email,
            password: password,
        }),
        headers: {
            "content-type": "application/json ; charset=UTF-8"
        },

    })
        .then(function (data) {
           
            console.log(data);
            return data.json();
        })
        .then(function (data) {
            alert(data)
            console.log(data.success);
          
            a = data.success;

            if (a==true){
                alert("1234")
                location.href = "https://www.youtube.com/"
            }

            else{
                alert("You entered wrong username or password")
            }


           
            
           

        })

    }



function signup() {
    email2 = document.getElementById("Semail").value
    password2 = document.getElementById("Spassword").value

    

    console.log(email2)
    console.log(password2)
    console.log("arpan")
    alert("??????????????")
}
