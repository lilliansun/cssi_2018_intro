// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

console.log(dataObject);
console.log(dataObject.data["0"].images.original.url);

let create = document.querySelector('#create');
let del = document.querySelector('#delete');
let body = document.querySelector('body');
let random = document.querySelector('#random');

create.addEventListener('click', ()=>{
  dataObject.data.forEach(function (object) {

    url = object.images.original.url;
    img = document.createElement('img');
    title = object.title;
    text = document.createElement('h6');

    img.src = url;
    img.style.height = "200px";
    img.style.width = "200px";
    img.classList.add('gif');

    text.innerText = title;
    text.classList.add('gif');

    body.append(text);
    body.append(img);



  })

})

del.addEventListener('click', ()=>{
  gif = document.querySelector('.gif');
  while(gif!=null){
    body.removeChild(gif)
    gif = document.querySelector('.gif');
  }
})

random.addEventListener('click', ()=> {
  index = Math.floor(Math.random()*10);
  newUrl = dataObject.data[index].images.original.url;
  
})
