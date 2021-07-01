# git reflog

The reflog is a play-by-play listing of switches or changes to references in your local repository

Reference logs, or "reflogs", record when the tips of branches and other references were updated in the local repository. Reflogs are useful in various Git commands, to specify the old value of a reference. For example, HEAD@{2} means "where HEAD used to be two moves ago", master@{one.

Every action you perform inside of Git where data is stored, you can find it inside of the reflog.
A mechanism to record when the tip of branches are updated and reflog command is to manage the information recorded in it

Git keeps track of updates to the tip of branches using a mechanism called reflog. This allows you to go back to changesets even though they are not referenced by any branch or tag. After rewriting history, the reflog contains information about the old state of branches and allows you to go back to that state if necessary.

$ git reflog
189aa32 HEAD@{0}: commit: all deleted: 0 files
e6f1ac7 HEAD@{1}: commit: 5th commit:  5 files
2792e62 HEAD@{2}: commit: 4th commit:  4 files
60699ba HEAD@{3}: commit: 3rd commit:  3 files
4ece4c7 HEAD@{4}: commit: 2nd commit:  2 files
cc6b274 HEAD@{5}: commit: 1st commit:  1 file

759a70d HEAD@{25}: checkout: moving from fix to master
1a7de13 HEAD@{26}: commit: fix virus 2
6b65e3d HEAD@{27}: commit: fix virus 1
759a70d HEAD@{28}: checkout: moving from master to fix
759a70d HEAD@{29}: checkout: moving from nf to master
8fb5e8e HEAD@{30}: commit: can mul
1055dd0 HEAD@{31}: commit: can add
759a70d HEAD@{32}: checkout: moving from master to nf
759a70d HEAD@{33}: commit: 1st change
debbc2e HEAD@{34}: commit (initial): 1st commit				
