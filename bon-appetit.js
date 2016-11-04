// www.hackerrank.com/challenges/bon-appetit

function bonAppetit(n, k, c, b)
{
    const anna = (c.reduce((s, c) => s + c, 0) - c[k]) / 2;
    return anna == b? "Bon Appetit" : b - anna;    
}

function processData(input)
{
    input = input.split('\n').map(x => x.split(' ').map(Number));
    const n = input[0][0];
    const k = input[0][1];
    const c = input[1];
    const b = input[2][0];
    console.log(bonAppetit(n, k, c, b));
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