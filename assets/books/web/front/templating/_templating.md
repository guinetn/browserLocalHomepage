# TEMPLATING LANGUAGES 

To Use Instead of HTML
Templating languages is a great way of connecting the server side to the frontend of your site

## EJS
https://ejs.co/


```html
<% if (user) { %>
  <h2><%= user.name %></h2>
<% } %>
```

Embedded JavaScript, or, EJS, is a templating language that lets you generate HTML with plain JavaScript in between. It is a very simple language and is a good choice for students if they ever need to choose a templating language.

It uses <% %> with JavaScript in between to create dynamic websites and webpages. This isn’t the best choice for complex applications but will work for most projects.

## Handlebars
https://handlebarsjs.com/


```html
<ul class="people_list">
  {{#each people}}
    <li>{{this}}</li>
  {{/each}}
</ul
```

Handlebars is another very simple templating language without a lot of unique features. It is, however, a great way to create small projects, and I’ve actually used this one in a project once.

The syntax is easy to read and use. The language features what they call helpers, which are functions you can use with the syntax with the hashtags. These can be a loop, conditionals, or something you can create yourself. So this language does offer customization if you need it.

## Pug
https://pugjs.org/


index.pug
```html
doctype html
html
  include includes/head.pug
  body
    h1 My Site
    p Welcome to my super lame site.
    include includes/foot.pug
```

Pug is an HAML-inspired templating language. Like Python, it uses whitespace to signify nesting. It has features such as including, conditionals, and creating reusable components using Mixins. Pug templates are made in .pug files and should be parsed using a framework or programmatically.

ID and class names are written in a shorthand that is often used in, for example, jQuery. This makes it easy to read, easy to edit, and it makes for a great templating language. It even has React integration!
I have written a few articles about Pug in the past that you can check out if you want to learn more about this language. You can also read the official documentation or just try it yourself with Express.js.

## Mustache
https://mustache.github.io/mustache.5.html


```html
Hello {{name}}
You have just won {{value}} dollars!
{{#in_ca}}
Well, {{taxed_value}} dollars, after taxes.
{{/in_ca}}
```

Mustache is a minimal templating language. It calls itself a logic-less templating language, and it is. It is a templating language with a fairly minimal feature set, but it still has everything you need for creating great websites and web applications.

From official docs
The syntax is easy to read, easy to learn, and easy to compile. This little language is a good choice for everyone learning to use templating languages or for simple websites.

## React (JSX)
https://reactjs.org/

```html
function HomePage(props) {
    return (
        <div>
            <div className="alert-text">
                <span>New address saved.</span>
            </div>
            <SubmitButton />
        </div>
    )
}
```

React isn’t so much a templating language as it is a way of creating reusable components. But it uses one that is worth noting: JSX. This templating language is very similar to other templating languages and is very easy to learn.
It is very commonly used nowadays and offers a lot of functionality that other templating languages don’t have when combined with React.

It uses custom HTML-like tags as components that you can create. You can use attributes and insert JavaScript between brackets where necessary.