# Cookies

A way to store information about your browser session and persist that data over a period of time. Before cookies were created, websites had no idea who you were from one page view to the next. 
LocalStorage and sessionStorage provide a much nicer way to store data locally but cookies still have their place

- Cookies
- Cross-Site Request Forgery Tokens (CSRF)
- Password reset tokens

## Set a cookie in the browser

// Set a cookie named sandwich, with a value of turkey
document.cookie = 'sandwich=turkey;';
{KEY}={STRING_VALUE};

|||
|---|---|
| path={path}         | Path to set the cookie at (current path is default). Good: the root path: path=/ |
|domain={domain}      | Domain for the cookie. Defaults to the current host name |
|max-age={maxage_sec} | The maximum amount of time to keep the cookie, in seconds |
|expires={date_GMT }  | A date on which to expire the cookie |
|secure               | The cookie can only be transmitted over HTTPS |
|same-site={lax|strict|none} | Whether or not the browser can send the cookie to other sites |
|                            | default: lax, only sends with same-site requests and navigation GET requests |
|                            | strict: does not send to any external sites, even when following a link |
|                            | none: does not place any restrictions |


To avoid cookies to remain in the browser indefinitely, define either `max-age` or `expires`
```js
// expires in two weeks: 60 seconds x 60 minutes x 24 hours x 14 days
document.cookie = `snack=chips; path=/; max-age=${60 * 60 * 24 * 14};`;
```

## Get a cookie value
All of the cookies for a site are stored as a single string, which makes getting the value of one of them a bit tedious.

```js
// logs a single string with all of the cookies for a site
console.log(document.cookie);
```

Helper method: 
```js
/**
 * Get the value of a cookie
 * Source: https://gist.github.com/wpsmith/6cf23551dd140fb72ae7
 * @param  {String} name  The name of the cookie
 * @return {String}       The cookie value
 */
function getCookie (name) {
	let value = `; ${document.cookie}`;
	let parts = value.split(`; ${name}=`);
	if (parts.length === 2) return parts.pop().split(';').shift();
}

Ex:
let sandwich = getCookie('sandwich');
let snack = getCookie('snack');
```

## Deleting Cookies
Set `max-age` to 0
Set `expires` date to the current time or sooner

Path must matches the one used to set the cookie, or it will not work:
```js
// Delete the cookie
document.cookie = `sandwich=turkey; path=/; max-age=0;`;
```

## Cookie storage limits

Browsers provide differing levels of storage space for cookies, but the general upper limit is 4093 bytes (just over 4kb).

For browsers with a maximum storage limit, this amount is a total for all cookies on your site. Accordingly, you should try to reduce the overall footprint of your data as much as possible.

## Security

Browsers automatically send cookies with subsequent requests, which is how the web achieves the smooth sign-in experience for users.

download.page(security/attack_csrf.md)