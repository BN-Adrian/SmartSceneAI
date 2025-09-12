//upload and search

//upload

const fileInput=document.getElementById('fileUpload');
fileInput.addEventListener('change',(event)=>{
    const file=event.target.file[0];
    if(file){
        alert('File selected: ${file.name}');
        //se poate adauga cod pentru upload server
    }
});


//search

const searchButton=document.getElementById('serchButton');
const searchInputt=document.getElementById('serchInput');
searchButton.addEventListener('click',()=>{
    const quare=searchInputt.ariaValueMax.trim();
    if(query){
        alert('search for: ${query}');
    }else{
        alert("add files");
    }
});
