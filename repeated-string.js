// www.hackerrank.com/challenges/repeated-string

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

function main()
{
    var s = readLine();
    var n = parseInt(readLine());
    
    // Number of 'a' within the string.
    const a = s.split('').filter(x => x == 'a').length;
    
    // Total number of 'a' required.
    let countA = Math.floor(n / s.length) * a;
    
    // Possible last word.
    let remainder = n % s.length;
    if (remainder != 0)
        for (let i = 0; i < remainder; i++)
            if (s[i] == 'a')
                countA++;
    
    console.log(countA);
}