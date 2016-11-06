// www.hackerrank.com/challenges/balanced-brackets

const closingBrakect = {'(' : ')', '[' : ']', '{' : '}'};

function isBalanced(a)
{
    let startIndex = 0;
    let start = a[startIndex];
    let end = closingBrakect[start];
    let sameAsStart = 0;
    let balanced = false;
    for (let i = 1; i < a.length; i++)
    {
        if (a[i] == start)
            sameAsStart++;
        else if (a[i] == end)
        {
            if (sameAsStart > 0)
                sameAsStart--;
            else
            {
                if (i - startIndex > 1)
                {
                    if ((i - startIndex  - 1) % 2 != 0) return false;
                    balanced = isBalanced(a.slice(startIndex + 1, i));
                    if (!balanced) return false;
                }
                else
                {
                    balanced = true;
                    if (i + 1 < a.length)
                    {
                        balanced = false;
                        i++;
                        startIndex = i
                        start = a[i];
                        end = closingBrakect[start];
                    }
                }    
            }
        }
    }
    return balanced;
}

function main()
{
    const t = parseInt(readLine());
    let strings = [];
    for (let i = 0; i < t; i++)
        strings.push(readLine());
    let results = [];
    for (let string of strings)
        results.push(isBalanced(string.split('')));
    for (const result of results)
        console.log(result? 'YES' : 'NO');
}