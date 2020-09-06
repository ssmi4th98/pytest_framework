Start by pip installing pytest.

You can run by using either pytest or py.test\n

The file that contains the test must have the work "test" in it and all functions that are test must start with the prefix "test"\n

The pytest command can be run just pointing to one test,e.g., pytest cal_test.py or run against a directory pytest test/

In a result set for failures: test_exception.py .FF  is show where the "." is a pass and the FF shows 2 failures.\n

To execute just one test in a multitest, use the pytest command with the name of the test framework and two colons followed by the name of the test, e.g., pytest test_multi_simple.py::test_string\n

A "-v" can be added to any pytest command for verbose\n
This shows test are run from top to bottom.

To run multiple tests, one can:\n
    1. use the "-k" flag to use keywords, e.g., pytest test_multi_simple.py -v -k "add"
    2. -k takes multiple expressions, e.g., "add and string" or "add or string"
    3. -x flag stops the tests from running if there is an error.
    4. -x flag has a --maxfail option that allows a max number of tests to fail before stopping tests,e.g, --maxfail=2
    5. to stop failure info, you can use the "--tb" (traceback) flag set to no, e.g., --tb=no (can use long, short,auto,line,native)
    6. decorators can be used to mark tests, run test with "-m" flag as the marker and declare the marker (some markers are registered, e.g., skip)
        "skip" also takes arguments "-r" flag for a short summary that takes an argument "s" to include reason for skip (-rs)
        -r flag can also take the argument "f" for failure details.
        other flags include -q for quiet; -v verbose
        
Pytest can be run in debug mode using the --pdb flag in console. Once a test has been found as bad, you can debug it in console and then hit "c" to continue along the test suite.\n
You can run pytest with the --trace flag to stop at every test with the debugger. use "c" to go to next test.



    
    
