// www.hackerrank.com/challenges/alternating-characters

function alternateCharacters(a)
{
    let deletions = 0
    for (let i = 0; i < a.length - 1; i++)
        if (a[i] == a[i + 1])
            deletions++;
    return deletions;
}

function processData(input)
{
    input = input.split('\n');
    const a = input.splice(1);
    let results = [];
    for (let item of a)
        results.push(alternateCharacters(item.split('')));
    for (let result of results)
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