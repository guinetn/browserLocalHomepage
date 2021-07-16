# petite-vue

https://www.npmjs.com/package/petite-vue
https://github.com/vuejs/petite-vue

5.5Kb Petite Vue, a “subset of Vue optimized for progressive enhancement.”

```js
<script src="https://unpkg.com/petite-vue" defer init></script>

<!-- anywhere on the page -->
<div v-scope="{ count: 0 }">
  {{ count }}
  <button @click="count++">inc</button>
</div>
```

Use v-scope to mark regions on the page that should be controlled by petite-vue.
The defer attribute makes the script execute after HTML content is parsed.
The init attribute tells petite-vue to automatically query and initialize all elements that have v-scope on the page.