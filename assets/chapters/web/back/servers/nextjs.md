# Next.js

React framework that comes with native server-rendering, client-side page-based routing as well as automatic code-splitting.
Anything that is coded in PHP can be deployed and rendered on the server fairly easily.

built atop existing React libraries and comes with faster server-side rendering. The best part about Next.js is that it is fully server agnostic, and can be deployed to any Node.js server or even used with its own in-built HTTP server.

Next.js brings a good deal of features to the table, such as:

Server-side rendering by default
Page-based client-side routing
Easy deployment to any HTTP server
Easy customization and support for Webpack-based environment
Automatic code splitting (faster page loading)

npm install next react react-dom

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