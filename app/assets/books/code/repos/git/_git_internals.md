# GIT INTERNALS

- https://betterprogramming.pub/a-short-journey-to-git-internals-fc9d11dd80b7

Git = key-value database. You insert any kind of content into a Git repository, for which Git will give you back a unique identifier (a key) that you can use to retrieve that content.

.git directories 
$ tree -L 1 .git/
.git/
├── HEAD          file that references the HEAD of the master branch
├── config
├── description
├── hooks
├── info
├── objects
└── refs

A “blob”: a sequence of bytes. 
Git blob: contains the exact data as a file stored in the Git key-value data store (while the “actual” file is stored on the file system)
Let’s create a blob:
$ echo hello | git hash-object --stdin -w        -w flag to actually write the object into the object database
ce013625030ba8dba906f756967f9e9ca394464a         “hello” is the “value” in the Git data store
$ git cat-file -p ce013625030ba8dba906f756967f9e9ca394464a
hello
check its type using the -t flag:
$ git cat-file -t ce013625030ba8dba906f756967f9e9ca394464a
blob
$ tree .git/objects/
.git/objects/
├── ce
│   └── 013625030ba8dba906f756967f9e9ca394464a
├── info
└── pack

save another object:
$ echo world | git hash-object --stdin -w
cc628ccd10742baea8241c5924df992b5c019f71
As expected, we now have two directories under .git/objects/:
$ tree .git/objects/
.git/objects/
├── cc
│   └── 628ccd10742baea8241c5924df992b5c019f71
├── ce
│   └── 013625030ba8dba906f756967f9e9ca394464a
├── info
└── pack

Tree Objects
solves the problem of storing the filename and allows storing a group of files together.


Initialized empty Git repo in C:/Temp/tstgit/.git/
git init .
        \__ creates hidden subdirectory that WILL containing all repository files
                \___ \hooks
                \___ \info
                \___ \logs 				commit msg	
                \___ \objects
                        \___ \xx		▲ when git add...
                        \___ \xx		▲ when git add...
                        \___ \info
                        \___ \pack
                \___ \refs
                        \___ \heads
                        \___ \tags 		tags
                \___ config
                \___ description
                \___ HEAD
                        ref: refs/heads/master
git status