console.log("hello world test");

function show_session_items(){
    email = localStorage.getItem("email");
    password = localStorage.getItem("password");

    //console.log(email)
    // console.log(password)

    document.getElementById('session_info').innerHTML = `
    SESSION STORAGE: ${email}
    <br>
    SESSION STORAGE: ${password}
    `;
}
show_session_items()