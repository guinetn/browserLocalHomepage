### BEM methodology (Organize CSS with a Modular Architecture: OOCSS, BEM, SMACSS)

Block, Element, Modifier methodology
CSS class-names naming convention so they are consistent, isolated, and expressive
To better understand the relationship between the HTML, CSS in a given project

.block {}
.block__element {}          represents a descendent of .block
.block--modifier {}         represents a different state or version of .block.

```css
/* Block component */
.btn {}
/* Element that depends upon the block */ 
.btn__price {}
/* Modifier that changes the style of the block */
.btn--orange {} 
.btn--big {}

<a class="btn btn--big btn--orange" href="http://css-tricks.com">
    <span class="btn__price">$9.99</span>
    <span class="btn__text">Subscribe</span>
</a>
```

MATERIAL DESIGN LITE (BEM written)
https://getmdl.io/templates/index.html
CSSWizardry             http://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/
CSS-Tricks              https://css-tricks.com/bem-101/
Smashing Magazine       http://www.smashingmagazine.com/2012/04/16/a-new-front-end-methodology-bem/
