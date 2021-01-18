# CSS

## MASTER CSS

### APPLYING CSS

IN-LINE
```css
<p style="color: red">text</p>
```
EMBEDDED
```css
<head>
    <style>p { color: red; }
    </style>

    <link rel="stylesheet" href="style.css">
```
SCOPED (style in &lt;body&gt;)
```css
<body>
    <div id="scoped-content">
    <style type="text/css" scoped>
        h1 { color: red; } 
    </style>
```
IMPORTING
```css
@import url(morestyles.css);	
    Another stylesheet onto your existing one.
    Must be placed at the top of a stylesheet, before any other rules

@import "mystyle.css";
@import url("mystyle.css");
```

### TYPE OF ELEMENTS 
* BLOCK 
>boxes are laid out one after the other vertically.
>Generate a line break before and after the content
>Occupies entire space of its parent element (container): stretch the full width
>Centering: { margin: 0 auto; }
><pre>Elements:
address article aside audio blockquote canvas dd
div dl fieldset figcaption figure figcaption footer form
h1, h2, h3, h4, h5, h6  header hgroup hr noscript ol
output p pre section table tfoot ul video
</pre>

* INLINE
>  laid out horizontally, one after the other, beginning at the top of a containing block.
> To have elements on the same horizontal line without floating them
> OCCUPIES JUST THE NEEDED PLACE (Only take up the space of the content inside)
> Width and height properties HAVE NO EFFECT.
> Margin and padding properties only have an effect horizontally.
> Wrap onto the next line when they run out of space in their container
> Centering: text-align:center;
><pre>Elements: b big i small tt abbr acronym cite code dfn em kbd strong samp var
a bdo br img map object q script span sub sup button input label select textarea
</pre>

* INLINE-BLOCK 
> Make elements inline but preserving their block capabilities (tipically a div without width)
> Used to give an inline element a width
><pre>Elements: button textarea input
>
> Use case:
>
> li {
> display: inline-block;
> }
> ul {  
> padding: 1em;    
> width: fit-content;  
> margin: 1em auto; /* move the container to the center on the X-axis */
> }
</pre>

### POSITIONING ELEMENTS

position: static | relative | fixed | absolute | inherit

* static (default)
>Renders a box in the normal HTML flow (block element take all the row, inline element on same line )
>Ignore: left,top,right,bottom,z-index

* relative
>element is positioned relative to its normal position
>= STATIC + OFFSET the box from its original position
>Alone, it does nothing (no visual change = static), useful for its children that will be relative to it now.
>Offset relative to itself
>Can be offset with top, right, bottom and left. 
>!! NORMALY WE DON'T USE TLRB with relative element cause it goes outside normal flow and it will >be difficult to style things around it
>WE USE IT WHEN A CHILD NEED A REFERENCE FOR "ABSOLUTE" POSITIONING  
>    Creates relative-type positioning context for children.
>    * Leaves behind it a "ghost" element in the same place in the document flow as when it had the >"static" position
>    * This cause the other elements to take it into account in their positioning just as in the >"static"
>    * Then the visible element is moved based on the values of top, right, bottom, and left.   

* absolute
> TO USE ABSOLUTE: MUST HAVE A PARENT 'relative or absolute or fixed or sticky'
>                                      window is the default 'absolute' parent 
> Element is taken out of the document flow: It no longer adheres to its natural position in the DOM. 
> the page doesn’t reserve any space for it
> positioning it to it’s nearest positioned element (if there is one) or the document root if nothing else.
> absolute is positioned absolutely INSIDE ITS POSITIONED PARENT ELEMENT (the window if it is the direct parent)
> Relative but removed from the normal document flow so all others elements ignore it           
> Element pulled out of HTML content flow and leaves no space behind. Manual positioning.  
>       Element is positioned RELATIVE TO ITS NEAREST PARENT HAVING A 'RELATIVE' TYPE POSITIONING. (inside a parent they can reference)
>       	 huge cause of unexpected behavior in CSS for many developers: absolute will look for an ancestor with its own position set
>     Can be offset with top, right, bottom and left.
>     Offset relative to its nearest relative-type positioned parent.
>     Creates relative-type positioning context for children.

* fixed
>Element is positioned related to the browser window
>Affixes the element, scrolling will not affect its position on the screen. element is positioned relative to the viewport (browser window)
>Can be offset with top, right, bottom and left.
>Offset relative to the viewport.
>Creates relative-type positioning context for children.
>Even if the user scrolls vertically/horizontally/resize the browswer window, element remains fixed at the same position inside the browser window. 

* Sticky
>to stick an element that’s initially farther down the page to the top of the screen.
>Elements will initially behave like position: relative elements, but if you keep scrolling, 
> They will get taken out of the normal flow and behave like "position: fixed" wherever you have positioned them.
>.another {position: sticky; top: 0px; }
### SELECTORS

* SPECIFICITY
Style priority is determined by position in site<br>
More Specific = Greater Precedence

    1. Find all declarations for the target media type
    2. Sort according to importance (normal or important) and origin (author, user, or user agent)
        1. user agent styles declarations (will be overwritten by next styles)     |
        2. user normal Declarations 											   |    increasing
        3. author normal declarations 											   |     priority         				!important RULES
        4. author !important declarations 										   |                  an "!important" declaration takes precedence over a normal declaration
        5. user !important declarations 										   |                  user "!important" rules override author "!important" rules
																				   ↓		 				→ this improves accessibility of documents by giving users with special requirements

* CSS-PREFIXES

```css
a:link {
    -webkit-transition: .2s;	chrome / Safari
    -moz-transition: .2s;		firefox
    -o-transition: .2s;			opera
    transition: .2s;            css standard
}
```

|SELECTORS||selector {  property: value; }|
|--|--|--|
|<strong>GROUPING SELECTORS</strong>|||
|,||h2, .thisOtherClass, .yetAnotherClass { color: red; }|
|<strong>CLEVER SELECTORS</strong>|||
| * |* {…}|Target everything|
|||* {  margin: 0;  padding: 0; }|
| > |A>B|Immediate Descendant=child (level 1 childs)|
|||Selects all immediate children of a specific parent<br>table>tbody>td:nth-child(2){font-weight: bolder;}|
| space |A  B| All descendants (level N childs)|
|||nested selectors<br>div span {...}  Target any &lt;span&gt; in a &lt;div&gt;|
|+|A+B|Sibling level 1 (brother)|
|||div + p {...} 	First paragraph|
|A ~ B||Sibling level N|
|||All nodes having a common predecessor (not parent)<br>input:focus ~ label → every "label" AFTER an input|
|<strong>ATTRIBUTE SELECTORS</strong>||Markup[attr...something]<br>[attr...something]|
||tag[attr]|Tag has this attribute|
|||a[href] {background-color: yellow; font-color: blue}|
||[attr]|Attribute exists|
|||[autoplay] target all elements having autoplay attribut set (with any value)|
||[attr=valeur]|Attribute has this exact value|
|||a[href="https://css-tricks.com"] {…}<br>input[type=text] { width: 200px; } <br>input[type=text][disabled] { border: 1px solid #ccc }|
||[attr\|=valeur]|Attribute value starts with this in a dash-separated list|
|||a[href\|="http://"] {background-color: green; font-color: yellow}<br>a[href|="http://google.com"] { color: red; }|
||[attr~=valeur]|Attribute has this value in a space-separated list somewhere |
||[attr^=valeur]| Attribute value starts with this<br>|							
|||a[href^=http] { padding-right: 10px; background: url(arrow.png) right no-repeat; }	Style external links|
||[attr$=valeur]|Attribute value ends with this|
|||a[href$=".zip"]:before { color: red; content: url('img/zip.jpg')}|
||[attr*=valeur]|Attribute value contains this value somewhere in it|
|||a[href*=@google] {... } Target all google emails|							
|PSEUDO-CLASSES||Select element by its state|							
|||selector:pseudo_class { property: value; }|
|DYNAMIC|||										
||:link||										   
||:visited||										
||:active ||										
||:hover  ||										
||:focus  ||										
||:target  ||										
||:checked ||	
||:focuswithin  |div:focus-within {...}: any div when any of its descendants gets the focus|										
||:invalid||
|STRUCTURED|||										
|| :first-child		 | Apply if IT IS the first child of its parent |
|| :last-child		 |li:last-child { border-bottom: 0; }|
|| :first-of-type()	 ||
|| :nth-of-type()	 ||
|| :nth-child(an+b)	 |li:nth-child(2n)   { even } <br>li:nth-child(2n+1) { Odd }|
|||Zebra Striped Table Rows:<br>tbody tr:nth-child(odd) {background-color: #ddd;}|
|| :only-child() 	 ||
|| :nth-last-child()  ||
|| :nth-last-of-type()||
|| :only-of-type()	 ||
|| :last-of-type ||
|STATES|||										
|| :enabled 	any enabled (active) element 	input:enabled {color: red}||
|| :disabled 	any disabled element||
|| :checked 	target selected checkbox||
|| :default 	target default selected elements (list, checkboxes)||
|| :valid		target valid elements ||
|| :in-range	target element where value is in the range (for min/max elements)||
|| :required	target required elements||
|| :out-of-range||
|| :optional||
|| :read-only	target read-only elements ||
|| :read-write||
|SPECIAL|||										
|:root||root element (html)|
|:empty||has no child|										
|:not(selector)|||        


|PSEUDO ELEMENTS|to style a specific part of the selected element|
|---|---|
|::after||
|::before||
|::first-letter||
|::first-line||
|::selection||

```css
/* <h2 class="emoji" data-emoji="😍"> */
.emoji::before {
  content: attr(data-emoji);
}

article p:first-of-type:first-line {
  font-weight: bold;
  font-size: 1.1em;
  color: darkcyan;
}

::selection {
  background: yellow;
  color: black;
}

How to change css of another element on hover
/* If the cube is directly inside the container:*/
#container:hover > #cube { background-color: yellow; }

/* If cube is next to (after containers closing tag) the container:*/
#container:hover + #cube { background-color: yellow; }

/* If the cube is somewhere inside the container:*/
#container:hover #cube { background-color: yellow; }

/* If the cube is a sibling of the container:*/
#container:hover ~ #cube { background-color: yellow; }

```


### CSS NATIVE VARIABLES
```css
: root { --size: 1em  }
font-size: var(--size);
```

### ANIMATIONS
```css
	
				           ____ animation-duration 
                          /                  
div:hover {  animation: myAnim 5s linear 2s;  }
                         /     \______________  animation-timing-function               
                animation-name				      . interpolation method (acceleration, deceleration)
                    ↓					              linear 		No accelleration   
        @keyframes myAnim {                            ease         Start with gradual acceleration/End with a gradual deceleration   
                from { color:blue;   	              ease-in 	    acceleration on the start
                35%  { color:green; }                  ease-out 	decceleration on the end
                ...n STEPS IN %                        ease-in-out  acceleration on start & deceleration on end
                to   { color:red; }                    steps (nombre, start | end)
        }                                              cubic-bezier( p1, p2, p3, p4)                                            
```

### TRANSFORMATIONS

||||
|---|---|---|
|ORIGIN|||
||transform-origin: 0 0;| default is 50% 50%|
|ROTATING|||
||transform: rotate(-10deg); | Rotate ten degrees anti-clockwise|
|SKEWING|||
||transform: skew(20deg,10deg)|tip over the x-axis by 20 degrees on the y-axis by 10 degrees|
||transform: skew(20deg)||
||skewX, skewY||
|SCALING|||
||transform: scale(2.5)|Multiply width/height and the size of everything contained in the box|
||scaleX, scaleY||
|TRANSLATING|||
||transform: translate(100px,200px)||
||translateX, translateY||
|COMBINING TRANSFORMATIONS|||
||transform: rotate(-10deg) scale(2);||
|MATRIX|||
||transform: matrix(2,-0.35, 0.35,2, 0,0)||
||||

Matrix operations: scale, skew, rotate, translate
    
    scale(a)  scaleX(x)   scaleY(y)  translateX(x)  translateY(y)  translate(x,y)    skewX(x)   skewY(y)   skew(x,y)      rotate(θ)
    ________  _________  __________  _____________  _____________  ______________    _________  _________  __________   ____________
    a 0 0     x 0 0      1 0 0        1 0 0           1 0 0           1 0 0          1 tanx 0    1   0 0    1  tanx 0   cosθ -sinθ 0 
    0 a 0     0 1 0      0 y 0        0 1 0           0 1 0           0 1 0          0  1   0   tany 1 0   tany 1   0   sinθ cosθ  0 
    0 0 1     0 0 1      0 0 1        x 0 1           0 y 1           x y 1          0  0   1    0   0 1    0   0   1     0    0   1

.FlipUpsideDown     { transform: scaleY(-1) }
.FlipLeftToRight    { transform: scaleX(-1) }
.FlipBothDirections { transform: scale(-1)  }
### MEDIA QUERIES

                                            unités (px, em)
                                            ratio avec des fractions (entier/entier). 
                                            résolution sera définie en dpi (points par pouce) ou en dpcm (points par centimètres).
                                                |	
                                            color						support de la couleur (bits/pixel)
                                            color-index					périphérique utilisant une table de couleurs indexées
                                            device-aspect-ratio			ratio du périphérique de sortie (par exemple 16/9)
                                            aspect-ratio				ratio de la zone d'affichage
                                            grid						périphérique bitmap ou grille (ex : lcd)
                                            monochrome					périphérique monochrome ou niveaux de gris (bits/pixel)
                                            resolution					résolution du périphérique (en dpi, dppx, ou dpcm)
                                            scan						type de balayage des téléviseurs (progressive ou interlace)
                                            orientation					orientation du périphérique 
                                                    portrait   h > w
                                                    landscape  w > h 
                                            device-height				dimension en hauteur du périphérique
                                            device-width				dimension en largeur du périphérique
                                            max-height					dimension en hauteur de la zone d'affichage
                                            min-height					
                                            max-width					dimension en largeur de la zone d'affichage
                                            min-width					
                                                /									         
                                            /	
    @media [mediatype] and|not|only (media feature) { css rules }
                \             \___ , means 'or'
                \
                    \
                    \
                screen    									Écrans
                handheld									Périphériques mobiles ou de petite taille
                print		    							Impression
                all											Tous les précédents (by default)
                aural (CSS 2.0) / speech (CSS 2.1)   		Synthèses vocales
                braille           		                    Plages braille
                embossed									Imprimantes braille
                projection									Projecteurs (ou présentations avec slides)
                tty											Terminal/police à pas fixe
                tv											Téléviseur

    @media all and (max-width: 500px) {body { color:red; }} 
    = 
    @media (max-width: 500px) {  body { color:red; }  } 

    @media all and (max-width: 1024px) {  #banniere_img {  display: none; }  }   remove a photo on small devices
    @media screen and (orientation: landscape) { ... }
    @media screen and (orientation: landscape), (max-width: 500px) { ... }
                                                \___ or
    @media screen and (min-device-height: 768px) and (max-device-width: 1024px) { .. }
## CSS LAYOUTS

First were hacks (tables, then floats, then positioning and inline-block) that ignore important functionality (vertical centering…). Flexbox helped for one-dimensional layouts. Grid is good for  complex two-dimensional ones (Flexbox and Grid actually work very well together).

Css grid and flexbox: 
- define a container element
- align items inside container axes/cells: [```justify (horizontal)``` | ```align (vertical)```]-```content```
- align items content: [justify|align]-```items``` 

download.md(assets/slides/web/css_layout_grid.md)

download.md(assets/slides/web/css_layout_flexbox.md)

download.md(assets/slides/web/css_bem.md)

## More
- https://moderncss.dev/guide-to-advanced-css-selectors-part-two/