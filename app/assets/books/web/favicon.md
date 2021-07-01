# Favicon

Currently, frontend developers have to deal with 20+ static PNG files just to display a tiny website logo in a browser tab or on a touchscreen.

* Need = 5 icons + JSON file

<link rel="icon" href="/favicon.ico"><!-- 32×32 -->
<link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png"><!-- 180×180 -->
<link rel="manifest" href="/manifest.webmanifest">

// manifest.webmanifest
{
  "icons": [
    { "src": "/192.png", "type": "image/png", "sizes": "192x192" },
    { "src": "/512.png", "type": "image/png", "sizes": "512x512" }
  ]
}


 Inkscape → icon.svg 