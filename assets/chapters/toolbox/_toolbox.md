# BKA markdown samples

**"BKA"** allow to display markdown chapters.

* Simple
* Beautiful
* Easy
* Emojis :+1: :dog: Details: https://github.com/showdownjs/showdown/wiki/emojis

# Arrays
Key      | Value                  | Default
---|---|---
slide    | directory name         | sample
progress | show progress bar      | false
limit    | progress limit minutes | 5
time     | progress start minutes | 0
 
# Images
![](app/img/cloud.png)

# Code snippets

```js
// Javascript snippet
var a = 1;
const pi = 3.14;
```

```css
#css {
  background-image: url(background-image.jpg);
  background-size: cover;
  color: darkred;
}
```

# Horizontal Slide Show
a `slideShowContainer` that contains `slideShowSlide` items

```html
<div class="slideShowContainer">   
   <div class="slideShowSlide">  
      ...  
      content #1
      ...        
   </div>  
   <div class="slideShowSlide">  
      ...  
      content #2
      ...        
   </div>  
</div>  
```

<div class="slideShowContainer">   
<div class="slideShowSlide">  
  ...  content #1
</div>  
<div class="slideShowSlide">  
  ...  content #2
</div>  
</div>  

# You tube extension
[The Map of Physics](https://www.youtube.com/watch?v=ZihywtixUYo)
[Natural Language Processing With RNNs  H - TensorFlow 2.0 Course](https://www.youtube.com/watch?v=hEUiK7j9UI8&t=6s)

# Iframe
&lt;iframe src="//www.youtube.com/embed/I0eVwo1VCuU?rel=0" frameborder="0" allowfullscreen&gt;&lt;/iframe&gt;
<iframe src="//www.youtube.com/embed/I0eVwo1VCuU?rel=0" frameborder="0" allowfullscreen></iframe>

# Downloading files...

## Render file as raw text or call api
My ip from https://httpbin.org/ip: <span>download</span>.raw(https://httpbin.org/ip)
My ip from https://httpbin.org/ip: download.raw(https://httpbin.org/ip)

## Render others markdown files
<span>download</span>.md(assets/chapters/toolbox/toolbox_subpage_1.md)
download.md(assets/chapters/toolbox/toolbox_subpage_1.md)

Use `download.chapter` to get ride of `assets/chapters/`
<span>download</span>.chapter(toolbox/toolbox_subpage_1.md)
download.chapter(toolbox/toolbox_subpage_1.md)

## Execute a javascript code file: will be run with eval()
Can interact normally with DOM elements in the .md file
- <span>download</span>.exec(https://...myfile.js)  
download.exec(https://...myfile.js)  

## Render file as code snippet (file extension is checked)

**Tips**  
Github's links need to be changed, ie:

https://<mark>github.com</mark>/pms67/PID/<mark>blob</mark>/master/PID.h
Must be changed to
https://<mark>raw.githubusercontent.com</mark>/pms67/PID/master/PID.h

❌ <span>download</span>.code(https://github.com/pms67/PID/blob/master/PID.h)  
✔️ <span>download</span>.code(https://raw.githubusercontent.com/pms67/PID/master/PID.h)
  
download.code(https://raw.githubusercontent.com/pms67/PID/master/PID.h)  

