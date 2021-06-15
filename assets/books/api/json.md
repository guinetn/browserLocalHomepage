# JSON

[JSON modules landed in Chrome](https://2ality.com/2021/01/import-assertions.html)

```js
import config from './data/config.json' assert { type: 'json' };
```
A core architectural principle of the web is to never use the filename extension to determine what’s inside a file. Instead, content types are used.
JavaScript engine can’t use the filename extension to determine that this is JSON data