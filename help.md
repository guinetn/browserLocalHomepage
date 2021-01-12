- ##version##
- ##github##

NAVIGATE IN VIEWS

* <kbd>CTRL</kbd>+<kbd>→</kbd> or <kbd>+</kbd>
* <kbd>CTRL</kbd>+<kbd>←</kbd> or <kbd>-</kbd>
* <kbd>NUMPAD</kbd> <kbd>0</kbd>-<kbd>9</kbd>: go to the view number…pressed
* <kbd>LETTERS</kbd> <kbd>A</kbd>-<kbd>Z</kbd>: go to view having a name starting by the letter pressed


NAVIGATE IN SLIDES

* <kbd>→</kbd> Next slide (Enter slide mode when on 1<sup>st</sup> slide)
* <kbd>←</kbd> Previous slide (Exit slide mode when on 1<sup>st</sup> slide)
* <kbd>Shift</kbd> Exit Slide mode

OTHERS

* <kbd>F</kbd> Go Full screen
* <kbd>ESC</kbd> Exit Full screen
* Selection done with the mouse is automatically copied every 3 sec (snackbar warning)

Slides syntax: standard markdown + additional syntax to include…
    
* <strong>download.md(assets/slides/myfile.md)</strong> : a markdown file:
* <strong>download.raw(https://<span>githubusercontent.com/abcdef/sourcefile.txt</span>)</strong> : a file as it is (raw, not prettified)
* <strong>download.html(https://<span>githubusercontent.com/abcdef/sourcefile.txt</span>)</strong> : an html (interpreted in innerHTML)
* <strong>download.code(https://<span>githubusercontent.com/abcdef.cpp</span>)</strong> : a code file (prettified by extension)
* <strong>download.iframe(url,[w,h])</strong> : an iframe 
* &nbsp; download.iframe(assets/slides/web/front/react_samples/react01/index.html)
* &nbsp; download.iframe(assets/slides/web/front/react_samples/react01/index.html,500,200)
* <strong>[video_title]<span>(https://www.</span><span>youtube.com/watch?xyzabc)</span></strong> : a youtube video: any link containing 'youtube' 
* Horizontal Slide Show: a slideShowContainer that contains slideShowSlide items
<pre><code><div class="slideShowContainer">   
  <div class="slideShowSlide">  
    ...  content #1
  </div>  
  <div class="slideShowSlide">  
    ...  content #2
  </div>  
</div>  
</code></pre>
