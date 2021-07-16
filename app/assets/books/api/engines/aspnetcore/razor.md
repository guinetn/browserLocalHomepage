## RAZOR

- https://www.ezzylearning.net/tutorial/a-developers-guide-to-asp-net-core-razor-pages
- https://www.ezzylearning.net/tutorial/a-beginners-guide-to-blazor-components


ASP.NET Core MVC views use the Razor view engine to render views. 
Razor is a compact, expressive and fluid template markup language for defining views using embedded C# code. Razor is used to dynamically generate web content on the server. You can cleanly mix server code with client side content and code.
https://docs.microsoft.com/fr-fr/aspnet/core/razor-pages/?view=aspnetcore-3.1&tabs=visual-studio
https://docs.microsoft.com/fr-fr/aspnet/core/mvc/views/razor?view=aspnetcore-3.1

<h1>Hello, world!</h1>
<h2>The time on the server is @DateTime.Now</h2>

<p>Last week this time: @(DateTime.Now - TimeSpan.FromDays(7))</p>

<ul>
    @for (int i = 0; i < 5; i++) {
        <li>List item @i</li>
    }
</ul>

@model IEnumerable<Product>
<ul>
    @foreach (Product p in Model)
    {
        <li>@p.Name</li>
    }
</ul>


## RAZOR SYNTAX

		@* Razor comments *@
		<!-- --> 	HTML client-side comments: prevent a browser from parsing/running/displaying the HTML content within it
		<%-- --%>	ASP.NET Web Forms server-side comment syntax
		 			compiler completely ignore everything within the <%-- --%> blocks at parse time, and removes the content completely when assembling the page



											   ____ '@model StrongModelType'  . model directive at the top of your Razor view file
											  |								  . clean/concise way to reference strongly-typed models from view files
											  |								  . Defines the model view that we can refer to in the rest of the view
											  |								  . We can refer to methods, fields, and properties through the '@Model' property
										      v 														|
	'@': a razor statement 					@model Razor.Models.Product									|
		(server-side code)																				|
	    									@* Comments *@												|
																										|
	'@{ ...block code... }'   		        @{															|
	    										// Comments 											|
											    /* Comments. Get numbers from 1 - 10*/					|
	ViewBag:  A dynamic container filled        ViewBag.Title = "Index";								|
	on the fly for simple database	         }															|		STRONGLY-TYPED VIEW
	A 'model' to pass to the view            															|		@model IEnumerable<MySite.Models.Products>   <---- At the top of the vi
								            <h2>Index</h2>												|		@foreach(var p in Model)
	'@@' to render a @ symbol		 		My Email is aaa@@bbb.com 									|		{
								            <h2>Name: @Model.Name</h2>									|		  <div>Price: @p.Price</div>
								            Time view rendered: @DateTime.Now.ToShortTimeString()		|		}
																										|
	@if							            @if (Model.Category == "Watersports")				________|
								            {     <p>@Model.Category <b>Splash!</b> </p> }

	@: one line of text (and not code) 			@: PART 2 OF THE PAGE

	@@: to include text and not code inside a code block that doesn’t start with an HTML element
		tells Razor to treat the line as though it begins with an HTML element

								            @if (@Model.Category == "Watersports") {
								                @:Category: @Model.Category <b>Splash!</b>
								            }

								            <br />

								            Use the "text" element to include a number of lines, none of which start with HTML elements:<br />
								            @if (@Model.Category == "Watersports") {
	<text> many lines of text (not code)		<text>
		   where code ends&begins again            Category: @Model.Category <b>Splash!</b>
           in block code  		                    <pre>
								                        Row, row, row your boat,
								                        Gently down the stream...
								                    </pre>
								                </text>
								                <text>@(number * 10) * 10 = @(number * 10)&nbsp;</text>
								            }

								            <br />
								            Open a code block with @{ and closing it with @}<br />
								            @{
								                if (Model.Category == "Watersports") {
								                    @:Category: @Model.Category <b>Splash!</b>
								                }
								                if (Model.Price > 10) {
								                    <h5>Pricey!</h5>
								                }
								            }

## Explicit nugget value: 					@(expression)

	Property Access
											@Model.Price * 1.2
											@(Model.Price * 1.2)
											@DateTime.Now.Seconds		// multiple levels deep
											<img src="img/@(p.productname).jpg">

	Array/Collection Indexing:
											@products[0].UnitPrice

	Calling Methods:
											@products.Count()
											@products.Sum(p=>p.UnitPrice)

	Razor Delegate						    @{
										      Func<dynamic, object> b = @<strong>@item</strong>;
										    }
										    @b("Bold this")

	Loop rendering 							@{
											    var numbers = Enumerable.Range(1, 10); //Get numbers from 1 - 10
											    foreach(var number in numbers)
											    {
											           <span>@(number * 10)&nbsp;</span>
											    }
											}

	Combining Text and markup				@foreach(var item in items)
											{
											  <span>@item.Prop</span>
											}

	@Html.Raw()  render text without html encoding

											@Html.Raw(".......")
											var allFaculties = @Html.Raw(Json.Encode(ViewData["Faculties"]));

	Conditional attributes
											@{ string foo = null; string bar = “bar” }
											<div id=”foo” class=”@foo @bar”>
												|
												 -----> <div id=”foo” class=”bar”>

	Easy url resolution
			Razor v1   	<a href="@Url.Content("~/MySite/")@Foo/Bar/@Baz">Something!</a>
			Razor v2   	<a href="~/MySite/@Foo/Bar/@Baz">Something!</a>
					 	Automatic ~ for easy url resolution: goodbye @href/@url.content...!!
		 				Any attribute value startsing by "~/" will be replaced with
		 						. @Url.Content 		(in MVC)
		 						. a call to @Href 	(in WebPages)

	@Styles.Render("~/content/css")
	@Scripts.Render("~/bundles/modernizr")


	Dynamic Views
		can display more than one model class

	http://www.mikesdotnetting.com/Article/209/Consuming-Feeds-And-Web-Services-In-Razor-Web-Pages
