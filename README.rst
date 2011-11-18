A very simple cookie dropping WSGI app and some tests
to illustrate a problem with multiple cookies and saucelabs.

To use::

    git clone git@github.com:scooterXL/Sauce-Cookie-Test.git
    cd Sauce-Cookie-Test
    virtualenv .
    . bin/activate
    bin/python setup.py develop
    bin/runapp


In a second shell::
    
    cd Sauce-Cookie-Test
    bin/python tests.py


Note: You'll need to be running both the SauceConnect proxy
and a SeleniumServer process.
