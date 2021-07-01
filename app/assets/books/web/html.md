# HTML


## Recommended Minimum

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!--
  The above 2 meta tags *must* come first in the <head>
  to consistently ensure proper document rendering.
  Any other head element should come *after* these tags.
 -->
<title>Page Title</title>
```

meta charset - defines the encoding of the website, utf-8 is the standard

meta name=”viewport” - viewport settings related to mobile responsiveness

width=device-width means that it will use the physical width of the device (instead of zooming out) which is good with mobile friendly pages

initial-scale=1 is the initial zoom, 1 means no zoom

## <head>
meta, link, title, style, script, noscript, base

information for how a document should be perceived, and rendered, by web technologies. e.g. browsers, search engines, bots, etc.

```html
<!--
  Set the character encoding for this document, so that
  all characters within the UTF-8 space (such as emoji)
  are rendered correctly.
-->
<meta charset="utf-8">

<!-- Set the document's title -->
<title>Page Title</title>

<!-- Set the base URL for all relative URLs within the document -->
<base href="https://example.com/page.html">

<!-- Link to an external CSS file -->
<link rel="stylesheet" href="styles.css">

<!-- Used for adding in-document CSS -->
<style>
  /* ... */
</style>

<!-- JavaScript & No-JavaScript tags -->
<script src="script.js"></script>
<script>
  // function(s) go here
</script>
<noscript>
  <!-- No JS alternative -->
</noscript>
```

download(web/emmet.md)

## more
- https://htmlhead.dev
- https://www.w3schools.com/howto/howto_css_pricing_table.asp
- [front-end template: html5-boilerplate](https://github.com/h5bp/html5-boilerplate)
- https://htmlreference.io/