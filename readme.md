# Brain cache

![](assets/img/bka.png)  
Never open you're .md notes again, it's automatic and as fast as your fingers can move.  

![screenshoot](assets/img/bka_sreenshoot_01.png)

# Features
* Blog
* You're notes in views+slides   
* Navigate in views   
* Navigate in view's slides 
* Set alarms
* Customize & enrich: add views, topics, links, slides to views, slideshow
* Automatic repeat copy when mousedown > 3sec

|Key|Action|  
|---|---|  
|<kbd>CTRL</kbd><kbd>→</kbd> or <kbd>+</kbd><br/><kbd>CTRL</kbd><kbd>←</kbd> or <kbd>-</kbd>  | Navigate in views|   
|<kbd>a…z</kbd> key | Go to view with a name starting by…|  
|<kbd>→</kbd> | Start slides navigation for current view|  
|<kbd>←</kbd> <kbd>→</kbd> | Navigate in slides of the current view|   
|<kbd>SHIFT</kbd><br>or <kbd>←</kbd> on 1st slide | Exit slide navigation<br>Slide page is memorized: come back to it with <kbd>→</kbd> |  
|<kbd>F</kbd> key | Fullscreen mode|  
|<kbd>ESC</kbd> key | Exit Fullscreen mode|  

# Configuration

![configuration](assets/img/bka_config.png)

### Use from server side
1. Clone-it on github  
2. Activate the github page  
2. Link it to your browser's homepage  (or as a bookmark)
>chrome::settings  
>└──Appearance  
>└────Welcome button  
>└─────Set this repo as you're browser homepage

### Use locally
1. Clone-it locally then starts a server…
2. npm i -g serve
3. cd <...repo...>
4. serve
5. http://localhost:5000

# Customize

Refer to bka_config.png for a global view of the process.

## Adding a blog item

* Just create a .md file in /blog folder!
* Blogs are requested with the github api. You won't show local changes. Publish!
* Publish on github to view the blog's files (local server isn't the githup file api!)
## Adding a view

* View contains topics (grouped links) or custom html  
* Views are defined inside &lt;div id="main"&gt; in index.html
* Each view can have a markdown file (.md) in assets/slides

***Empty view***     
```html
 <div id="Name_Of_My_View" class="view">  ← Change 'Name_Of_My_View'
    <h1>Title_Of_My_View</h1>             ← Change (or remove the h1) 'Title_Of_My_View'
    <div class="topics">                   
       ...add topics here     
    </div>
    ...add any other html content here
</div>
```
***Add topics***   

```json
Topics are defined in assets/topics.json

…
"news": [		
		"https://www.nytimes.com",
		"https://www.washingtonpost.com"		
        ], 
…
```
***Connect topic to view***
```html
 index.html

 <div id="Name_Of_My_View" class="view">
    <h1>Title_Of_My_View</h1>           
    <div class="topics">   
       <div id="news"></div>   ← This is how to inject the topic 'news' in a view. In the topic title, char _ will be replaced by a space  
    </div>                        Ex: "Productivity_Tools" → "Productivity Tools"   
</div>

an unique option: 
 
    <div class="topics">   
       <div id="news" data-info='-t'></div>   ← '-t' will remove the topic's title (it display the links 'inline', you won't see the 'News' in aqua color below)
    </div>    
```
***Result***  
![view+topic](assets/img/bka_view-topic.png)      

> You can change colors in ```css/index.css```

***Topics options***  
* Replace links by a friendly name
* Add icons from [fontawesome](https://fontawesome.com/icons?d=gallery) with 'fa… fa-…'

```json
"news": [		
		"https://www.nytimes.com",                             ← Display "https://www.nytimes.com"  
		"https://www.nytimes.com(THE NY TIMES)",               ← Display "THE NY TIMES"
        "https://www.nytimes.com[fas fa-newspaper]",         ← Display an icon
        "https://www.nytimes.com[inline fab fa-newspaper]",  ← To have icon inline (no rows)
        "https://www.washingtonpost.com"	

      GET DATA FROM API
                                      ____ !getjson60  Fetch json data every 60 sec (in sec)
                                     /____ !getjson    Fetch json data a single time
                                    / 
                                   /         _____ Topic Text to render is between ()
                                  /         /                                             
      "https://httpbin.org/ip[!getjson](my ip: $origin)",
                                               \
                                                \____ Variable to search for in the json object 
                                                      Must be $ prefixed
                                                      Recursive search trough the json object
      samples:
		"http://ip-api.com/json/[!getjson =lat =lon](my lat/lon: $lat $lon)",
		"https://api.wheretheiss.at/v1/satellites/25544[!getjson3600 =latitude =longitude](iss: $latitudeN $longitude)"
        ], 
…	
```
## Adding slides to a view...takes 10 sec

1. In ```assets/slides``` folder
- Create a folder having the same name that the targeted view 
- Create a file named _xxxx.md file having the same name that the targeted view but starting with a _
2. Write some markdown

* Each view can have a markdown file (.md) 
* This .md file is converted in html on the fly when you press <kbd>→</kbd>     
* The sequence '::::' is the slide separator (any number of ':' superior to 3). Slides are not limited in size.  
* Slides can contains youtube video (and kind of by extension)
* Slides can have nested slides

```md
home.md

Slide 1.
# My Awesome Slide #1

lorem.........  
  
How to add an image with the right path to:
![](assets/img/cloud.png)

::::
Slide 2.

### Add a video
<iframe src="//www.youtube.com/embed/I0eVwo1VCuU?rel=0" frameborder="0" allowfullscreen></iframe>
[video_title]<span>(https://www.</span><span>youtube.com/watch?xyzabc)</span>

### Add a markdown file   
<span>download</span>.md(assets/slides/code.md)
download.md(assets/slides/code.md)

### Add html data: will be integrated as 'innerHTML' (interpreted html)   
<span>download</span>.html(https://httpbin.org/ip)
download.html(https://httpbin.org/ip)

### Add raw data: will be integrated as 'innerText' (NOT interpreted html/text)   
<span>download</span>.raw(https://httpbin.org/ip)
download.raw(https://httpbin.org/ip)

### Execute a javascript code file: will be run with eval()
Can interact normally with DOM elements in the .md file
- <span>download</span>.exec(https://...myfile.js)  
download.exec(https://...myfile.js)  

### Add a code file (will be prettyfied, not interpreted)

- <span>download</span>.code(https://...myfile.js)  
- <span>download</span>.code(https://...myfile.cpp)  
- <span>download</span>.code(https://...myfile.html)  

**Tips**
Github's original links need to be changed, ie:

❌ <span>download</span>.code(https://github.com/pms67/PID/blob/master/PID.h)  
✔️ <span>download</span>.code(https://raw.githubusercontent.com/pms67/PID/master/PID.h)
  
https://<mark>github.com</mark>/pms67/PID/<mark>blob</mark>/master/PID.h
Must be changed to
https://<mark>raw.githubusercontent.com</mark>/pms67/PID/master/PID.h

download.code(https://raw.githubusercontent.com/pms67/PID/master/PID.h)  

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

::::     ← Slides separator

Slides are not limited in size.

## My better Slide #2
**"abcdef"** is a tool to create a simple and beautiful slide
…
::::
…

```

### SLIDES SYNTAX

Standard markdown + additional syntax to include…
    
* <strong>download.md</strong>(assets/slides/myfile.md) : a markdown file (html rendered)
* <strong>download.raw</strong>(https://<span>githubusercontent.com/abcdef/sourcefile.txt</span>) : a file as it is (raw, not transformed)
* <strong>download.html</strong>(https://<span>githubusercontent.com/abcdef/sourcefile.txt</span>) : an html file (interpreted in innerHTML)
* <strong>download.code</strong>(https://<span>githubusercontent.com/abcdef.cpp</span>) : a code file (prettified by its extension)
* <strong>download.iframe(url,[w,h])</strong> : an iframe + width/height in px
* <strong>download.iframe</strong>(assets/slides/web/front/react_samples/react01/index.html)
* <strong>download.iframe</strong>(assets/slides/web/front/react_samples/react01/index.html,500,200)
* <strong>[video_title]<span>(https://www.</span><span>youtube.com/watch?xyzabc)</span></strong> : a youtube video: any link containing 'youtube' 
* Horizontal Slide Show: a slideShowContainer that contains slideShowSlide items
```html
<div class="slideShowContainer">   
   <div class="slideShowSlide">  
      ...  content #1
   </div>  
   <div class="slideShowSlide">  
      ...  content #2
   </div>  
</div>  
```



# Alarms

* Audio (speaker)
* Visual message

![](assets/img/bka_alarms.png)

* Click the clock  
* Optionally enter a text in relation to the alarm  
* Click a duration  
* To close the alarm selection, click the clock again or somewhere in the red square  
* A progressbar is displayed below the clock  
* Now, wait for the speaker and the snackbar!

***Cancelling an alarm***  
* Click the clock  
* Click the duration with a yellow background 

# Development

>> git clone https://github.com/guinetn/braincache.git   
>cd braincache  
>Start a server:  
>* serve (npm i -g serve)   
>* or live-server from vs code…  

## Markdown parser
> [ShowdownJs](https://github.com/showdownjs/showdown)  
> [Markdown syntax](https://github.com/showdownjs/showdown/wiki)
> [Emoji supported, ex: ```:dog:```](https://github.com/showdownjs/showdown/wiki/emojis)
## Code prettyfier
* [Google code-prettify (Powers https://code.google.com/ and http://stackoverflow.com/)](https://github.com/googlearchive/code-prettify)  
* [skin Gallery is here. ](https://raw.githack.com/google/code-prettify/master/styles/index.html) Inject skin name in index.html → at the end of 
```<script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js?autoload=true&amp;skin=sunburst" defer></script>```
* https://jmblog.github.io/color-themes-for-google-code-prettify/

# License
Released under the [MIT License][http://www.opensource.org/licenses/MIT]