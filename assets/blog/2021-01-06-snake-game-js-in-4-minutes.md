# Snake Game in js in 4 minutes

```        
window.onload=function() {	
	
    document.addEventListener("keydown",keyPush);
        
    // User interactions
    function keyPush(evt) {
	    switch(evt.keyCode) {
		    case 37:
			xv=-1;yv=0;
			break;
            ...
            
    // Draing game status
	setInterval(game,1000/15); // 15x/sec
        function game() {    
            // Move player        
            // Constrainsts: screen boudaries
            // Draw snake
            // Add user position o trail
            // Snake grow when it eat the apple
            // Draw prey
                ↓
            <canvas id="gc" width="400" height="400"></canvas>
}

```
To start, press <kbd>←</kbd> <kbd>↑</kbd> <kbd>↓</kbd> <kbd>→</kbd>            
download.iframe(assets/blog/assets/snake_in_4_min.html, 500, 500)

download.raw(assets/blog/assets/snake_in_4_min.html)

