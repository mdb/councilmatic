Councilmatic!
=============
Philly City Council Legislative Subscription Service.

Contact Us
----------
- Join the mailing list at https://groups.google.com/group/councilmatic/
- Find us on irc.freenode.net in the #councilmatic room

Getting Started
---------------
First check out the project code.

    $ git clone git://github.com/codeforamerica/councilmatic.git

To work on your own instance of Councilmatic, you should first get Python
installed. Follow the instructions for doing so on your platform.

In addition, we recommend setting up a virtual environment for working with any
project, so that you can manage your project-specific dependencies.

    $ virtualenv councilmatic_env --no-site-packages
    $ source councilmatic_env/bin/activate
    
Next, install the requirements for Councilmatic (we recommend working in a
virtual environment, but it's not strictly necessary).

    $ pip install -r requirements.txt

Set up the project database and populate it with city council data (when the
syncdb command prompts you to create an administrative user, go ahead and do
so). There is a lot of data to be loaded, so downloading it all may take a
while. If you're familiar with this routine, you can skip that step.

    $ cd councilmatic
    $ python manage.py syncdb
    $ python manage.py migrate
    $ python manage.py loadlegfiles

Finally, to run the server:

    $ python manage.py runserver

Now, check that everything is working by browsing to http://localhost:8000/. Now
browse to http://localhost:8000/admin and enter the admin username and password
you supplied and you should have access to all of the legislative files!

Compass
-------

Councilmatic utilizes [Compass](http://compass-style.org/) as its CSS authoring framework.

To install Compass:
    
    $ gem install compass

To compile CSS:

    $ compass compile /path/to/councilmatic/static/sketch

Interested in Contributing?
---------------------------

See [Pivotal Tracker](https://www.pivotaltracker.com/projects/258817) for a list of outstanding issues.

Copyright
---------
Copyright (c) 2010 Code for America Laboratories
See [LICENSE](https://github.com/cfalabs/open311/blob/master/LICENSE.mkd) for details.

[![Code for America Tracker](http://stats.codeforamerica.org/codeforamerica/philly_legislative.png)](http://stats.codeforamerica.org/projects/philly_legislative)
