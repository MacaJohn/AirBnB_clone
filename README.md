# AirBnB_clone
This is the clone of the popular Airbnb web application for booking houses and hotels anywhere in the world.

The process of building this application involves several stages. The first stage is building the console application.

The console application is a command interpreter that will allow the software engineer/administrator to interact and manage the storage engine of the application. This storage engine could be a file or a database. We will start by persisting data in a file and then move on to a database. Thus, the engineer/admins will be able to:
- create data models
- manage (create, update, destroy, etc) object via the console/command interpreter
- store and persist objects to a file (JSON file)

The main aim is to manipulate a powerful storage system. The storage system will give a abstraction between "My objects" and "How they are stored and persisted". This means, there will be no need to pay attention to how objects are stored when the frontend and RestAPI are built later.

The abstraction will alos allow changing the type of storage easily without updating all of the codebase.

The console will also help in validating the data models implemented with file storage so that it can be finalized with a SQL database.
