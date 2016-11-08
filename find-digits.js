// www.hackerrank.com/challenges/find-digits

process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function findDigits(x)
{
    const digits = x.split('');
    const number = parseInt(x);
    let count = 0;
    for (const digit of digits)
        if (digit > 0 && number % digit == 0)
            count++;
    return count;
}

function main()
{
    const t = parseInt(readLine());
    let results = [];
    for (let i = 0; i < t; i++)
        results.push(findDigits(readLine()));
    for (const result of results)
        console.log(result);
}