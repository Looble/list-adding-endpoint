# Adam Cohen Coding Test

This project uses django and django rest framework to make an API endpoint that returns the sum of a list of numbers.
Assumptions that have been made throughout this project have been listed in Assumptions.py

## Installation

Please note this repository requires Python 3  
1. Clone the repository from github to the location of your choice.  
2. Using your command line navigate to the folder location.  
3. You may wish to initialise a python virtual environment. Instructions for doing so can be found [here](https://docs.python.org/3/library/venv.html)  
4. Run the command:  
```
pip install -r requirements.txt
```  
which will install both django and django rest framework.

## Usage

In your command line, run the command:  
```
python manage.py runserver 5000
```  
then navigate to [localhost:5000/total](localhost:5000/total).  
If prompted for a login, the details are:  
    Username: admin  
    Password: password123

An example of the expected output is stored in the file *api.total LIST.json*

## Testing

Tests are stored in the file *coding\_test/number_sum/tests.py*
To run the tests run command:  
```
python manage.py test
```  
in the command line. This will run the test suite.
