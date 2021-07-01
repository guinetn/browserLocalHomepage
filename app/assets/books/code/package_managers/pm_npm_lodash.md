# Npm lodash

https://lodash.com/
https://lodash.com/docs/4.17.4

# Lodash is a toolkit of Javascript functions that provides clean, performant methods for manipulating objects and collections.

# Lodash makes JavaScript easier by taking the hassle out of working with arrays, numbers, objects, strings, etc.
• Iterating arrays, objects, & strings
• Manipulating & testing values
• Creating composite functions


npm install lodash --save
const _ = require('lodash');

...
resolve: function(post) {
    return _.find(Authors, a => a.id == post.author_id);
}



