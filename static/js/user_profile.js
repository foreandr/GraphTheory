/* When the user clicks on the button, toggle between hiding and showing the dropdown content
*/
function dropdown_function(my_array) {
    console.log("USERPROFILE.JS FRIENDS: " + globalVariable.friends, globalVariable.friends.length);
    if (globalVariable.friends != "NO FRIENDS"){
        console.log("showing friends");
        for (let i = 0; i < globalVariable.friends.length; i++){
            document.getElementById("myDropdown").innerHTML += `<a href=/${globalVariable.friends[i]}>${globalVariable.friends[i]}</a>`
        }
        document.getElementById("myDropdown").classList.toggle("show");
    }else{
        document.getElementById("myDropdown").innerHTML = "NO FRIENDS"
        document.getElementById("myDropdown").classList.toggle("show");
    }
}

/* Close the dropdown menu if the user clicks outside of it
*/
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
function show_session_items(){
    // console.log("FUNCTION: show_session_items()");
    email = localStorage.getItem("email");
    password = localStorage.getItem("password");

    // console.log(email)
    // console.log(password)

    document.getElementById('session_info').innerHTML = `
    SESSION STORAGE: ${email}
    <br>
    SESSION STORAGE: ${password}
    `;
}

/*
*/
function show_datasets(){
    console.log("asljd");
    show_datasets()
}
show_session_items()


