# Content Security Policy - CSP

add an additional layer of protection to your web application on almost all current browsers. Technique for decreasing the threat of cross-site scripting attacks.

a security standard that adds an extra layer of defense in detecting and mitigating certain kinds of attacks, such as Cross-Site Scripting (XSS), clickjacking, and other code injection threats. CSP is a preventative step against attacks that rely on executing malicious material in a trusted web context, as well as other attempts to bypass the same-origin policy

Threats CSP Can Mitigate?
1. Mitigating cross-site scripting

reduce the XSS attack using the CSP by defining trusted source sites for the executable scripts. When we use the CSP header, browsers only allow us to run the script from the whitelisted domains and ignore all other scripts.


<meta http-equiv="Content-Security-Policy" content="default-src 'self'">
<meta http-equiv="Content-Security-Policy" content="default-src 'self' *.loginradius.com">
 <meta http-equiv="Content-Security-Policy" content="default-src https:; script-src https: 'unsafe-inline'; style-src https: 'unsafe-inline'">
 <meta http-equiv="Content-Security-Policy" content="default-src 'self' img-src *; script-src cdn.loginradius.com;">