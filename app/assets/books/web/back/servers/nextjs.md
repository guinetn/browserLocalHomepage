# Next.js

React framework with hybrid static & server rendering (no config)
Pre-rendering can result in better performance and SEO

- https://nextjs.org/
- https://www.youtube.com/watch?v=Sklc_fQBmcs&t=158s
- https://github.com/fireship-io/nextjs-basics

Classic CSR (Client Side Rendering) drawbacks
- content is not reliably indexed (react=content must be rendered)
- can be longer to have first contentful paint

Next = fully rendered for bots + interactive content for users
- creates fast search engine optimized react apps with no configuration
- First thing search bot see is the fully rendered html then csr takes over and works as normzl react app
- can be deployed to any Node.js server or even used with its own in-built HTTP server
- client-side page-based routing 
- automatic code-splitting

Each generated HTML is associated with minimal JavaScript code necessary for that page. When a page is loaded by the browser, its JavaScript code runs and makes the page fully interactive. (This process is called hydration)

Features:
* Server-side rendering by default
* Page-based client-side routing
    Pages are associated with a route based on their file name. For example, in development:
    pages/index.js              →  / route
    pages/posts/first-post.js   →  /posts/first-post route
* Server agnostic: Easy deployment to any HTTP server
* Easy customization and support for Webpack-based environment
* Automatic code splitting (faster page loading)
* built-in support for CSS (.css), Sass (.scss), Tailwind CSS
* serve static assets under the top-level public directory (img...) 
* Image Component: Resizing & optimizing images
    <img src="/images/profile.jpg" alt="Your Name" />
    
    import Image from 'next/image'
    const YourComponent = () => (
    <Image
        src="/images/profile.jpg" // Route of the image file
        height={144} // Desired size with correct aspect ratio
        width={144} // Desired size with correct aspect ratio
        alt="Your Name"
    />
    )

Folder_A
    |
    ├── components
    |
    ├── pages                 each page = a route
    |    |
    |    └── api
    |    └── cars              each page export a react component that represents a route
    |    |     └── [id].js   ← example.com/cars/:id                               ↓
    |    |     └── index.js  ← example.com/cars                                   ↓
    |    └── _app.js                                                       import { useRouter } from 'next/router'
    |    └── index.js        ← example.com/                                export default function Car() {
    └── public
    └── styled                                                             const router = useRouter()
    └── .gitignore                                                         const { name } = router.query
    └── .package.json
                                                                           return <h1>{name}</h1>

PERFORM MULTIPLE SSR STATEGIES: SSG - SSR - ISR

- SSG - STATIC GENERATION: render all pages at build time: blog...when data don't change often, 
    Marketing pages
    Blog posts
    E-commerce product listings
    Help and documentation
    Use Static Generation (with and without data) whenever possible because your page can be built once and served by CDN, which makes it much faster than having a server render the page on every request.

publish + cdn
```js
export async function getStaticProps() {   // called at build time
    // Get external data from the file system, API, DB, etc.
    const req = await.fetch('/some-api');  // fetch data
    const car = await.req.json();          // return props to component

    // pass props values to the component
    return {
        // props for your component
        props: {car}
    }
}
export default function Car({car}) {      // use props
    return <h1>{car.model}</h1>
}
```

- SSR - SERVER SIDE RENDERING: data change often, generate each page at request time
When frequently updated data, and the page content changes on every request.
Slower, but the pre-rendered page will always be up-to-date. Or you can skip pre-rendering and use client-side JavaScript to populate frequently updated data

```js
export async function getServerSideProps() {    // called at request time
    const req = await.fetch('/some-api');       // fetch data
    const car = await.req.json();               // return props to component
    return {
        // props for your component
        props: {car}
    }
}
export default function Car({car}) {      // use props
    return <h1>{car.model}</h1>
}
```

- hybrid! ISR - INCREMENTAL STATIC REGENERATION: regerate single pages in the background
```js
export async function getStaticProps() {   // called at build time
    const req = await.fetch('/some-api');       // fetch data
    const car = await.req.json();               // return props to component
    return {
        // props for your component
        props: {car},
        revalidate: 50     // REBUILD AT MOST EVERY 50 seconds
    }
}
export default function Car({car}) {      // use props
    return <h1>{car.model}</h1>
}
```


Client-Side Navigation
<a href="…"> browser load != <Link href="…"> js load
The Link component enables client-side navigation between two pages in the same Next.js app.
Client-side navigation means that the page transition happens using JavaScript, which is faster than the default navigation done by the browser.



npm install next react react-dom

```js
import { useRouter } from 'next/router'
export default function Car() {

const router = useRouter()
const { name } = router.query

return <h1>{name}</h1>
```


***package.json***
```json
{
"Scripts": {
“dev”: “next”,
“build”: “next build”,
“start”: “next start”
    }
}
```
>npm run dev

***header.js***: Custom Reusable Component
```jsx
const Header = () => (
    <div>
        <h1>This is Next.js</h1>
    </div>
)
export default Header
```

***index.js***: integrate the header
```jsx
import Header from './components/header';
const Index = () => (
    <div>
        <Header />
        <p>This is my first page rendered using Next.js :)</p>
    </div>
)
export default Index
```

***Static files***: make references to the /static assets
```js
function MyFilez() {
  return <img src="/static/some-image.png" alt="some image" />;
}
export default MyFilez;
```


## More
- https://nextjs.org/
- https://buddy.works/tutorials/creating-our-first-app-in-next-js
- https://egghead.io/projects/create-an-ecommerce-store-with-next-js-and-stripe-checkout
- https://dev.to/dabit3/magic-link-authentication-and-route-controls-with-supabase-and-next-js-leo