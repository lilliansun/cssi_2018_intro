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

setInterval(() => {
  console.log(new Date());
}, 1000)

greet("Alice");
