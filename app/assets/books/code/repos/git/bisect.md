## git bisect		

Use binary search algorithm to find the commit that introduced a bug
a function that allows you to hunt out bad commits
Make a binary search between two given commits and then presents you with a specific commit’s details. You first need to give Git a good commit, where you know your functionality was working, and a bad commit. Note that as long as you have one good commit and one bad, the commits can be years apart 

The git bisect commands allows you to do a binary search of the repository looking for which commit introduced the problem and the regression. In this step we'll find the commit which forgot HTML tags in list.html.
Git bisect takes a number of steps, execute the steps in order to see the results.


$id: commit, branch, tagname

git bisect start 			Enter into bisect mode
git bisect good $id
git bisect bad $id
git bisect bad/good
git bisect vizualize
git bisect reset

Once in bisect mode you define your current checkout as bad using git bisect bad. This indicates that it contains the problem your searching to see when it was introduced.
We've defined where a bad commit happened, we now need to define when the last known good commit was using git bisect good HEAD~5. In this case it was five commits ago.
Step 3 will checkout the commit in-between bad and good commits. You can then check the commit, run tests etc to see if the bug exists. In this example you can check the contents using cat list.html
This commit looks good as everything has correct HTML tags. We tell Git we're happy using git bisect good. This will automatically check out the commit in the middle of the last known good commit, as defined in step 5 and our bad commit.
As we did before we need to check to see if the commit is good or bad. cat list.html
This commit has missing HTML tags. Using git bisect bad will end the search and output the the related commit id.
The result is that instead of searching five commits, we only searched two. On a much larger timescale bisect can save you signifant time.

