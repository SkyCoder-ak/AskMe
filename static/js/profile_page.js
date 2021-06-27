

function previewProfileImage( uploader ) {
    if (uploader.files && uploader.files[0]) {
        var imageFile = uploader.files[0];
        var reader = new FileReader();    
        reader.onload = function (e) {
            $('#avtar').attr('src', e.target.result);
        }    
        reader.readAsDataURL( imageFile );
    }
}

$("#avtar_img").change(function(){
    previewProfileImage( this );
});



// =======================FOR PASSWORD CHANGE FORM================

function show_password_form() {
    var frm = document.getElementById("password_form");
    frm.style.display = "flex";
}

function hide_password_form() {
    var frm = document.getElementById("password_form");
    frm.style.display = "none";
}

