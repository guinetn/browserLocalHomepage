# CSS Module

A CSS file in which all class names and animation names are scoped locally by default. All URLs (url(...)) and @imports are in module request format (./xxx and ../xxx means relative, xxx and xxx/yyy means in modules folder, i. e. in node_modules).

A build step that changes class names and selectors to be scoped.

Why: modular and reusable CSS!
- No more conflicts
- Explicit dependencies
- No global scope

- 1. Write CSS files normally

style.css
```css
.className {
  color: green;
}
```

2. Import the CSS Module from a JS Module
it exports an object with all mappings from local names to global names

```js
import styles from "./style.css";
// import { className } from "./style.css";
element.innerHTML = '<div class="' + styles.className + '">';
```

- CSS Modules are compiled to a low-level interchange format called [ICSS](https://github.com/css-modules/icss) (Interoperable CSS)

## more 
- https://github.com/css-modules/css-modules