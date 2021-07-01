# git whatchanged

A legacy command that predates the log function
Show logs with difference each commit introduces

git whatchanged
git whatchanged -p v2.6.12.. include/scsi drivers/scsi    Show as patches the commits since version v2.6.12 that changed any file in the include/scsi or drivers/scsi subdirectories
git whatchanged --since="2 weeks ago" -- gitk             Show the changes during the last two weeks to the file gitk. The "--" is necessary to avoid confusion with the branch named gitk