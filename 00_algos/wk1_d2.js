/* 
    String: Reverse
    Given a string,
    return a new string that is the given string reversed
*/

const str1 = "creature";
// const expected1 = "erutaerc";

const str2 = "dog";
// const expected2 = "god";

const str3 = "hello";
// const expected3 = "olleh";

const str4 = "";
// const expected4 = "";


function reverseString(str) {
    var newString = "";
    for(let i = str.length - 1; i >= 0; i--);
        newString += str[i];
}

function reverseString(str) {
    var newString = "";
    for (var i = str.length - 1; i >= 0; i--) {
        newString += str[i];
    }
    return newString;
}


//TEST CODE FOR REVERSE
console.log(reverseString(str1)) // Expected: erutaerc
console.log(reverseString(str2)) // Expected: god
console.log(reverseString(str3)) // Expected: olleh
console.log(reverseString(str4)) // Expected: ""