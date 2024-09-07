function log(){
    
    var username=document.getElementById('username').value;
    var password=document.getElementById('password').value;

    if (!username || !password){
        alert("Please Enter valid Elements....!")
    }
    else{
        alert("Login Success")
    }

}