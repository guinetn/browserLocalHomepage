# Blazor

https://dotnet.microsoft.com/apps/aspnet/web-apps/blazor

For many years, Javascript rules the dom scripting to manipulate client-side UI

- Can build entire stack in .NET, including UI
- Web Assembly: Allows compiled languages to be interpreted client-side (fully supported across all browsers now)
- Create .NET applications that run completely inside of the browser. The output of a Blazor WASM project are all static files. You can deploy these applications to various static site hosts like GitHub Pages.

## COMMANDS
	dotnet new blazorserver -o BlazorApp --no-https
	cd BlazorApp
	dotnet new razorcomponent -n Todo -o Pages
	dotnet run
	http://localhost:5000

## JavaScript interoperability API

Invoke JavaScript functions from .NET and .NET methods from JavaScript
Microsoft.JSInterop namespace
https://swimburger.net/blog/dotnet/communicating-between-dotnet-and-javascript-in-blazor-with-in-browser-samples

IJSRuntime   
	allows you to call JavaScript functions from .NET in Blazor, but only functions that are available on the global window object. 

	@inject IJSRuntime JS
	@code {
		protected override async Task OnInitializedAsync()
		{
			string name = await JS.InvokeAsync<string>("prompt", "What is your name?");
			await JS.InvokeVoidAsync("alert", $"Hello {name}!");
		}
	}

#### Articles
- https://developer.okta.com/blog/2019/10/16/csharp-blazor-authentication
- [Deploy Blazor WebAssembly to GitHub Pages](https://www.youtube.com/watch?v=nNxII6jvPvQ&feature=youtu.be)
- [](https://swimburger.net/blog/dotnetcore)
- https://medium.com/younited-tech-blog/unit-test-a-blazor-component-729eec4eab01
- https://medium.com/younited-tech-blog/localization-of-a-blazor-component-2178aa855ded
- https://medium.com/@ankitsharmablog/how-to-perform-crud-operations-using-blazor-and-google-cloud-firestore-52890b06e2f8
- https://andrewlock.net/using-source-generators-to-generate-a-nav-component-in-a-blazor-app/