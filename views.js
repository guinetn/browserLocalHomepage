import * as assets from "./aaa.js"

let currView = -1;
const views = document.querySelectorAll(".view");
document.addEventListener("keydown", (e) => onKeydown(e));
document.addEventListener("click", (e) => onClick(e));

function onKeydown(e) {
	
	if (e.ctrlKey || e.shiftKey)
		return;

	let key = e.key.toLowerCase();
	if (e.key=="+") { // Navigate by "+"	
		currView = views.length <= currView+1 ? 0 : currView+1;	
		key = views[currView].id.slice(0,2);
	}
	else if (e.key=="-") { // Navigate by "+"	
		currView = currView-1 < 0 ? views.length-1 : currView-1;	
		key = views[currView].id.slice(0,2);
	}
	else if (! [...views].some(v=>v.id[0]==key))
		return;

	[...views].map(v=> v.id.slice(0,key.length)==key ? v.classList.add("active") : v.classList.remove("active"));
}

async function getLinks() {
  try {
    let response = await fetch('links.json');
    let jsonLinks = await response.json();		    
    extractLinks(jsonLinks);
  }
  catch(e) {
    console.log('Error!', e);
  }
}

function createLink(l, prefix) {
	if (l.name=='')
		return null;

	const fragment = document.getElementById( `${prefix}linkTemplate`);        
	// Create an instance of the template content
    const instance = document.importNode(fragment.content, true);
    // Add relevant content to the template
    let a = instance.querySelector("#link");
    a.href = l.ref;             
    a.classList.add("jsonlink");
    if (prefix != '') // for vlinks: o xxxxx
    	a.classList.add("mark");
    a.title = l.name;
    if (l.class != undefined)
    	l.class.split(' ').map(cl => a.classList.add(cl)); // classlist doesn't accept spaces...  
    else 
    	a.innerText=l.name;  
    
    return instance;
}

function createText(l) {
	let elem = document.createElement("div");
	elem.innerText = l.name;
	elem.classList.add("text");
	if (l.class != undefined)
    	l.class.split(' ').map(cl => elem.classList.add(cl));
    return elem;
}

function extractLinks(links) {
	  		
  		for (var key in links) {
          if (typeof links[key] == "object" || typeof links[key] == "array") {          	
			const target = document.querySelector(`#${key}`);		
			const isVLinks = (key.slice(0,6) == 'vlinks' || key.slice(0,4)=="text");
			if (isVLinks && target!=undefined)
			{
				let h3 = document.createElement("h3");				
				h3.innerText = key.split("_").pop().toUpperCase();
				target.appendChild(h3);
			}

			if (target==undefined)
				continue;
			links[key].forEach(function(l){ 		
				let elem = null;
				switch(key.split('_')[0])
				{
	        		case "text":
						elem = createText(l);
	        			break;
	        		case "hlinks":
	        		case "vlinks":
						elem = createLink(l, isVLinks ? "V" : "");
	        			break;
				}
				if (elem != null)
	        		target.appendChild(elem);
			});
		  }
        }	
}		

function onClick(e) {
	if (e.target.matches('.copy')) {
		copyToClipboard(e.target.innerText);		
	}
}

async function copyToClipboard(stringToCopy) {
	if (navigator.clipboard) {
	  try {
	    await navigator.clipboard.writeText(stringToCopy);        
	  } catch (err) {
	    console.error(`Failed to copy ${stringToCopy}`, err);
	  }
	}
}


const getTime = () => new Date().toLocaleTimeString();

window.onload = () => {
	const clock = document.querySelector("#clock");		
	setInterval(()=> clock.innerText = getTime(), 1000 );

	getLinks();
	// weather()
}