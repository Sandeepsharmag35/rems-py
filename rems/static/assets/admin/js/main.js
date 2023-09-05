// add hovered class to selected list item
let list = document.querySelectorAll(".navigation li");

function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

// Menu Toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function () {
  navigation.classList.toggle("active");
  main.classList.toggle("active");
};


const imageUploader = document.querySelector("input");
const imagePreview = document.querySelector("img");

function showImage() {
  let reader = new FileReader();
  reader.readAsDataURL(imageUploader.files[0]);
  reader.onload = function (e) {
    imagePreview.classList.add("show");
    imagePreview.src = e.target.result;
  };
}