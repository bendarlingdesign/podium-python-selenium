DEPENDENCIES / PRE-REQUISITES:
* Install python 3 (https://www.python.org/downloads/)
* Install pip (https://phoenixnap.com/kb/install-pip-windows or go here to select between OS's https://pip.pypa.io/en/stable/installation/)
* Install pytest (cmd line: pip install pytest)
* Install selenium (cmd line: pip install selenium)
* Install ChromeDriver if running MacOS (MacOS blocks by default) -> (https://timonweb.com/misc/fixing-error-chromedriver-cannot-be-opened-because-the-developer-cannot-be-verified-unable-to-launch-the-chrome-browser-on-mac-os/)
* Install Google Chrome browser.

RUNNING PYTHON SELENIUM ON LOCAL
* Add file path for Chromedriver as the driver service
* Clone user profile from Chrome directory on your local to use for local caching session
* Add Python and Chromedriver directories to Sys.PATH environment variables (https://searchitoperations.techtarget.com/answer/Manage-the-Windows-PATH-environment-variable-with-PowerShell)
* For MAC users - 
Try this if you want to run Selenium and the Chrome Webdriver on your Mac:
 1. Put Chromedriver in /usr/local/bin
 2. Open your finder.
 3. Press Command+Shift+G.
 4. Write the following: /usr/local/bin in the search bar that pops up.
 5. Drag and drop your Chromedriver into the bin folder.
*Follow the below steps to install the Selenium on macOS using pip:
  1. Install the latest Python3 in MacOS.
  2. Check if pip3 and python3 are correctly installed.
  3. Upgrade your pip to avoid errors during installation.
  4. Enter the following command to install Selenium using pip3.

* Tests
** A pytest test MUST begin with a 'test_' at the beginning of the test's name, otherwise it may not be collected as a test for execution
** A pytest has three portions: assembly (pull in parts to evaluate), action (what are you doing to those parts), assertion (what do you believe they should tell you)
** You may have multiple assertions made in a single test, but will only report a single result (pass/fail/warning, etc.) for that test. Furthermore, a single failure overrides all successes in that test case
** To run all the tests, make sure you are in the test case folder in the terminal.  Type the command, pytest and press enter.
** To execute a specific test, make sure you are in the test case folder in the terminal.  Type the command, pytest test_theTestName.py
** The terminal will display if the test(s) were a failure or 100% pass.

**Page Objects file added but not applied to the test cases.  Did not have time to impliment them or add classes.
