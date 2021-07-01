## git blame `filename`

git blame `file`	
Who changed what and when in a file
to get an author name, last modified date, and commit hash for every single line
to discover why and when a certain line was added/removed and have Git annotate each line of a source file with the name and date it came into existence

If trying to discover why and when a certain line was added, cut to the chase and have Git annotate each line of a source file with
the name and date it came into existence

git blame on a file to get an author name, last modified date, and commit hash for every single line
to figure out the author and track him or her down for questioning

git blame -L 6,8 list.html
If we know the lines which we're concerned with then we can use the -L parameter to provide a range of lines to output.

