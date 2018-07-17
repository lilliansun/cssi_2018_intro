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

if (/**boolean expression*/) {
  // Execute if exrpession is true
} else {
  // Execute if expression is false
}


if (age >= 18) {
  console.log('You can get your driver\'s license and vote');
} else if (age >=15 ){
  console.log('You can get your permit but can\'t vote')
} else {
  console.log('Sorry, you can\'t vote or get your license')
}
