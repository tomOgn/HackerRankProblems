// https://www.hackerrank.com/challenges/sparse-arrays

function sparseArrays(strings, queries)
{
    let results = [];
    for (const query of queries)
        results.push(strings.filter(x => x == query).length);
    return results;
}

function processData(input)
{
    input = input.split('\n');
    const n = parseInt(input[0]);
    const strings = input.slice(1, n + 1);
    const q = parseInt(input[n + 1]);
    const queries = input.slice(n + 2);
    let results = sparseArrays(strings, queries);
    for (result of results)
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