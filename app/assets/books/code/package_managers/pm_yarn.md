# YARN

# A new package manager for JavaScript
# Faster (from minutes to seconds), reliable, and secure alternative npm client.
# By engineers from Facebook , Exponent, Google, and Tilde
https://github.com/yarnpkg/yarn

# Yarn is not a replacement for the npm package registry. It is not a competing package library ecosystem. 
# This is not a repeat of the Bower fiasco.
# It’s a client that works with the npm package registry.

. Faster installs.
. Deterministic dependencies — with yarn.lock, you’ll get the same versions of the same packages installed in the same directory structure every time.

> npm install -g yarn
npm install 				→ yarn
npm install --save <name> 	→ yarn add <name>

yarn init
yarn add <packagename> 						Add a dependency
yarn add --dev <packagename> 				Add a dev dependency
yarn remove <packagename>  					Remove a dependency
yarn (install is the default behavior) 		Install
yarn <command> 	yarn start, yarn test


global install path: %LOCALAPPDATA%/Yarn/config/global


# To fix npm client issues
npm installs dependencies into the node_modules directory non-deterministically. This means that based on the order dependencies are installed, the structure of a node_modules directory could be different from one person to another. 

# Yarn uses 
* lockfiles (lock the installed dependencies to a specific version)
# Don’t .gitignore yarn.lock. It is there to ensure deterministic dependency resolution to avoid “works on my machine” bugs.
* an install algorithm (parallelize operations) that is deterministic and reliable
* a mutex to ensure that multiple running CLI instances don't collide and pollute each other
# Therefore every install results in the exact same file structure in node_modules across all machines.

# The install process is broken down into three steps:

• RESOLUTION
    Yarn starts resolving dependencies by making requests to the registry and recursively looking up each dependency.
• FETCHING
    Next, Yarn looks in a global cache directory to see if the package needed has already been downloaded. If it hasn't, Yarn fetches the tarball for the package and places it in the global cache so it can work offline and won't need to download dependencies more than once. Dependencies can also be placed in source control as tarballs for full offline installs.
• LINKING
    Finally, Yarn links everything together by copying all the files needed from the global cache into the local node_modules directory.



# With Yarn, engineers still have access to the npm registry, but can install packages more quickly and manage dependencies consistently across machines or in secure offline environments. Yarn enables engineers to move faster and with confidence when using shared code so they can focus on what matters — building new products and features.

 JavaScript community, engineers share hundreds of thousands of pieces of code so we can avoid rewriting basic components, libraries, or frameworks of our own. Each piece of code may in turn depend on other pieces of code, and these dependencies are managed by package managers. The most popular JavaScript package manager is the npm client, which provides access to more than 300,000 packages in the npm registry. More than 5 million engineers use the npm registry, which sees up to 5 billion downloads every month.

 Many of our projects at Facebook, like React, depend on code in the npm registry. However, as we scaled internally, we faced problems with consistency when installing dependencies across different machines and users, the amount of time it took to pull dependencies in, and had some security concerns with the way the npm client executes code from some of those dependencies automatically. We attempted to build solutions around these issues, but they often raised new issues themselves


# The primary function of any package manager is to install some package — a piece of code that serves a particular purpose — from a global registry into an engineer's local environment. Each package may or may not depend on other packages. A typical project could have tens, hundreds, or even thousands of packages within its tree of dependencies.

# These dependencies are versioned and installed based on semantic versioning (semver).


https://medium.com/javascript-scene/faster-more-reliable-ci-builds-with-yarn-7dbc0ef31580#.49g8sffz3

# Yarn Commands

    yarn help <command>
    https://yarnpkg.com/en/docs/cli/

    - access
    - add
    - bin
    - cache
    - check
    - clean
    - config
    - generate-lock-entry
    - global
    - info
    - init
    - install
    - licenses
    - link
    - list
    - login
    - logout
    - outdated
    - owner
    - pack
    - publish
    - remove
    - run
    - tag
    - team
    - unlink
    - upgrade
    - upgrade-interactive
    - version
    - versions
    - why


  Usage: yarn [command] [flags]

   Options:

    -h, --help                      output usage information
    -V, --version                   output the version number
    --verbose                       output verbose messages on internal operations
    --offline                       trigger an error if any required dependencies are not available in local cache
    --prefer-offline                use network only if dependencies are not available in local cache
    --strict-semver
    --json
    --ignore-scripts                don't run lifecycle scripts
    --har                           save HAR output of network traffic
    --ignore-platform               ignore platform checks
    --ignore-engines                ignore engines check
    --ignore-optional               ignore optional dependencies
    --force                         ignore all caches
    --no-bin-links                  don't generate bin links when setting up packages
    --flat                          only allow one version of a package
    --prod, --production [prod]
    --no-lockfile                   don't read or generate a lockfile
    --pure-lockfile                 don't generate a lockfile
    --frozen-lockfile               don't generate a lockfile and fail if an update is needed
    --global-folder <path>
    --modules-folder <path>         rather than installing modules into the node_modules folder relative to the cwd, output them here
    --cache-folder <path>           specify a custom folder to store the yarn cache
    --mutex <type>[:specifier]      use a mutex to ensure only one yarn instance is executing
    --no-emoji                      disable emoji in output
    --proxy <host>
    --https-proxy <host>
    --no-progress                   disable progress bar
    --network-concurrency <number>  maximum number of concurrent network requests








