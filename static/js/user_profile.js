/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction(my_array) {
    // console.log("\nFRIEND FUNCTION");
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



    // document.getElementById("myDropdown").innerHTML += '<a href="#">Link 1</a>' // FUNCTION TO GET ALL FRINEDS
    // document.getElementById("myDropdown").innerHTML += '<a href="#">Link 1</a>'
}

// Close the dropdown menu if the user clicks outside of it
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