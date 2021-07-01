## git log

Designed to report Git activity to you. Learn to dig and find what file changed in a commit

git log 					Viewing project's commit history using the default format (author and message)
							Displays committed snapshots. It lets you list the project history, filter it, and search for specific changes. 
git log -3

						 main
						  ↓
9ef9173  ←  7c709f0  ←  b764644
line1       line1 		line1
            line2       line2
            			line3
git log --oneline
b764644 File with three lines
7c709f0 File with two lines
9ef9173 File with one line


git log --raw               WHICH FILES CHANGED
							Show file changed (A: added, M: modified, R: renamed, D: deleted)

git log --patch 			VIEW CHANGES
							Inline diff, a line-by-line display of all changes for each file
git log -p index.js			Single file history  
git log -p -2 				Shows the difference introduced in each commit at level 2...


git log --since=yesterday
git log --since=2.weeks
git log --stat
git blame author name, last modified date, commit hash 
git log to look at the commit history of the overall repo.
git log | grep someFunction -C 3  (3 lines of context)
git log --pretty=format:"%h %an %ar - %s"
git log --pretty=format:"%h %s" --graph
git log --pretty=oneline


	git log --oneline --decorate   
		git log shows where the branch pointers (master, Head) are pointing
			a33d80 (HEAD -` master) Revert "Fix username"
			82d742a Fix username
			b3756bf Name updated
			fc2470c Name added
	
	git log | grep someFunction -C 3 			(-C 3 will show your matches with three lines of context).

	git log --author="John Smith" -p hello.py
	This will display a full diff of all the changes John Smith has made to the file hello.py

	git log --oneline master..some-feature
	.. for comparing branches: displays a brief overview of all the commits that are in some-feature that are not in master.

	git log --graph --oneline --decorate

	git log --pretty=format:"%h %an %ar - %s"

	git log
		Display the entire commit history using the default formatting. If the output takes up more than one screen, you can use Space to scroll and q to exit.

	git log -n `limit`
		Limit the number of commits by `limit`. For example, git log -n 3 will display only 3 commits.

	git log --oneline
		Condense each commit to a single line. This is useful for getting a high-level overview of the project history.

	git log --stat
		Along with the ordinary git log information, include which files were altered and the relative number of lines that were added or deleted from each of them.

	git log -p
		Display the patch representing each commit. This shows the full diff of each commit, which is the most detailed view you can have of your project history.

	git log --author="`pattern`"
		Search for commits by a particular author. The `pattern` argument can be a plain string or a regular expression.

	git log --grep="#1234"
		to find all the commits containing #1234

	git log --grep="`pattern`"
		Search for commits with a commit message that matches `pattern`, which can be a plain string or a regular expression.

	git log `since`..`until`
		Show only commits that occur between `since` and `until`. Both arguments can be either a commit ID, a branch name, HEAD, or any other kind of revision reference.

	git log `file`
		Only display commits that include the specified file. This is an easy way to see the history of a particular file.

		git log -p index.js 				 history of a single file

		git log --since=yesterday
		git log --since=2weeks

	git log --graph --decorate --oneline
		A few useful options to consider.
		--graph 			draw a text based graph of the commits on the left hand side of the commit messages. 
		--C--decorate 		adds the names of branches or tags of the commits that are shown
		--oneline 			shows the commit information on a single line making it easier to browse through commits at-a-glance.


	SAMPLES

		git log 					Displays committed snapshots by date DESC
		git log `file` 				Only display commits that include the specified file
		git log -n `limit` 			Limit the number of commits
		git log -p -2 				Shows commits difference, limit to only the last two entries
		git log --stat 			 	Files altered & how many lines in those files were added and removed
		git log --oneline 			Condense each commit to a single line for getting a high-level overview of the project history
		git log --pretty=oneline 	changes the log output to +/- details
							short
							full
							fuller
		git log --pretty=format:"%h - %an, %ar : %s"
		git log --pretty=format:"%h %s" --graph 		Display an ASCII graph of the branch and merge history beside the log output.
			git log --since=2.weeks
			git log --since="2008-01-15"
			git log --since="2 years 1 day 3 minutes ago"
			git log --author="John Doe"
			git log --grep ="keywords in commit msg"
			git log -Sfunction_name 					 	Takes a string and only shows the commits that introduced a change
															to the code that added or removed that string.

		git log --decorate								Shows where the branch pointers (master, Head) are pointing
														Adds the names of branches or tags
		git log --graph --decorate --oneline 			Text based graph of the commits on the left hand side of the commit messages.

			~ character is useful for making relative references to the parent of a commit.
			For example
				3157e~1 refers to the commit before 3157e
				HEAD~3 is the great-grandparent of the current commit.


		git log -limit   				Limit number of commits by limit. E.g. git log -5 will limit to 5 commits.
		git log --oneline 				Condense each commit to a single line.
		git log -p 						Display the full diff of each commit.
		git log --stat 					Include which files were altered and the relative number of lines that were added or deleted from each of them.
		git log --author=”pattern” 		Search for commits by a particular author.
		git log --grep=”pattern” 		Search for commits with a commit message that matches pattern.
		git log since..until 			Show commits that occur between since and until. Args can be a commit ID, branch name, HEAD, or any other kind of revision reference.
		git log -- file 				Only display commits that have the specified file.
		git log --graph --decorate      --graph flag draws a text based graph of commits on left side of commit msgs. --decorate adds names of branches or tags of commits shown.