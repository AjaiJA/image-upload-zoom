let clickedPopupImg=document.querySelector('.popup-click-img')
let totalImg=document.querySelectorAll('.image-view-zoom')

for(let i=0;i<totalImg.length;i++){
    totalImg[i].addEventListener('click',ApplyPopup)
}

function ApplyPopup(e){
    let filePath=e.target.src
    clickedPopupImg.src=filePath;
    clickedPopupImg.alt=filePath
    document.querySelector('.modal-img-path').innerHTML=filePath.replace("http://localhost:8000/Media/","");
}