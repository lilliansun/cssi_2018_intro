console.log('Hello World!');

const name = 'Charlie';
console.log('Hello ' + name + '!');
console.log('Hello ${name}!');

const age = 16;
console.log('You are ' + age + ' years old');
console.log('You are ${age+1} years old');

//line comment
/* block
comment */
/** documentation comment */


if (age >= 18) {
  console.log('You can get your driver\'s license and vote');
} else if (age >=15 ){
  console.log('You can get your permit but can\'t vote')
} else {
  console.log('Sorry, you can\'t vote or get your license')
}

function makeGreetingMessage(name1, name2=null) {
  if (name2 == null)
    return `Hello ${name1}`;
  else {
  //code
    return `Hello ${name1} and ${name2}`;
  }
}


function greet(name1, name2=null) {
  console.log(makeGreetingMessage(name1, name2));
}

const multiplyBy3 = (x) => x*3;

/*setInterval(() => {
  console.log(new Date());
}, 1000)
*/
greet("Alice");


//Data Structures//
/**empty array: []*/
const emptyArray = [];
const nonEmptyArray = [1, 2, 3, 4];

//For loops//
for (let i = 0; i <4; i++)
{
  console.log(nonEmptyArray[i]);
}
//foreach loops//
nonEmptyArray.forEach((name) =>{
  console.log(`forEach: ${name}`);
})

const article  = {
  name: 'Dog family gives birth to liter of 10 puppies.',
  views: 1234,
  datePublished: '03/25/2018',
};

document.addEventListener('DOMContentLoaded', () => {
const floatingBox = document.querySelector('.floatingBox');
let boxTop = 100;
let boxLeft = 100;
document.addEventListener('keydown', (event) => {
  const key = event.key;
  if (key==="ArrowDown"){
    boxTop+=5
  } else if(key === "ArrowUp"){
    boxTop-=5;
  } else if (key==="ArrowLeft"){
    boxLeft-=5;
  } else if (key==="ArrowRight"){
    boxLeft+=5;
  } else {
    return;
  }
  floatingBox.style.top = boxTop + 'px';
  floatingBox.style.left = boxLeft + 'px';
  console.log(event);
});

});
