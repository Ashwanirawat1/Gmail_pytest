A. selenium :- Steps to install selenium :-  
	     1. open terminal in pycharm.
	     2. type the command "pip install selenium"

B. Pytest  :- Steps to install pytest :-
	     1. Open the terminal in pycharm.
	     2. type the command  "pip install pytest" 


D. HTML report :-
	     1. Open the terminal in pycharm.
	     2. type the command  "pip install pytest-html"




FOR EXECUTING PERTICULAR SCRIPT :- pytest test_script/test_MODULENAME/test_FILENAME.py
Example :-   If we want to execute the test_valid_login.py script.
                                 pytest -vs Test_script/test_valid_login.py



FOR EXECUTING SCRIPTS (with html report) :- pytest Test_script/test_valid_login.py --html="Reports/report.html"
		It will create a html file with name "report.html" inside the Reports folder.
	
FOR EXECUTING ONLY THE FAILED TEST CASES :- pytest --last-failed
It will execute only failed test cases.
