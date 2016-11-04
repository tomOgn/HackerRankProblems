// www.hackerrank.com/challenges/jumping-on-the-clouds

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
    let n = parseInt(readLine());
    let c = readLine().split(' ').map(Number);
    let position = 0;
    let moves = 0;
    while (position != n - 1)
    {
        if (position + 2 < n && c[position + 2] != 1)
        {
            position += 2;
            moves++;
        }
        else
        {
            position++;
            moves++;
        }
    }
    console.log(moves);
}