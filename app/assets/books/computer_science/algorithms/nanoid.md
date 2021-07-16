## NANOID

using NanoID over UUID for any future projects considering its small size, URL friendliness, security, and speed
https://www.npmjs.com/package/nanoid

Small. 108 bytes (minified and gzipped). No dependencies. Size Limit controls the size.
Fast. It is 60% faster than UUID.
Safe. It uses cryptographically strong random APIs. Can be used in clusters.
Compact. It uses a larger alphabet than UUID (A-Za-z0-9_-). So ID size was reduced from 36 to 21 symbols.
Portable. Nano ID was ported to 14 programming languages.

>npm i nanoid

```js
import { nanoid } from 'nanoid';
model.id = nanoid();   // => "V1StGXR8_Z5jdHi6B-myT"
```