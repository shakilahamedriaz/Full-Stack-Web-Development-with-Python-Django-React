// String Methods Examples

// charAt(index) : returns the character at the specified index
let str1 = "Hello";
let char = str1.charAt(1);
// output: "e" (character at index 1)

// concat(str1, str2, ...) : combines the text of two or more strings
let str2 = "Hello";
let str3 = "World";
let combined = str2.concat(" ", str3);
// output: "Hello World"

// includes(substring) : checks if a string contains the specified substring
let str4 = "Hello World";
let hasHello = str4.includes("Hello");
// output: true (since "Hello" is in the string)

// indexOf(substring) : returns the index of the first occurrence of a substring
let str5 = "Hello World";
let index = str5.indexOf("World");
// output: 6 (index where "World" starts)

// lastIndexOf(substring) : returns the index of the last occurrence of a substring
let str6 = "Hello World, Hello Universe";
let lastIndex = str6.lastIndexOf("Hello");
// output: 13 (index where "Hello" starts last)

// startsWith(searchString) : checks if a string starts with the specified substring
let str7 = "Hello World";
let startsWithHello = str7.startsWith("Hello");
// output: true (since the string starts with "Hello")

// endsWith(searchString) : checks if a string ends with the specified substring
let str8 = "Hello World";
let endsWithWorld = str8.endsWith("World");
// output: true (since the string ends with "World")

// match(regexp) : searches a string for a match against a regular expression
let str9 = "Hello World";
let matchResult = str9.match(/World/);
// output: ["World"] (array containing the matched substring)

// replace(searchValue, newValue) : replaces a substring with another substring
let str10 = "Hello World";
let replacedStr = str10.replace("World", "Universe");
// output: "Hello Universe" (replaces "World" with "Universe")
