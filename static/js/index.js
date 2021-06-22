


// ===========================FOR CATEGORIES DROPDOWN======================
function showHideDropdown(){
    var dropdown = document.getElementById("cate_dropdown");
    var moreBtn = document.getElementById("more_btn");
    if (dropdown.style.height === "12rem") {
        dropdown.style.height = "0.1rem";
        moreBtn.innerHTML = 'More <i class="fas fa-caret-down"></i>';
    }else{
        moreBtn.innerHTML = 'More <i class="fas fa-caret-up"></i>';
        dropdown.style.height = "12rem";
    }
}


// ===========================FOR TOP NAVBAR======================

window.addEventListener("scroll", (event) => {
    let scroll = this.scrollY;
    if (scroll > 10){
        document.getElementById("nav_top").classList.add("sticky");
    }else{
        document.getElementById("nav_top").classList.remove("sticky");
    }
});

// document.getElementById('ans_file').onchange = function () {
//     var fileElem = document.getElementById("selected_file");
//     var fileValue = this.value;
//     var fileName = fileValue.replace("C:\\fakepath\\",'')
//     fileElem.innerHTML = fileName;
//   };

//   =====================READONLY FORM================
function LoginAlert(){
    alert("You need to login first.")
}

// ==================for popup messsage===============
function DismissPopup(){
    document.getElementById("message_main").style.display = "none";
}