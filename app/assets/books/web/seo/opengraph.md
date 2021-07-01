# Open Graph

http://ogp.me/

Open Graph is a set of standards for websites to be able to declare metadata that other platforms can pick out, to get a TL;DR of the page. You’d declare something like this in your HTML:

<meta property="og:image" content="https://www.rd.com/wp-content/uploads/2020/01/GettyImages-454238885-scaled.jpg" />
https://github.blog/2021-06-22-framework-building-open-graph-images/

When a crawler (like Twitter’s crawling bot, which activates any time you share a link on Twitter) looks at your page, it’ll see those meta tags and grab the image. Then, when that platform shows a preview of your website, it’ll use the information it found. Twitter is one example, but virtually all social platforms use Open Graph to unfurl rich previews for links.


# The Open Graph protocol
	enables any web page to become a rich object in a social graph
	 was originally created at Facebook and is inspired by Dublin Core, link-rel canonical, Microformats, and RDFa.
	 Tags giving to social networks (Facebook, Google +, Twitter, Linked in...) informations about the page

# Basic Metadata

	The four required properties for every page are:
		og:title 	The title of your object as it should appear within the graph, e.g., "The Rock".
		og:type 	The type of your object, e.g., "video.movie". Depending on the type you specify, other properties may also be required.
		og:image 	An image URL which should represent your object within the graph.
		og:url 		The canonical URL of your object that will be used as its permanent ID in the graph, e.g., "http://www.imdb.com/title/tt0117500/".


	<html prefix="og: http://ogp.me/ns#">
	<head>
	<title>The Rock (1996)</title>
	<meta property="og:title" content="The Rock" />
	<meta property="og:type" content="video.movie" />
	<meta property="og:url" content="http://www.imdb.com/title/tt0117500/" />
	<meta property="og:image" content="http://ia.media-imdb.com/images/rock.jpg" />
	...
	</head>
	...
	</html>


# Optional Metadata

og:audio - A URL to an audio file to accompany this object.
og:description - A one to two sentence description of your object.
og:determiner - The word that appears before this object´s title in a sentence. An enum of (a, an, the, "", auto). If auto is chosen, the consumer of your data should chose between "a" or "an". Default is "" (blank).
og:locale - The locale these tags are marked up in. Of the format language_TERRITORY. Default is en_US.
og:locale:alternate - An array of other locales this page is available in.
og:site_name - If your object is part of a larger web site, the name which should be displayed for the overall site. e.g., "IMDb".
og:video - A URL to a video file that complements this object.
# For example (line-break solely for display purposes):

<meta property="og:audio" content="http://example.com/bond/theme.mp3" />
<meta property="og:description"
  content="Sean Connery found fame and fortune as the
           suave, sophisticated British agent, James Bond." />
<meta property="og:determiner" content="the" />
<meta property="og:locale" content="en_GB" />
<meta property="og:locale:alternate" content="fr_FR" />
<meta property="og:locale:alternate" content="es_ES" />
<meta property="og:site_name" content="IMDb" />
<meta property="og:video" content="http://example.com/bond/trailer.swf" />



