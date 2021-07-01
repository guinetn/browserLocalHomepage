## git bundle

Bundle prepares binary diffs for transport on a USB stick or via email. 
These binary diffs can be used to “catch up” a repository that is behind otherwise too stringent of firewalls to successfully
be reached directly over the network by push or pull.

git bundle create catchupsusan.bundle HEAD~8..HEAD
git bundle create catchupsusan.bundle --since=10.daysmaster

These diffs can be treated just like any other remote, even though are a local file on disk. The contents of the bundle can be
inspected with Is-remote and the contents pulled into the local repository with fetch. Many Git users add a file extension of
.bundle as a matter of convention.

git ls-remote catchupsusan.bundle
git fetch catchupsusan.bundle