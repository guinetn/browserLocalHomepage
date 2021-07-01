import fileinput
import os

# lines of the file f1 containing an item of the titles array are capitalized and marked as markdown title (# xxxx)
# result is saved in fOut
error : set files to run this
titles=['Introduction to Node.js','A brief history of Node.js','How to install Node.js','How much JavaScript do you need to know to use Node?','Differences between Node and the Browser','The V8 JavaScript Engine','How to exit from a Node.js program','How to read environment variables from Node.js','Where to host a Node.js app','How to use the Node.js REPL','Node, accept arguments from the command line','Accept input from the command line in Node','Expose functionality from a Node file using exports','Introduction to npm','Where does npm install the packages?','How to use or execute a package installed using npm','The package.json guide','The package-lock.json file','Find the installed version of an npm package','Install an older version of an npm package','Update all the Node dependencies to their latest version','Semantic Versioning using npm','Uninstalling npm packages','npm global or local packages','npm dependencies and devDependencies','The npx Node Package Runner','The Event Loop','Understanding process.nextTick()','Understanding setImmediate()','Timers','Asynchronous Programming and Callbacks','Promises','Async and Await','The Node Event emitter','How HTTP requests work','The HTTP protocol','Build an HTTP Server','Making HTTP requests with Node','HTTP requests in Node using Axios','Using WebSockets in Node.js','Working with file descriptors in Node','Node file stats','Node File Paths','Reading files with Node','Writing files with Node','Working with folders in Node','The Node fs module','The Node path module','The Node os module','The Node events module','The Node http module','Node.js Streams','The basics of working with MySQL and Node','The difference between development and production']
fIn = r'N:\md\md\Web_ClientServer_Servers_NodeJs - Handbook.md'
fOut = r'N:\md\md\Web_ClientServer_Servers_NodeJs - Handbook2.md'

fOut = open(fOut, 'w')
print(os.path.getmtime(fIn))
with fileinput.input(fIn) as f:    # line starting with '>' causes  'charmap' codec can't decode byte 0x90 in position 2907500:
    for line in f:
        line2 = line.replace('\n','')
        for t in titles:                
            if line2 == t:
                fOut.write('\r\n# ' + line.capitalize() + '\r\n')
                break        
        if line2 != t:        
            fOut.write(line)
fOut.close()