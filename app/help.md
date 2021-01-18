- ##version##
- ##github##

NAVIGATE IN BOOKS

* <kbd>CTRL</kbd>+<kbd>→</kbd> or <kbd>+</kbd>: go to next book
* <kbd>CTRL</kbd>+<kbd>←</kbd> or <kbd>-</kbd>: go to previous book
* <kbd>NUMPAD</kbd> <kbd>0</kbd>-<kbd>9</kbd>: go to the book number… pressed
* <kbd>LETTERS</kbd> <kbd>A</kbd>-<kbd>Z</kbd>: go to the book having a name starting by the letter pressed


NAVIGATE IN CHAPTERS

* <kbd>→</kbd> Next chapter (Enter chapter mode when not in)
* <kbd>←</kbd> Previous chapter (Exit chapter mode when done while on 1<sup>st</sup> chapter)
* <kbd>Shift</kbd> Exit chapter mode

OTHERS

* <kbd>F</kbd> Go Full screen
* <kbd>ESC</kbd> Exit Full screen
* Text selected with the mouse for more than 3 sec is automatically copied (snackbar warning)

Chapters syntax: standard markdown + additional syntax:
    
* <strong>download.md(assets/chapters/web/myfile.md)</strong> : a markdown file:
* <strong>download.chapter(myfile.md)</strong> : a markdown file in 'assets/chapters' 
* <strong>download.raw(https://<span>githubusercontent.com/abcdef/sourcefile.txt</span>)</strong> : a file as it is (raw, not prettified)
* <strong>download.html(https://<span>githubusercontent.com/abcdef/sourcefile.txt</span>)</strong> : an html (interpreted in innerHTML)
* <strong>download.code(https://<span>githubusercontent.com/abcdef.cpp</span>)</strong> : a code file (prettified by extension)
* <strong>download.iframe(url [,w,h])</strong> : an iframe 
*  └── download.iframe(assets/chapters/web/front/react_samples/react01/index.html)
*  └── download.iframe(assets/chapters/web/front/react_samples/react01/index.html,500,200)
* <strong>[video_title]<span>(https://www.</span><span>youtube.com/watch?xyzabc)</span></strong> : a youtube video: any link containing 'youtube' 
* <strong>Horizontal Slide Show</strong>: a slideShowContainer that contains slideShowSlide items

<pre><code>
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
</code></pre>