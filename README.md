# django-locator

An easy to integrate store locator plugin for Django.


## Setup

 1. Run `pip install django-locator`.
 2. In `settings.py` add `locator` to the `INSTALLED_APPS`.
 3. In `urls.py` add `url(r'^locator/', include('locator.urls', namespace='locator'))` to the `urlpatterns`.
 4. Run `manage.py syncdb`.


## Using the template tag

django-locator is easy to include in your templates, you just need to do two
things:

 1. Include the CSS and JS files on the page you're wanting to use django-locator.
 2. Load the django-locator template tag and insert it where you want it to show up.

### Including the CSS and JS files

There is one CSS file, place this line in your HTML header with the rest of your
CSS imports:

    <link rel="stylesheet" href="{{ STATIC_URL }}locator/css/map.css" />

The JS is slightly more complex, first, make sure you don't already have jQuery,
if you don't have jQuery then add this to the bottom of your HTML file but still
inside your `<body></body>` tag:

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>

Once you have jQuery you now need the Google Maps API JS files:

    <script src="//maps.google.com/maps/api/js?sensor=false"></script>

Close to the end! Now include the store locator JS file below both of these
imports:

    <script src="{{ STATIC_URL }}locator/js/jquery.storelocator.js"></script>

Lastly we need to initialize the store locator script by putting this at the
very bottom below the imports we just made:

    <script>
        $(function() {
            $('#map-container').storeLocator({
                'jsonData': true,
                'dataLocation': '{% url locator:locations %}',
            });
        });
    </script>

### Loading the template tag

Once you have the CSS and JS included the template tag is easy, add
`{% load locator %}` to the top of your template and then put `{% locator %}`
where you want the locator to show up on your page.


## Customizing

You can of course override everything in my CSS file easily by importing your
own CSS file below it or copying my CSS file, making changes to it and then
importing your changed CSS file instead of my own.

Along with the basic CSS customizing see [Bjorn's blog post][0] about how you can
modify our JavaScript initilizer to further customize your experience.


## Notes

I include an `initial_data.json` fixture to load in a few example items, you can
easily mass delete them on the admin interface.

To access my "test" template you can append `/locator/` to your base URL. All of
the locations are pulled via JSON from the URL `/locator/locations/` if you want
to use this data for anything else.


## Credits

Give all your thanks to [Bjorn][1] who created the [jQuery plugin][0] we make extensive
use of in this app.


## License (Simplified BSD)

Copyright (c) Isaac Bythewood  
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


[0]: http://www.bjornblog.com/web/jquery-store-locator-plugin
[1]: http://www.bjornblog.com/
