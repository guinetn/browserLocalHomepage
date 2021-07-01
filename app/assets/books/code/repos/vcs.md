# VERSION CONTROL SYSTEM

VCS (Version Control Systems)
SCM (Source Code Management)
RCS (Revision Control System)
DVCS (DISTRIBUTED VERSION CONTROL SYSTEM): standard for version control in software development.
SVN (tracks differences of a file)

Essential part of the every-day of the modern software team's professional practices even on small solo projects
Software tools helping a software team to manage changes to source code over time. 
keeps track of every modification to the code in a special kind of database
Compare code with earlier versions to fix mistake
Avoid code conflicting

App is organized in a folder structure (file tree). One developer on the team may be working on a new feature while another developer fixes an unrelated bug by changing code, each developer may make their changes in several parts of the file tree.
Distributed development also makes it easier to scale your engineering team

## BENEFITS OF VERSION CONTROL

The goal of really any version control system is to save periodic snapshots of your projects. Once you have a snapshot saved, you can feel safe working on your project as you can always revert back to an earlier snapshot if you make a huge error.
If saving the snapshot is the goal, then staging is the actual act of taking the snapshot before you add it to the photo album (repository) for safe keeping.

* Preserve efficiency and agility as the team scales to include more developers

* A complete long-term change history of every file 
	creation
	deletioneditions
	author, date and written notes

* Branching and merging
	Team members work concurrently on independent streams of changes (branches)
	Facility to merge branches to verify that the changes on each branch do not conflict

	Team workflow
		There are many different workflows that teams can choose to make branching and merging
		Many software teams adopt a practice of branching for each feature or perhaps branching for each release, or both.

