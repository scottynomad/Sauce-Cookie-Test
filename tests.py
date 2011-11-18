from selenium import selenium
import unittest

# HTTP/1.0 200 OK
# Content-Type: text/html; charset=utf-8
# Content-Length: 153
# Set-Cookie: ccc0=stuff; Path=/
# Set-Cookie: ccc1=stuff; Path=/
# Set-Cookie: ccc2=stuff; Path=/
# Server: Werkzeug/0.8.1 Python/2.7.2
# Date: Fri, 18 Nov 2011 14:55:12 GMT
# 
# 
#         <html>
#             <head><title>Cookie Test</title></head>
#             <body>Dropped cookies under name <em>ccc</em></body>
#         </html>
# 

class CookieTest(object):

    def test_cookies(self):
        for N in range(1,4):
            browser = self.browser
            browser.delete_all_visible_cookies()
            browser.open("/test/%s" % N)
            for n in range(N):
                # Note that when this fails it seems to be last in wins
                self.assertTrue(browser.is_cookie_present('test%d' % n),
                                "Missing cookie test%d" % n)


class Sauce(unittest.TestCase, CookieTest):

    def setUp(self):
        self.browser = selenium(
            '127.0.0.1',
            4445,
            """{\
                "username": "swidealist",\
                "access-key": "d87a3a3d-4b8d-45a1-8f0b-c005926b55ed",\
                "os": "Windows 2003",\
                "browser": "firefox",\
                "browser-version": "7",\
                "name": "Multiple Cookie Bug Test." \
               }""",
               'http://127.0.0.1:5000')
        self.browser.start()
        self.browser.set_timeout(90000)

    def tearDown(self):
        self.browser.stop()


class Localhost(unittest.TestCase, CookieTest):

    def setUp(self):
        self.browser = selenium(
            '127.0.0.1',
            4444,
            '*firefox',
            'http://127.0.0.1:5000')
        self.browser.start()
        self.browser.set_timeout(90000)

    def tearDown(self):
        self.browser.stop()


if __name__ == "__main__":
    unittest.main()
