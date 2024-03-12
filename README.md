AirBnB
Project Description
This is the first step towards building a full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

This project is part of the AirBnB clone project, which aims to create a command-line interpreter (CLI) to manage AirBnB objects. The CLI provides users with a text-based interface to interact with the system, allowing them to perform various tasks and operations such as creating, updating, and deleting objects such as Users, States, Cities, and Places. This serves as a crucial foundation for the subsequent development of a full-fledged web application.

Command Interpreter
The command interpreter, also known as the console or shell, is a program that allows users to interact with the AirBnB system using text-based commands. It provides a command-line interface where users can input commands to perform specific tasks or operations on AirBnB objects.

How To Run The Command Line Interpreter
To start the AirBnB clone command interpreter, Run the command ./console.py .

Using the Interpreter
Once the command interpreter is running, you can use various commands to manage AirBnB objects. The available commands include:

create: Create a new object.

show: Display details of a specific object.

destroy: Delete a specified object.

all: List all available objects.

update: Update attributes of a specified object.

Examples of Usage
create: Create a new object (e.g., User, State, City, Place).

(hbnb) create User

show: Retrieve information about a specific object.

(hbnb) show User 1234-5678

destroy: Delete a specified object.

(hbnb) destroy User 1234-5678

all: Display all instances of a specific class or all objects.

(hbnb) all

(hbnb) all User

update: Update attributes of a given object.

(hbnb) update User 1234-5678 name "John Doe"

quit/EOF: Exit the command interpreter.

(hbnb) quit
