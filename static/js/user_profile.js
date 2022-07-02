function demo_friends(){
    document.getElementById('friends_display').innerHTML += "daskjh"
}
function show_session_items(){
    console.log("FUNCTION: show_session_items()");
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