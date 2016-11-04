/*
Find the minimum greater character on the right-side,
given an index of an array of characters.
E.g.: {a = ['f', 'a', 'd', 'c'], i = 1} => {min = {index: 3, value: 'c'}} 
*/
function findMinGreaterRight(a, i)
{
    let min = null;
    for (let j = i + 1; j < a.length; j++)
        if (a[j] > a[i] && (min == null || min.value > a[j]))
            min = { index: j, value: a[j] };
    return min
}

function evaluateTest(test)
{
    let i, greater;
    
    /*
    Iterate, starting from the second-last character, 
    until there is a greater character on its right.
    */
    for (i = test.length - 2; i >= 0; i--)
    {
        greater = findMinGreaterRight(test, i);
        if (greater != null) break;
    }

    /*
    If no greater character has been found, then there is no answer.
    E.g.: test = 'bb'
    */
    if (greater == null) return "no answer";
    
    // Else, swap the two characters.
    const tmp = test[i];
    test[i] = greater.value;
    test[greater.index] = tmp;
    
    // Now order the right side.
    let rightSide = test.slice(i + 1);
    rightSide.sort((a, b) => {
        if (a > b) return 1;
        if (a < b) return -1;
        return 0;
    });
    
    /* 
    Return the concatenation between the left side, 
    the modified character and the ordered right side.
    */
    return test.slice(0, i + 1).concat(rightSide).join('');
}

function processData(input)
{
    let tests = input.split('\n').slice(1);
    let output = [];

    for (let test of tests)
        output.push(evaluateTest(test.split('')));  
    for (const result of output)
        console.log(result); 
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});