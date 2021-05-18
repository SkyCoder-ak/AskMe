// $(document).ready(function(){
//     $('#avtar_img]').change(function(e){
//         var fileName = e.target.files[0].name;
//         alert('The file "' + fileName +  '" has been selected.');
//     });
// });

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

// =================================FOR COVER IMAGE============================
// function previewProfileImage( uploader ) {
//     if (uploader.files && uploader.files[0]) {
//         var imageFile = uploader.files[0];
//         var reader = new FileReader();    
//         reader.onload = function (e) {
//             $('#cover_img').attr('src', e.target.result);
//         }    
//         reader.readAsDataURL( imageFile );
//     }
// }

// $("#cover_img_input").change(function(){
//     previewProfileImage( this );
// });