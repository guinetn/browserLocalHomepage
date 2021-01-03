export let slideShow = {
    
    slideIndex : {},
    
    plusSlides: function(id,n) {
        this.slideIndex[id] += n;
        this.showSlides(id);
    },

    currentSlide: function(id,n) {
        this.slideIndex[id] = n;
        this.showSlides(id);
    },

    showSlides: function(id) {
    
    if (id==null)  
        return;
    
    var i;
    var slides = document.querySelectorAll(`#${id} .slideShowSlide`);
    
    if (slides.length<1) 
        return;

    const currentPosition = this.slideIndex[id];
    const dots = document.querySelectorAll(`#${id}_dotContainer .slideShowDot`);
    if (currentPosition > slides.length) {
        this.slideIndex[id] = 1;
    }
    if (currentPosition < 1) {
      this.slideIndex[id] = slides.length;
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
         dots[i].classList.remove("activeSlideshow");
    }
    slides[this.slideIndex[id] - 1].style.display = "block";
    dots[this.slideIndex[id] - 1].classList.add('activeSlideshow');    
    },

    init: function() {
        // Add Next/prev buttons to the slideshow
        const slideShowContainers = document.querySelectorAll(".slideShowContainer");
        
        if (slideShowContainers.length==0)
            return;
        
        this.slideIndex = {};
        for (var i = 0; i <= slideShowContainers.length; i++) {
          this.slideIndex[`sshow${i + 1}`] = 1;
        }
        
        [...slideShowContainers].map((kont,i)=> {
            kont.classList = 'slideShowKontainer';
            const id = `sshow${i + 1}`;
            kont.id = id;
            
            // Add dots/bullets/indicators
            let dotContainer = document.createElement("div");
            dotContainer.id = `${id}_dotContainer`;
            dotContainer.className = 'slideShowDotContainer';

            [
              { class: 'slideShowSlidePrev', text: '&#10094;' },
              { class: 'slideShowSlideNext', text: '&#10095;' },
            ].forEach(element => {
                let bt = document.createElement("a");
                bt.classList = element.class;
                bt.innerHTML = element.text;    
                kont.appendChild(bt);
            });

            const slidesShow = kont.querySelectorAll(`.slideShowSlide`);
            [...slidesShow].map( (s,is) => {
            let dotSpan = document.createElement("div");
            dotSpan.className = 'slideShowDot';
            dotSpan.setAttribute('data-dotSpan', is+1);
            dotContainer.appendChild(dotSpan);
            })
            
            kont.appendChild(dotContainer);
        })
       
        for (let sid = 0; sid <= slideShowContainers.length; sid++) 
            this.showSlides(`sshow${sid + 1}`);
    }
}

