
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



// Форматирование телефона

const phoneInput = document.getElementsByName('phone11')[0];


// phoneInput.addEventListener('keypress', (event) => {
//     console.log(event.key)
//     if (parseInt(event.key)){
//         event.target.value=8
//     }
//    });
phoneInput.addEventListener('focus', (event) => {
    event.target.value='+7('
   });
phoneInput.addEventListener('keypress', (event) => {
    // +7(953) 986-31-65
    if (parseInt(event.key)) {
        if (event.target.value.length < 4) {
            event.target.value = '+7(';
        }
        if (event.target.value.length === 6) {
            event.target.value += ') ';
        } else if (event.target.value.length === 11) {
            event.target.value += '-';
        } else if (event.target.value.length === 14) {
            event.target.value += '-';
        }
    }
    else{event.target.value=event.target.value.slice(-1);}
});