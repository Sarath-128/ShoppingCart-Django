function inf(){

    var user_name=document.getElementById('user_name').value;
    var first_name=document.getElementById('first_name').value;
    var last_name=document.getElementById('last_name').value;
    var email=document.getElementById('email').value;
    var password=document.getElementById('password').value;
    var conf_password=document.getElementById('conf_password').value;

    if( password == conf_password ){
        alert("Please enter the correct password...!")
    }
    else{
        alert("Registration Success")
    }



}