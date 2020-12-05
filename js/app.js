import * as assets from "./addons.js"

const getTime = () => new Date().toLocaleTimeString();

class app {

	currentView = null;
	views = []; // [{ id:0, dom: null, name: '', slideId: 0 }, …]
	currentSlide = 0;
	currentSlidesFile = null;
	slidesVisible = null;
	slides = [];	
	slidesFolder = '';

	constructor(slidesFolder, elem) { 		
		document.querySelectorAll(elem).forEach((v,i) => this.views.push( {'id':i, 'name':v.id, 'dom':v, 'slideId':0} ));
		this.currentView = this.views[0];
		this.slidesFolder = slidesFolder;
	}

	scrollTo(y=0) {
		document.documentElement.scrollTo({top: y,behavior: "smooth"});			
	}

	onViewKeydown(e) {
		if (e.shiftKey)
			return;

		let key = e.key.toLowerCase();
		
		// Navigate in views by [+] or [CTRL + →]
		if (e.key=="+" || (e.ctrlKey && e.keyCode==39  /*right*/)) { 
			this.currentView = this.views[this.views.length <= this.currentView.id+1 ? 0 : this.currentView.id+1];	
			key = this.currentView.name.slice(0,3);
		}
		// Navigate in views by "-" or [CTRL + ←]	
		else if (e.key=="-" || (e.ctrlKey && e.keyCode==37  /*left*/)) { 
			this.currentView = this.views[this.currentView.id-1 < 0 ? this.views.length-1 : this.currentView.id-1];	
			key = this.currentView.name.slice(0,3);
		}
		else if (e.ctrlKey || ! [...this.views].some(v=>v.name[0]==key))
			return; // no key match a view name
		
		e.preventDefault();
		this.scrollTo(0);
		// hide slides
		this.toggleSlidesVisibility(false);				
		// display view
		this.views.forEach(view=> view.name.slice(0,key.length)==key ? view.dom.classList.add("active") : view.dom.classList.remove("active"));
	}

	onSlideKeydown(e) {
		if (e.keyCode == 27 || e.shiftKey) {
		 	// [ESC] or [shift]	key 	
		 	this.toggleSlidesVisibility(false);		 	
		 	if (this.currentSlide>0)
		 		this.currentSlide--; // to come back on the same slide after [esc]] (as we do [→] to show it again, we don't want slide+0)
		 	 this.currentView.slideId = this.currentSlide+1; // memo thz slide id to retrieve after anothers view navigation and come back 
		 }
		 else {	 	
			switch (e.keyCode) {
		        case 37: // left arrow key          	        	          
		          this.changeSlide(-1);
		          break;
		        case 39: // right arrow key	        	          
		          this.changeSlide(+1);	          
		          break;
				case 70: // f key
					if (this.slidesVisible)
						utils.fullScreen(this.slides[this.currentSlide]);
					else
					  	utils.fullScreen(this.currentView.dom);
		          break;
		    }
		 } 
	}
	async changeSlide(direction) { 

		if (this.currentSlidesFile != this.currentView.name)
		{	    		
	    	this.createSlidesInDom(this.currentSlidesFile);
	    	this.currentSlide = this.currentView.slideId;
			return;
		}
		
		// Press [←] while on first slide: hide		
		if (this.currentSlide==0 && direction==-1)  
		{
			this.toggleSlidesVisibility(false);					
			return;
		}
		// Press [→] while slides are not visible: show			
		else if (!this.slidesVisible && this.currentSlide==0 && direction==+1)	
		{
			this.scrollTo(0);
			this.toggleSlidesVisibility(true);      		
			return;
		}

		 this.currentSlide += direction;
		if (this.slides.length <= this.currentSlide)
	       this.currentSlide = 0;   
	 	else if (this.currentSlide < 0) 
	       this.currentSlide = 0;   
	    	    
	   	this.scrollTo(0);
	    this.toggleSlidesVisibility(true);
	}
	async downloadViewSlides(folder, slideFile) {
	  try {	  		  	
	    let response = await fetch(`${folder}/${slideFile}.md`);
	    let markdown = await response.text();		
	    
	    const html = this.markdownToHtml(markdown);
	    const htmlSides = html.split("<hr />");		
	    return htmlSides;
	  }
	  catch(e) {
	    console.log(`Error in downloadViewSlides(${slideFile})`, e);
	  }
	}
	createSlidesInDom() {
		
		this.deleteExistingSlides();

		this.currentSlidesFile = this.currentView.name;		
		
		this.downloadViewSlides(this.slidesFolder, this.currentSlidesFile)
	        .then((htmlSlides)=>{         
	          this.appendSlides(htmlSlides);                  
			  this.slides = document.querySelectorAll(".slide");          
	          this.toggleSlidesVisibility(true);
	          this.renderCurrentSlide();
	        });
	}
	appendSlides(slides) {
	    slides.forEach((html, i) => {
	      const slide = document.createElement("div");
	      slide.innerHTML = `<div>${slides[i]}</div>`;
	      slide.id = `p${i+1}`;
	      slide.className = "slide";
	      document.querySelector("#main").appendChild(slide);
	    });
	} 
	markdownToHtml(data) {
	  // Transform md → html
	  var converter = new showdown.Converter();
	  return converter.makeHtml(data);
	}
	renderCurrentSlide() { 		
		this.slides.forEach((s,i)=> (this.slidesVisible && i==this.currentSlide) ? s.classList.add("current") : s.classList.remove("current"));
	}
	toggleSlidesVisibility(forceVisibility) { 		
		if (forceVisibility!=undefined)
			this.slidesVisible = forceVisibility;
		else
			this.slidesVisible = ! this.slidesVisible;				
	    
	    this.renderCurrentSlide();		
		// this.progress.setProgress("#progress-page", this.pageCount(), this.current);
	}
	deleteExistingSlides() {
		if (this.slides.length>0)
			this.slides.forEach(s=>s.remove());

		this.slides = null;				
		this.currentSlide = 0;	
	}	
}

let utils = {

	clock: document.querySelector("#clock"),
	
	snackbar: document.getElementById("snackbar"),

	mainbox : document.querySelector(".mainbox"),
	modalContent: document.getElementById("modalContent"),
	modalTitle: document.getElementById("modalTitle"),
	
	alarm: document.getElementById("alarm"),
	alarmSign: document.getElementById("alarmSign"),
	alarmTimer: null,	
	alarmReason: 0,
	alarmVisible: false,
	alarmRate:0,
	alarmRemainder:0,

	init: function(){
		setInterval(()=> this.heartbeat(), 1000 );
	},

	heartbeat: function() {		
		clock.innerText = getTime();
		if (this.alarmTimer)
		{
			this.alarmRemainder -= this.alarmRate;
			this.alarmSign.style.width = `${Math.trunc(this.alarmRemainder)}%`;				
		}
	},

	copyToClipboard: async function(stringToCopy) {		
		  try {
		    await navigator.clipboard.writeText(stringToCopy);        
		    this.snackbar("copied");
		  } catch (err) {
		    console.error(`Failed to copy ${stringToCopy}`, err);
		  }		
	},

	modal: function(title, content) {	  
	  this.modalTitle.innerText = title;
	  this.modalContent.querySelectorAll("*").forEach((n) => n.remove());
	  this.modalContent.appendChild(content);
	  this.mainbox.classList.add("visible");
	},

	modalClose: function() {
		this.mainbox.classList.remove("visible");
	},

	alarmOpenClose: function() {
		this.alarm.classList.toggle("alarm");
		this.alarmVisible = this.alarm.classList.contains("alarm");
	},

	alarmSet: function(minutes, reason) {

		if (minutes==0) {
			clearTimeout(this.alarmTimer);
			const msg = `Alarm canceled: ${this.alarmReason}`;
			document.querySelector(".alarmItem.alarm-active").classList.remove("alarm-active");
			this.speak(msg);
			this.snackbar(msg);			
			this.alarmSign.classList.remove("active");
			this.alarmRate = 0;
			return;
		}

		// Start Countdown
		this.alarmSign.classList.add("active");		
		this.alarmRemainder = 100;	
		this.alarmRate = 100/(minutes*60); // rate at wich, each sec, thecountdown progressbar must be reduced

		this.alarmReason = reason;
		this.alarmTimer = setTimeout(() => {  
						const msg = `Alarm (${minutes} min elapsed)<br/>${reason != '' ? '"'+reason+'"' : ''}`;
					 	this.snackbar(msg, 5000);	
						if (msg.trim().slice(0,2)!="//") // dot not speak msg prefixed by //
							this.speak(msg.replace("<br/>",""));					 	
						document.querySelector(".alarmItem.alarm-active").classList.remove("alarm-active");
						this.alarmSign.classList.remove("active");						
					 }, minutes*60*1000);						      
	},

	speak: function(msg) {                
		if (msg != "" && window.speechSynthesis) {
        	var to_speak = new SpeechSynthesisUtterance(msg);
     	   	window.speechSynthesis.speak(to_speak);
        }
    },

	snackbar: function(msg, duration=2500) {
	  snackbar.innerHTML = msg;
	  snackbar.classList.add('show');
	  setTimeout(() => snackbar.classList.remove('show'), duration);
	},

	fullScreen: function(elem) {	    
	    const request = elem.requestFullscreen
	                 || elem.webkitRequestFullScreen
	                 || elem.mozRequestFullScreen
	                 || elem.msRequestFullscreen;
	    request.call(elem);
	}	  
}

async function downloadLinks(file) {
  try {
    let response = await fetch(file);
    let jsonLinks = await response.json();		    
    extractLinks(jsonLinks);
  }
  catch(e) {
    console.log('Error!', e);
  }
}

function extractLinks(links) {
	  	
	const regex = /(?<link>[^\[\(]*)+(\[+(?<classes>[^\]]*)?\]+)*(\(+(?<description>[^\)]*)?\)+)*/;
	
	for (var key in links) {
      if (typeof links[key] == "object" || typeof links[key] == "array") {          	
		
		const container = document.querySelector(`#${key}`);				
		if (container == undefined)
			continue;
		
		const containerAttr = container.getAttribute("data-info");
		if (containerAttr==null || (containerAttr!=null && containerAttr.toLowerCase().indexOf('-t')<0))
		{
			// Add title
			let h3 = document.createElement("h3");				
			h3.innerText = key.toUpperCase().replace('_',' ');
			container.appendChild(h3);
		}

		links[key].forEach(function(item){ 		

			var m = regex.exec(item);   // ex: "https://gmail.com[fas fa-envelope](GMAIL)"
			if (m != null)	
			{
				let link = m.groups["link"];
				let classes = m.groups["classes"];
				let description = m.groups["description"];
				
				let elem = createLink(link, classes, description);        	
				if (elem != null)
	        		container.appendChild(elem);
        	}
        	else
        		console.log(`ExtractLinks(): Error in parsing ${item}`);
		});
	  }
    }	
}	
let simplifyLink = (link) => {
  /*
	https://developers.google.com/analytics → developers.google.com/analytics
	https://www.nasaspaceflight.com			→ nasaspaceflight.com 

	*/ 
	let match = /((?<prot>https?):\/{2}(w{3})?\.?(?<domain>[^/]*)\/?(?<query>.*)?|(?<link>.*))?/.exec(link);
	if (match != null)
	{
		if (match.groups["link"] != undefined) return match.groups["link"];
    else return match.groups["domain"];
	}
}
function createLink(link, classes, description) {

	const prefix = (classes || 'block').indexOf('inline') >=0 ? "inline" : "block";
	const fragment = document.getElementById( `${prefix}LinkTemplate`);        
    const instance = document.importNode(fragment.content, true);

    let a = instance.querySelector(".topicLink");
    a.href = link;                     
    a.title = link;
    if (classes != undefined)
    	classes.split(' ').forEach(cl => a.classList.add(cl)); // classlist doesn't accept spaces...  
    
    if (prefix != 'inline')
    	a.innerText = description || simplifyLink(link) || "???";  
    
    return instance;
}

	

function initTools() {
	document.querySelector("#timestamp").value = Math.floor(new Date().getTime()/1000.0);		
	document.querySelector("#timestampDecode").value = Math.floor(new Date().getTime()/1000.0);		
	document.querySelector("#timestampEncode").value = new Date().toISOString();
}

document.addEventListener('DOMContentLoaded', function () {
	
	utils.init();

	let application = new app('assets/slides', '.view');
	
	document.addEventListener("keydown", function(e) {
		if (utils.alarmVisible)
			return; // we need all the keys to enter alarm msg

		application.onViewKeydown(e);
		if (! e.defaultPrevented)
			application.onSlideKeydown(e);
	});
	document.addEventListener("click", function(e) {
		
		if (e.target.matches('.copy')) {
			utils.copyToClipboard(e.target.innerText);		
		}
		else if (e.target.matches('#help')) {
			if (utils.mainbox.classList.contains("visible"))
				utils.modalClose();		
			else
			{				
				const fragment = document.getElementById('helpTemplate');        
    			const instance = document.importNode(fragment.content, true);    			
				utils.modal("HELP", instance);
			}
		}
		else if (e.target.matches('.modal-close') || e.target.className=='mainbox visible') {
			utils.modalClose();		
		}
		else if ( e.target.matches('#clock') || e.target.matches('#alarm') || (utils.alarmVisible && e.target.className=='active view')) {
			utils.alarmOpenClose();			
		}				
		else if (e.target.matches('.alarmItem') ) {

			// alarm already set ? → Cancel it
			if (e.target.classList.contains("alarm-active")) {
				utils.alarmSet(0);
				document.querySelector(".alarmItem.alarm-active").classList.remove("alarm-active");
				return;
			}

			// set alarm
			const alarmSelected = document.querySelector(".alarmMessage");
			const alarmReason = alarmSelected.value || "";
			const alarmDurationMin = e.target.getAttribute("data-duration");
			e.target.classList.toggle("alarm-active");
			utils.alarmOpenClose();			
			utils.snackbar(`Alarm in ${alarmDurationMin} min<br/>${alarmReason}`);	
			utils.speak(`Alarm in ${alarmDurationMin} min`);	
			utils.alarmSet(alarmDurationMin, alarmReason);
		}		
	});

	downloadLinks('assets/topics.json');
	initTools();
	
	if (showdown)
		showdown.setFlavor('github');
	// weather()
});