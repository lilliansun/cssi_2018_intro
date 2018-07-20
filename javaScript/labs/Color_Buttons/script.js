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

// Use querySelector to store the div in a variable.
let redButton = document.querySelector('#red');
let greenButton = document.querySelector('#green');
let blueButton = document.querySelector('#blue');
let clearButton = document.querySelector('#clear');
let box = document.querySelector('#responseBox');
let innerText = "";

// Use addEventListener to respond to a click event.
redButton.addEventListener('click', () => {
  console.log("You clicked the red button!");
  box.style.backgroundColor = "red";
  innerText = innerText + "red ";
  box.innerText = innerText;
  box.style.fontSize = "50px";
  box.style.textAlign = "center";

})

greenButton.addEventListener('click', () => {
  console.log("You clicked the green button!")
  box.style.backgroundColor = "green";
  innerText = innerText + "green ";
  box.innerText = innerText;
  box.style.fontSize = "50px";
  box.style.textAlign = "center";

})

blueButton.addEventListener('click', () => {
  console.log("You clicked the blue button!")
  box.style.backgroundColor = "blue";
  innerText = innerText + "blue ";
  box.innerText = innerText;
  box.style.fontSize = "50px";
  box.style.textAlign = "center";
})

clearButton.addEventListener('click', () => {
  box.style.backgroundColor = "white";
  box.innerText = "";
})
