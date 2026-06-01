# AirBnB Clone - The Console

## Description
This project is the first step toward building a full web application:
the **AirBnB clone**. It begins with a command interpreter (console) that
manages AirBnB objects such as User, State, City, Place, and more.

The console allows you to:
- Create new objects (e.g., a new User or Place)
- Retrieve objects from a file
- Perform operations on objects (count, compute stats, etc.)
- Update object attributes
- Destroy objects

This first step lays the foundation for HTML/CSS templating, database
storage, API, and front-end integration in later phases of the project.

## Storage
All classes are handled by a `Storage` engine (`FileStorage`) which uses
JSON serialization/deserialization:

`Instance <-> Dictionary <-> JSON string <-> file`

## How to Start
The console is launched by running the `console.py` file: