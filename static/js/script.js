
let img_link = document.getElementById("img_link");

function setImageUrl() {
    const link = img_link.value;
    let my_img = document.getElementById("profile_img");
    if (link) {
        my_img.alt = "Не получилось загрузить картинку";
        my_img.src = link;

    } else {
        my_img.alt = 'Вставте ссылку на картинку';
        my_img.src = "#";
    }
}


img_link.addEventListener("change", function () {
    setImageUrl();
});
// document.getElementById("img_link").addEventListener("focus", function(){setImageUrl();});
// document.getElementById("img_link").addEventListener("focusout", function(){setImageUrl();});
// document.getElementById("img_link").addEventListener("keydown", function(){setImageUrl();});
// document.getElementById("img_link").addEventListener("blur", function(){setImageUrl();});