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

let customer_name;
let balance;
let logged_in = false;
let password;

function testMe(a) {
  return a+4;
}

console.log(testMe(5))

function openAccount(name, startbalance=0, pass){
  balance = startbalance;
  password = pass;
  // Set the value for customer_name equal to name below
  customer_name = name;
  return `${customer_name} has just opened a new account with a balance of $${balance}`;//write the statment you need to return here
}

function login(name, pass){
  if (current_name===name && password === pass){
    logged_in = true;
    return `${current_name} has logged in`;
  }
  else {
    logged_in = false;
    return `Incorrect login`;
  }
}

function logout(){
  logged_in = false;
  return `${current_name} has logged out`;
}

function deposit(value){
  if (!logged_in){
    return "User must log in."
  } else{
    balance = balance + value;
    return `${customer_name} has deposited ${value}. ${customer_name}'s account has $${balance} now`;
  }

  // update the value of balance
  //return the correct statement
}

function withdraw(value){
  if (!logged_in){
    return "User must log in.";
  } else if((balance - value)<0){
    return `Sorry ${customer_name}, you do not have enough money in your account. You need ${Math.abs(balance-value)} more dollars`;
  }
  else {
    balance = balance - value;
    return `${customer_name} has withdrawn $${value}. ${customer_name} now has $${balance} remaining.`;
  }//update the value of balance
  //return the correct statement
}

// Write your script below
console.log(openAccount("Bob", 300));
console.log(deposit(50));
console.log(withdraw(500));
