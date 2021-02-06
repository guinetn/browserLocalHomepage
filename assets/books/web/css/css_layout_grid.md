# CSS GRID

Solve 2D layouts (flexbox is one dimension)  
- non-flexible units: px
- flexible units: fr

<div class="slideShowContainer">

 <!-- Full-width slides/quotes -->
<div class="slideShowSlide">
1. Define a container element 
<pre><code>

.container {
  display: grid | inline-grid;       generates a block-level or an inline-level grid  
}
</code></pre>
</div>

<div class="slideShowSlide">
2. Defines the columns and rows of the grid 
<pre><code>
.container {
  grid-template-columns: 40px 50px auto 50px 40px;
  grid-template-rows: 25% 100px auto;
}

grid-template-columns: repeat(3, 20px)
grid-template-columns: 1fr 1fr 1fr;      Each col width is third the width of the grid container
                                         fr: fraction of the free space of the grid container
grid-template-columns: 1fr 50px 1fr 1fr; free space is calculated after any non-flexible items (1/3rd free space + 50px)  


SHORTHAND:
grid: 100px 300px / 3fr 1fr;          grid: columns/rows


SET AUTOMATIC ROW/COL SIZE FOR ITEMS PLACED IN UNDEFINED ROW/COL: 
grid-auto-columns: <track-size> ...;
grid-auto-rows: <track-size> ...;
</code></pre>
<strong>Grid lines</strong> are automatically assigned positive and negative numbers
<img src='assets/books/web/css/grid/grid-template01.png'>
<br/>
<br/>
grid-template-areas: "Visual" grid definition
<pre><code>
.container {
  display: grid;
  grid-template-columns: 50px 50px 50px 50px;
  grid-template-rows: auto;
  grid-template-areas:               Use names to defines a grid template (more visual)
    "header header header header"    Repeating grid area name = span those cells
    "main main . sidebar"            . = empty grid cell
    "footer footer footer footer";   none = no grid areas are defined
}
</code></pre>
<img src='assets/books/web/css/grid/grid-template02.png'>
<br/>
Shorthand: grid-template
<pre><code>
.container {
  grid-template: none | <grid-template-rows> / <grid-template-columns>;


  grid-template:
    [row1-start] "header header header" 25px [row1-end]
    [row2-start] "footer footer footer" 25px [row2-end]
    / auto 50px auto;
}
</code></pre>

</div>

<div class="slideShowSlide">

POSITION GRID CHILDREN: use grid-column and grid-row to position your grid items 
<pre><code>
grid-column-start: <number> | <name> | span <number> | span <name> | auto;
grid-column-end: <number> | <name> | span <number> | span <name> | auto;
grid-row-start: <number> | <name> | span <number> | span <name> | auto;
grid-row-end: <number> | <name> | span <number> | span <name> | auto;
}


SHORTHAND:
.item {
  grid-column: <start-line> / <end-line> | <start-line> / span <value>;
  grid-row: <start-line> / <end-line> | <start-line> / span <value>;
}

<line>        – can be a number to refer to a numbered grid line, or a name to refer to a named grid line
span <number> – the item will span across the provided number of grid tracks
span <name>   – the item will span across until it hits the next line with the provided name
auto          – indicates auto-placement, an automatic span, or a default span of one
</code></pre>

Aligns a grid item inside a cell 
<pre><code>
.item {
  justify-self: start | end | center | stretch;     Horizontal align
  align-self: start | end | center | stretch;       Vertical align
}
</code></pre>


<pre><code>

.item-a {
  grid-area: header;
}...  

.item-a {
  grid-column-start: 2;
  grid-column-end: five;
  grid-row-start: row1-start;
  grid-row-end: 3;
}

.item-b {
  grid-column-start: 1;
  grid-column-end: span col4-start;
  grid-row-start: 2;
  grid-row-end: span 2;
}

.item-a {
  grid-column: 1;
  grid-row: 1 / 3;       .item-a will start on row line 1 and end at row line 2 
}
.item-a {
  grid-column: 1 / 2;    .item-a will start on column line 1 and end at column line 2
  grid-row: 2 / 3;
}

.item-c {
  grid-column: 3 / span 2;
  grid-row: third-line / 4;
}
</code></pre>

<img src='assets/books/web/css/grid/grid-children.png'>
</div>


<div class="slideShowSlide">
Width of the gutters between the columns/rows<br/>  
only created between the columns/rows, not on the outer edges
<pre><code>
.container {
  grid-template-columns: 100px 50px 100px;
  grid-template-rows: 80px auto 80px;  


  column-gap: 10px;     Unprefixed properties (no grid-xxx) are already supported in 
  row-gap: 15px;        Chrome 68+, Safari 11.2 50+, Opera 54+   
</code></pre>


SHORTHAND: 
<pre><code>
.container {
  grid-gap: 15px 10px;
  gap: 15px 10px;       unprefixed properties
}
</code></pre>
<img src='assets/books/web/css/grid/grid-gutters.png'>

</div>

<div class="slideShowSlide">
Align items horizontally
<pre><code>
.container {
  justify-items: start | end | center | stretch;
}

start   – aligns items to be flush with the start edge of their cell 
end     – aligns items to be flush with the end edge of their cell
center  – aligns items in the center of their cell
stretch – fills the whole width of the cell (this is the default)
</code></pre>

Align items Vertically
<pre><code>
.container {
  align-items: start | end | center | stretch;
}

start   – aligns items to be flush with the start edge of their cell
end     – aligns items to be flush with the end edge of their cell
center  – aligns items in the center of their cell
stretch – fills the whole height of the cell (this is the default)
</code></pre>


SHORTHAND: <strong>place-items</strong>
<pre><code>
.container {
  place-items: <align-items> / <justify-items>;
}
</code></pre>


</div>


<div class="slideShowSlide">
non-flexible units (px) = total grid size < grid container size<br/>  
justify-content: set the horizontal alignment of the grid within the grid container<br/>
align-content: set the vertical alignment of the grid within the grid container<br/>
place-content: <align-content> / <justify-content> is the shorthand<br/>
<pre><code>
.container {
  justify-content: start | end | center | stretch | space-around | space-between | space-evenly;    
  align-content: start | end | center | stretch | space-around | space-between | space-evenly;    
}


end           – aligns the grid to be flush with the end edge of the grid container
center        – aligns the grid in the center of the grid container
stretch       – resizes the grid items to allow the grid to fill the full height of the grid container
space-around  – places an even amount of space between each grid item, with half-sized spaces on the far ends
space-between – places an even amount of space between each grid item, with no space at the far ends
space-evenly  – places an even amount of space between each grid item, including the far ends
</code></pre>
<img src='assets/books/web/css/grid/align-content.png'>

</div>


<div class="slideShowSlide">
Items inside not defined col/row<br/>
grid-auto-flow controls the auto-placement algorithm <br/>
<pre><code>
.container {
  grid-auto-flow: row | column | row dense | column dense;
}

row    – auto-placement algorithm to fill in each row in turn, adding new rows as necessary (default)
column – auto-placement algorithm to fill in each column in turn, adding new columns as necessary
dense  – auto-placement algorithm to attempt to fill in holes earlier in the grid if smaller items come up later
</code></pre>
<img src='assets/books/web/css/grid/grid-auto-flow_row.png'>
</div>


</div>  

- https://css-tricks.com/snippets/css/complete-guide-grid/
- https://www.freecodecamp.org/news/flexbox-vs-grid-how-to-build-the-most-common-html-layouts/

