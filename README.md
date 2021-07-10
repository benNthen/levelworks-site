# Level Up Works Website
Level Up Works is a coding school programme for kids aged 7-12 years old. This is a prototype website with an Enrol feature that allows the user to input the child and parent's details. The details are all stored in the PostgreSQL database container.

![image](https://user-images.githubusercontent.com/53241776/125166228-b5977480-e1ee-11eb-80a3-017b99b9eb92.png)
![image](https://user-images.githubusercontent.com/53241776/125166891-e331ed00-e1f1-11eb-9cd4-14c662510ec7.png)
![image](https://user-images.githubusercontent.com/53241776/125166896-e6c57400-e1f1-11eb-9f1f-4002af33719c.png)

The overall design of this website was adapted from [Wireframe V1 which can be found on Figma here](https://www.figma.com/file/AkCQSjLAE18VIGIWofagFY/LEVELUP-WORKS---Team-Version-File?node-id=0%3A1). 

# Using this repository

You can run the website locally using Visual Studio Code with a Docker container. 

## Prerequisites

To use this repository, you need the following installed locally:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Django](https://www.djangoproject.com/)
- A container runtime, [Docker](https://www.docker.com/).

Clone the repository and navigate to the directory:

```
git clone https://github.com/benNthen/levelworks-site.git

cd levelworks-site
```

Before you start, install the dependencies and then set the virtual environment using the following commands.

```
cd levelworks

pip install -r requirements.txt

cd - 

source virtual/Scripts/activate

cd levelworks
```
## Running the website locally using a container

To build the site in a container, run the following to build the container images:

```
docker-compose build
docker-compose up -d
```

Open up your browser to http://localhost:5432 to view the website. As you make changes to the source files, docker updates the website and forces a browser refresh simultaneously.

## Retrieving the enrolment details stored in the PostgreSQL database

The database table can be displayed in the terminal to show evidence that the submited details from the enrolment pages have been stored (Note: ensure that the docker container  images `levelupworks-app` and `levelworks_db_1` are running).

Obtain the container ID of `levelworks_db` using the `docker ps`.

Then enter the following command:
```
docker exec -it <container ID> //bin/sh 

docker-compose up -d
```

```
su - postgres 

psql

\c levelupworksdb

SELECT * FROM levelweb_student;
```
![image](https://user-images.githubusercontent.com/53241776/125165969-79174900-e1ed-11eb-81bd-cefa278cd5f2.png)
Figure N: shows an example of the output database in the terminal.

# Contributors

| <a href="https://github.com/benNthen" target="_blank">**Benedict Velasco**</a> | <a href="https://github.com/blimeyitscode" target="_blank">**Gaurang Ambani**</a>
| :---: |:---:|
| <img src="https://avatars0.githubusercontent.com/u/53241776" width="100">      | <img src="https://avatars.githubusercontent.com/u/48747837?v=4" width="100"> |
| <a href="http://github.com/BenNthen" target="_blank">`github.com/BenNthen`</a> | <a href="https://github.com/blimeyitscode" target="_blank">`github.com/blimeyitscode`</a> |
