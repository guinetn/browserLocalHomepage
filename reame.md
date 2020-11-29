# How to run
>cd <here>
>serve   	(npm i -g serve)

# Learned

## CSS
@import url('fontawesome/css/all.min.css');

## JS

<script type="module" src="views.js"></script>
           ____/ 
views.js  /    
		 /___ to use "import..."				
	    _______________/		 ___ export const assets = `aaa`;
       /						/ 
	import * as assets from "./aaa.js"
	...
	console.log(assets.assets);

	const getTime = () => new Date().toLocaleTimeString();
	                -----
	setInterval( () => clock.innerText = getTime(), 1000 );
	             ------                             ----

	const views = document.querySelectorAll(".view");
	[...views].map(v=> v.id[0]==key ? v.classList.add("active") : v.classList.remove("active"));

	async function getLinks() {
	-----  try {
		    let response = await fetch('/links.json');
		    			   -----
		    let json = await response.json();         remove the fetch(...).then(res=>res.json()).then(res=>...)
		               -----
		    console.log(json);
			console.log(assets.assets);
		  }
		  catch(e) {
		    console.log('Error!', e);
		  }
		}

	document.addEventListener("keydown", (e) => onViewChange(e));
								   \     ------              -   
									\___if (e.key=="+") 

  	Create html elements on the fly

	  	const html = ["<div class='bookmark-set'>"];
	    html.push(`<div class="bookmark-title">${b.title}</div>`);
	    html.push('<div class="bookmark-inner-container">');
	    html.push(
	      ...b.links.map(
	        (l) =>
	          `<a class="bookmark" href="${l.url}" target="_blank">${l.name}</a>`
	      )
	    );
	    html.push("</div></div>");
	    return html.join("");

		bookmarkContainer.innerHTML =...
		                 ---   ----

	    function createLink(l) {
			const fragment = document.getElementById("linkTemplate");        
			// Create an instance of the template content
		    const instance = document.importNode(fragment.content, true);
		    // Add relevant content to the template
		    let a = instance.querySelector("#link");
		    a.href = l.l;             
		    a.classList.add("jsonlink");
		    if (l.i != undefined)
		    	l.i.split(' ').map(c => a.classList.add(c));         
		    else 
		    	a.innerText=l.n;         
		    return instance;
		}

		function extractLinks(links) {
			  		
		  		for (var key in links) {
		          if (typeof links[key] == "object" || typeof links[key] == "array") {
					const target = document.querySelector(`#${key}`);		
					if (target==undefined)
						continue;
					links[key].forEach(function(l){ 		
			        	target.appendChild(createLink(l));
					});
				  }
		        }	
		}		