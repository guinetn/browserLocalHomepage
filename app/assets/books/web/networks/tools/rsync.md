### RSync
https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories
“remote sync”, is a remote and local file synchronization tool. included on most Linux distributions by default.
    
rsync -a source destination
rsync -a dir1/ dir2 
rsync	Secure copy file.txt to remote host /tmp folder
rsync	
rsync -a /home/apps /backup/	Synchronize source to destination

rsync -a ~/dir1 username@remote_host:destination_directory
rsync -a username@remote_host:/home/username/dir1 place_to_sync_on_local_machine