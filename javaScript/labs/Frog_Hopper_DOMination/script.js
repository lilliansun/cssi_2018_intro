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

let currentlily = 1;
let currentlilyId = '#lilypad' + currentlily;
let frogger = document.querySelector('#frog');
/*use a querySelector to grab your frog from your HTML*/;
let lilypad = document.querySelector(currentlilyId);

frogger.addEventListener('mouseover', function() {
  console.log("hovered");
  frogger.style.width = "80px";
  frogger.style.height = "80px";
})

frogger.addEventListener('mouseout', function() {
  frogger.style.width = "70px";
  frogger.style.height = "70px";
})


frogger.addEventListener('click', function(){
  console.log("hop");
  lilypad.classList.remove("active");

  currentlily = currentlily + 1;
  currentlilyId = "#lilypad" + currentlily;
  lilypad = document.querySelector(currentlilyId);
  frogger.style.left = lilypad.style.left
  frogger.style.top = lilypad.style.top
  lilypad.classList.add("active");
  // Insert what should happen when you click on the frog!

});
