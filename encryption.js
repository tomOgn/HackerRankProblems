// www.hackerrank.com/challenges/encryption

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

function encryption(s)
{
    let rows = Math.floor(Math.sqrt(s.length));
    let cols = Math.ceil(Math.sqrt(s.length));
    while (rows * cols < s.length) rows++;
    let lines = [];
    let i = 0;
    for (let row = 0; row < rows && i < s.length; row++)
    {
        let line = [];
        for (let col = 0; col < cols && i < s.length; col++)
        {
            line.push(s[i]);
            i++;
        }
        lines.push(line);
    }
    let digest = new Array(cols).fill('');
    for (const line of lines)
        for (let i = 0; i < cols && i < line.length; i++)
            digest[i] += line[i]
    return digest.join(' ')
}

function main()
{
    var s = readLine();
    console.log(encryption(s));
}