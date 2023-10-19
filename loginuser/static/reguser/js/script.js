
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

const phoneInput = document.getElementById('phone');
phoneInput.value='+7('

// phoneInput.addEventListener('keypress', (event) => {
//     console.log(event.key)
//     if (parseInt(event.key)){
//         event.target.value=8
//     }
//    });



function dispatchEvent(event) {
    const input = event.target;
    const regexp = /\d/;
    if (!regexp.test(input.value)) {
    event.preventDefault();
    console.log("dddddddddddddddddddd");
}
}

phoneInput.addEventListener('focus', (event) => {
    event.target.value='+7('
   });
phoneInput.addEventListener('keypress', (event) => {
    // +7(953) 986-31-65
    // if (!parseInt(event.key)) {return;}
    if (event.target.value.length>16) {
    event.preventDefault();
    }
    // const input = event.target;
    const start = '+7(';
    let curr_string = event.target.value;
    // event.target.value=start;


    const regexp = /\d/;
    if (!regexp.test(event.key)) {
    event.preventDefault();
    }

    //Буквы вводить нельзя, но будут зарезервированные символы, которые присоедеинятся к строке
    let tmp='';
    // for (let ch in curr_string)
    for (ch=3;ch<17;ch++)
    {
        if (parseInt(curr_string[ch])){
            if (tmp.length<10) {
                tmp+=curr_string[ch];
            }else{break;}

        }

    }

    console.log(tmp);


    let res='';
    for (let ch in tmp){
        res +=tmp[ch];
        if (res.length === 3) {
            res += ') ';
        } else if (res.length === 8) {
            res += '-';
        } else if (res.length === 11) {
            res += '-';
        }


    }
    console.log(res);
    event.target.value = start+res;
    // console.log(event.target.value)

    //
    // if (event.target.value.length < 4) {
    //     event.target.value = '+7(';
    // }
    // if (event.target.value.length === 6) {
    //     event.target.value += ') ';
    // } else if (event.target.value.length === 11) {
    //     event.target.value += '-';
    // } else if (event.target.value.length === 14) {
    //     event.target.value += '-';
    // }

    // else{event.target.value=event.target.value.slice(-1);}
});