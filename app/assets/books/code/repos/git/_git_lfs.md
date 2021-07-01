## GIT LFS (Large File Storage)

For projects containing large files, particularly large files that are modified regularly, this initial clone can take a huge amount of time, as every version of every file has to be downloaded by the client. Git LFS is a Git extension developed by Atlassian, GitHub, and a few other open source contributors, that reduces the impact of large files in your repository by downloading the relevant versions of them lazily. 

http://www.lafermeduweb.net/billet/git-large-file-storage-vos-fichiers-lourds-hors-de-votre-repo-github-1820.html

large file support (LFS) option. 
It refers to a Git extension aimed at replacing large files (i.e., blobs, images, datasets) with text pointers. 
The actual (large) files stay stored on a remote server while locally you handle them through shorter and 
simpler monikers. 
You can select the types of files you want to handle via LFS on each repository. 
Essentially, LFS allows downloading large files in a lazy way, thus reducing the performance hit of such files 
on your repository.
