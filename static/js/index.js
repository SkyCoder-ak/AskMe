


// ===========================FOR CATEGORIES DROPDOWN======================
function showHideDropdown() {
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

// ===========================FOR SECTION COLUMN2======================
// document.getElementById("peoples_link").addEventListener("click", function() {
//     var sectionHome = document.getElementById("section_home");
//     var peoplesBox = document.getElementById("peoples_box");
//     // if (sectionHome.style.display === "none")
//   });

// document.getElementById("peoples_link").addEventListener("click", function(){
//     var sectionHome = document.getElementById("section_home");
//     var peoplesBox = document.getElementById("peoples_box");
//     var ansPage = document.getElementById("ans_page");
//     sectionHome.style.display = "none";
//     peoplesBox.style.display = "block";
//     ansPage.style.display = "none";
// });

// document.getElementById("sec_home_link").addEventListener("click", function(){
//     var sectionHome = document.getElementById("section_home");
//     var peoplesBox = document.getElementById("peoples_box");
//     var ansPage = document.getElementById("ans_page");
//     sectionHome.style.display = "block";
//     peoplesBox.style.display = "none";
//     ansPage.style.display = "none";
// });

// function showHideItem(){
//     var sectionHome = document.getElementById("section_home");
//     var peoplesBox = document.getElementById("peoples_box");
//     var ansPage = document.getElementById("ans_page");
//     sectionHome.style.display = "none";
//     peoplesBox.style.display = "none";
//     ansPage.style.display = "block";
// }
// var ansBtn = document.getElementsByClassName("ans_btn");
// for (i = 0; i < ansBtn.length; i++) {
//     ansBtn[i].addEventListener("click", showHideItem);
// }
// document.getElementsByClassName("ans_btn").addEventListener("click", function(){

// });

// ===========================FOR TOP NAVBAR======================

window.addEventListener("scroll", (event) => {
    let scroll = this.scrollY;
    if (scroll > 10){
        document.getElementById("nav_top").classList.add("sticky");
    }else{
        document.getElementById("nav_top").classList.remove("sticky");
    }
});

document.getElementById('ans_file').onchange = function () {
    var fileElem = document.getElementById("selected_file");
    var fileValue = this.value;
    var fileName = fileValue.replace("C:\\fakepath\\",'')
    fileElem.innerHTML = fileName;
  };

//   =====================READONLY FORM================
function LoginAlert(){
    alert("You need to login first.")
}