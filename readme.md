# Browser Local Homepage

A custom homepage for use locally in your browser as a tool   
Include many pages having links, tools (B64, Timestamp)  

![screenshoot](screenshoot01.png)

### Navigation 
- [+] [-]  
- First letter of the name of the page you want to navigate to [h]omepage [w]eb [c]ode…  

# Configuration

Add your own pages, links...

### pages

* Pages are defined in index.html

* Basic
>&lt;div id="web" class="view"&gt;  
>add content here   
>&lt;/div&gt;  

* Related to links in links.json  
>&lt;div id="&lt;my_topic&gt;" class="view"&gt;  
>&lt;h1&gt;a name for my topic&lt;/h1&gt;   
>
>  &lt;div class="container"&gt;  
>    &lt;div id="vlinks_xxx1" class="containerItem"&gt;&lt;/div&gt;  <mark>vlinks_xxx or hlinks_xxx are defined in links.json</mark>  
>    &lt;div id="vlinks_xxx2" class="containerItem"&gt;&lt;/div&gt;  
>    &lt;div id="links_xxxx" class="containerItem"&gt;&lt;/div&gt;         
>  &lt;/div&gt;  
>  
>&lt;/div&gt;  

>links.json  
* vlinks_&lt;my_topic&gt;  for vertical links list  
* links_&lt;my_topic&gt;   for horizontal links list  

* Then links_<my_topic> is placed as a placeholder in index.html  
>	"vlinks_help": [  
>		{ "name": "gitter", "ref": "https://gitter.im" },  
>		{ "name": "quora", "ref": "https://www.quora.com" },  
>		{ "name": "stackoverflow", "ref":"https://stackoverflow.com" }  
>		],	

# Development

>cd <my_folder>  
>serve   	(npm i -g serve)  
>or live-server from vs code…  

# How to use

Host it for free as a github page  

>chrome::settings  
>Appearance  
>Welcome button  
>Set your repo <cite><you>.github.io/browserLocalHomepage</cite> as you're browser homepage






