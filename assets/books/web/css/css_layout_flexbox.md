# CSS FLEXBOX

<div class="slideShowContainer">

<div class="slideShowSlide">
Have responsive layouts!<br>
Good option for centering things in CSS<br>
Container has x-y axis coordinate<br>
<ul>
    <li>horizontal part: Main axis</li>  
    <li>vertical part: Cross axis</li>  
</ul>

<img src='assets/books/web/css/flexbox/flexbox-axis.png'>
</div>

<div class="slideShowSlide">
<pre><code>
.container {
    display: flex;

    flex-direction: row;            place flex-items in row (horizontal)
    flex-direction: row-reverse;    place flex-items in row but in reverse order
    flex-direction: column;         place flex-items in column (vertical)
    flex-direction: column-reverse; place flex-items in column but in reverse order
}
</code></pre>

<img src='assets/books/web/css/flexbox/flex-direction.png'>
</div>

<div class="slideShowSlide">
Flex-wrap: wrapping flex-items inside the flex-container<br/>
no-wrap: items on one line anytime<br/>
wrap: items move to another line when adjusting viewport
<pre><code>
.container {
    display: flex;
    flex-wrap : wrap | nowrap
}
</code></pre>
<img src='assets/books/web/css/flexbox/flex-wrap.png'>
</div>

<div class="slideShowSlide">
Flex-items alignement<br>
<ul>
    <li>horizontal: along main axis: justify-content</li>
    <li>vertical: along cross axis: align-content (same properties as justify-content)</li>
</ul>
<pre><code>
.container {
display: flex;

justify-content: flex-start will place flex-item to the start of flex-container
justify-content: flex-end will place flex-item to the end of flex-container
justify-content: center to center flex-items.
justify-content: space-around` space up around item.
justify-content: space-between uses the whole frame and space item between.
justify-content: space-evenly space all item evenly

align-content: cross axis along placement
}
</code></pre>

Align items:
<pre><code>
align-items: flex-start will place flex-item to the start of flex-container (refer the first image above)
align-items: flex-end will place flex-item to the end of flex-containers
align-items: center to center flex-items.
align-items: baseline place flex-item to base item.
</code></pre>

</div>

</div>