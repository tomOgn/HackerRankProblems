// www.hackerrank.com/challenges/utopian-tree

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution
{
    static void Main(String[] args)
    {
        var t = Convert.ToInt32(Console.ReadLine());
        var answers = new List<int>();
        for (var i = 0; i < t; i++)
        {
            var n = Convert.ToInt32(Console.ReadLine());
            var spring = true;
            var height = 1;
            for (var j = 0; j < n; j++)
            {
                if (spring)
                    height *= 2;
                else
                    height++;
                spring = !spring;
            }
            answers.Add(height);
        }
        foreach (var answer in answers)
            Console.WriteLine(answer);
    }
}