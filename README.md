![65f4a1dd9c51265f49d0](https://github.com/Teheremiti/holbertonschool-AirBnB_clone/assets/120781178/cf61344a-c330-4d1b-8e03-d1873c4207e0)

# :hotel: AirBnB Clone - The Console

This repository contains all the packages and modules for a [command interpreter](https://www.tutorialspoint.com/what-is-the-purpose-of-the-command-interpreter#:~:text=A%20command%20interpreter%20allows%20the,interfaces%20and%20menu%2Ddriven%20interfaces.) to manage the AirBnB objects.
This is the first step towards building a first full web application: the **AirBnB clone**. This first step is very important because it will be used in all other following projects: HTML/CSS templating, database storage, API, front-end integration…

## Installation

1.  Clone the repository from [https://github.com/Teheremiti/holbertonschool-AirBnB_clone.git](https://github.com/Teheremiti/holbertonschool-AirBnB_clone.git)
2.  Make sure the "console.py" file is executable on your machine. If not, run `chmod +x console.py` from within the repo.
3.  Run the program using `./console.py`

## Usage

The console will display a prompt ("(hbnb) ") when it is ready to accept commands. Simply enter the command you wish to execute and press Enter. The console will then execute the command and display the output.

### Examples

Here are some examples of how to use the console :

		AirBnB_clone$ ./console.py
		(hbnb) 
Run `help` to see the list of existing commands , and `help` followed by a command to have some information on it :

		(hbnb) help
		
		Documented commands (type help <topic>):
		========================================
		EOF  all  create  destroy  help  quit  show  update
		
		(hbnb) help create
		Command to create a new instance of BaseModel.
		Automatically saves it to the JSON file and prints
		the id.
		
		Args:
			class_name (str): Name of the class to create
			an instance of

		(hbnb) quit
		AirBnB_clone$

## Modules

Here is a brief overview of the modules in this repository:

 - [console.py](https://github.com/Teheremiti/holbertonschool-AirBnB_clone/blob/master/console.py "console.py") : Contains the source code for the command interpreter
 - [models/base_model.py](https://github.com/Teheremiti/holbertonschool-AirBnB_clone/blob/master/models/base_model.py) : Defines the BaseModel class, which is the base class for all AirBnB objects. All other classes in this repository inherit from BaseModel.
 - [models/user.py](https://github.com/Teheremiti/holbertonschool-AirBnB_clone/blob/master/models/user.py) : Has the User class which keeps user's informations as attributes.
 - [models/state.py](https://github.com/Teheremiti/holbertonschool-AirBnB_clone/blob/master/models/state.py) : Defines the State class
 - [models/city.py](https://github.com/Teheremiti/holbertonschool-AirBnB_clone/blob/master/models/city.py) : Defines the City class
 - [models/amenity.py](https://github.com/Teheremiti/holbertonschool-AirBnB_clone/blob/master/models/amenity.py) : Defines the Amenity class
 - [models/place.py](https://github.com/Teheremiti/holbertonschool-AirBnB_clone/blob/master/models/place.py) : Defines the Place class
 - [models/review.py](https://github.com/Teheremiti/holbertonschool-AirBnB_clone/blob/master/models/review.py) : Defines the Review class
<br>

 - [models/engine/file_storage.py](https://github.com/Teheremiti/holbertonschool-AirBnB_clone/blob/master/models/engine/file_storage.py) : Contains the FileStorage class. This is the only class in the repository that does not inherit from BaseModel. It keeps memory of all the objects and the actions taken on them.
<br>

 - [tests](https://github.com/Teheremiti/holbertonschool-AirBnB_clone/tree/master/tests) : This folder contains all the test modules that were realized to ensure the console works correctly

## Testing

		AirBnB_clone$ python3 -m unittest discover tests
		...................
		----------------------------------------------------------------------
		Ran 19 tests in 0.098s
		OK
		AirBnB_clone$ 

## AUTHORS

This console was written by **Teheremiti Tuiaiho**
