# .NET MAUI (.NET 6)

**Maui (Multi-platform App User Interface)**
share code across desktop and mobile platforms
Write .NET apps with the same codebase (same libraries) for iOS, Android, Windows, macOS. 
Evolution of Xamarin.Forms, extended from mobile to desktop scenarios with UI controls rebuilt from the ground up for performance and extensibility
Goodbye Xamarin.Forms, Hello .NET MAUI

https://github.com/dotnet/maui
	While Xamarin.Forms continues to be actively developed to meet customer needs today, we are proposing evolutionary changes based on some early customer research of what would be most beneficial.
	Active development is happening today to build Android and iOS SDKs against the next version of .NET. Samples may be found here.

2011: Xamarin
	.NET and C# cross-platform applications on iOS, macOs, Android, Windows
	Since developing with Xamarin was all based on the same language, you could share your code across all supported platforms, and thus reuse quite a bit.
	The last piece that wasn’t reusable was the user interface (UI) of each platform. 

2014: Xamarin.Forms 	
	abstraction layer above the different platforms’ UI concepts. By the means of C# or XAML, you
	were now able to declare a Button, and Xamarin.Forms would then know how to render that button on iOS,
	and that same button on Android as well. 
	Xamarin.Forms Internals: Renderers
		Each VisualElement, which is basically each element that has a visual representation (so pages and
		controls mostly), has a renderer. For instance, if we look at the Button again, Button is the abstract
		Xamarin.Forms component which will be translated into a UIButton for iOS and an Android.Button on
		Android.
		To do this translation, Forms uses a renderer. In this case, the ButtonRenderer. Inside of that renderer, two
		things happen basically:

2016: Xamarin was acquired by Microsoft
	https://docs.microsoft.com/fr-fr/xamarin/get-started/what-is-xamarin

2020:  Xamarin.Forms will evolve into something called .NET MAUI. 	
	Everything that is in Forms today, will be available in .NET MAUI



# Support for Multiple Design Patterns
	Xamarin.Forms, and other Microsoft products for that matter, have mostly been designed to work with the
	Model-View-ViewModel (MVVM) pattern.
	With .NET MAUI, this will change.
	While MVVM will still be supported (again, nothing is taken away), because of the new renderer
	architecture, other patterns can be implemented now.
	
	For instance, the popular Model View Update (MVU) pattern will now also be implemented. 
	If you are curious what that looks like, have a look at the code below.
	
	readonly State count = 0;
	[Body]
	View body() => new StackLayout
	{
	 new Label("Welcome to .NET MAUI!"),
	 new Button(
	 () => $"You clicked {count} times.",
	 () => count.Value ++)
	 )
	};	





## more
- https://github.com/dotnet/maui
- https://www.youtube.com/watch?v=hoC5FIblKz8&t=899s
- https://devblogs.microsoft.com/xamarin/the-new-net-multi-platform-app-ui-maui/?WT.mc_id=dotnet-00000-cephilli