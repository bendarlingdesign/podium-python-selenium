DEPENDENCIES / PRE-REQUISITES:
* Install python 3 (https://www.python.org/downloads/)
* Install pip (https://phoenixnap.com/kb/install-pip-windows or go here to select between OS's https://pip.pypa.io/en/stable/installation/)
* Install pytest (cmd line: pip install pytest)
* Install selenium (cmd line: pip install selenium)
* Install ChromeDriver if running MacOS (MacOS blocks by default) -> (https://timonweb.com/misc/fixing-error-chromedriver-cannot-be-opened-because-the-developer-cannot-be-verified-unable-to-launch-the-chrome-browser-on-mac-os/)

RUNNING PYTHON SELENIUM ON LOCAL
* Add file path for Chromedriver as the driver service
* Clone user profile from Chrome directory on your local to use for local caching session
* Add Python and Chromedriver directories to Sys.PATH environment variables (https://searchitoperations.techtarget.com/answer/Manage-the-Windows-PATH-environment-variable-with-PowerShell)

* Tests
** A pytest test MUST begin with a 'test_' at the beginning of the test's name, otherwise it may not be collected as a test for execution
** A pytest has three portions: assembly (pull in parts to evaluate), action (what are you doing to those parts), assertion (what do you believe they should tell you)
** You may have multiple assertions made in a single test, but will only report a single result (pass/fail/warning, etc.) for that test. Furthermore, a single failure overrides all successes in that test case
** To run all the tests, make sure you are in the test case folder in the terminal.  Type the command, pytest and press enter.
** To execute a specific test, make sure you are in the test case folder in the terminal.  Type the command, pytest test_theTestName.py
** The terminal will display if the test(s) were a failure or 100% pass.