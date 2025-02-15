document.addEventListener("DOMContentLoaded", function() {
    var modal = document.getElementById("userModal");
    var btn = document.getElementById("profileLogo");
    var span = document.getElementsByClassName("close")[0];
    var usernameButton = document.getElementById("usernameButton");
    var emailButton = document.getElementById("emailButton"); 

    // When the user clicks the button, open the modal 
    btn.onclick = function() {
        modal.classList.add("show");
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.classList.remove("show");
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.classList.remove("show");
        }
    }
    // Toggle username visibility
    usernameButton.onclick = function() {
        toggleUsername();
    }
    emailButton.onclick = function() {
        toggleEmail();
    }
});
function toggleUsername() {
    const usernameSpan = document.getElementById('username');
    usernameSpan.style.display = usernameSpan.style.display === 'none' ? 'inline' : 'none';
}
function toggleEmail() {
    const emailSpan = document.getElementById('email');
    emailSpan.style.display = emailSpan.style.display === 'none' ? 'inline' : 'none';
}