## git archive

https://www.atlassian.com/git/tutorials/export-git-archive

Git archive is a helpful utility for creating distributable packages of git repositories. Git archive can target specific refs of a repository and only package the contents of that ref. Git archive has several output formats that can utilize added compression.
To create an archive file of a Git repository. An archive file combines multiple files into a single file. An archive file can then be extracted to reproduce the individual files. Git is incredibly powerful at preserving history and team collaboration; however, archive files remove the overhead of Git's metadata and can be simpler to distribute to other users or preserve in long term cold storage.
Git command line utility that will create an archive file from specified Git Refs like, commits, branches, or trees. 


git archive --format=tar HEAD
                       \___ tar, zip, tar.gz
create an archive from the current HEAD ref of the repository.

git archive --output=./example_repo_archive.tar --format=tar HEAD
create a new archive and store it in the exmaple_repo_archive.tar file

git archive --output=./example_repo_archive.tar.gz --format=tar HEAD ./build
output an archive containing only files stored under the ./build directory