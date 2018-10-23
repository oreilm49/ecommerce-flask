# Flask Ecommerce Project
A simple ecommerce web application built using the Flask framework for Python web development.
This project is part of the
[Udacity Full Stack Web Developer Nanodegree](https://eu.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

<b>Built with</b>
- Python 3
- Flask
- sqlite

## Usage
<b>PreRequisites</b>
- Python3
- Flask
- Vagrant
- VirtualBox
- sqlite

<b>Setup</b>
1. Clone this repo
    ~~~~
    git clone https://github.com/oreilm49/ecommerce-flask
    ~~~~
2. [Install vagrant](https://www.vagrantup.com/docs/installation/)
3. [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)
4. [Download](https://github.com/udacity/fullstack-nanodegree-vm) the vagrant set up files. Copy the Vagrantfile into the project directory.
5. Ensure that the Vagrantfile package installations match the below:
    ~~~~
    apt-get -qqy install python3 python3-pip
    pip3 install --upgrade pip
    pip3 install flask packaging oauth2client redis passlib flask-httpauth
    pip3 install sqlalchemy flask-sqlalchemy psycopg2-binary bleach requests
    pip install SQLAlchemy-JSONField

    apt-get -qqy install python python-pip
    pip2 install --upgrade pip
    pip2 install flask packaging oauth2client redis passlib flask-httpauth
    pip2 install sqlalchemy flask-sqlalchemy psycopg2-binary bleach requests
    pip install oauth2client
    pip install requests
    pip install httplib2
    ~~~~
6. Add the below port config to the Vagrantfile and save:
    ~~~~
    config.vm.network "forwarded_port", guest: 6500, host: 6500, host_ip: "127.0.0.1"
    ~~~~
<b>Run</b>
1. Launch Vagrant by & log in by running
    ~~~~
    > vagrant up
    > vagrant ssh
    ~~~~
2. Initialize database by running the following command in the cli
    ~~~~
    python database.py
    ~~~~
3. Add data to the database
    ~~~~
    python lotsofproducts.py
    ~~~~
4. Visit http://localhost:5000 in the browser to view the live application.
## Under the hood
<b>Database</b>

There are four tables in the database
- Global: All global catalogs. These are used as the navlinks in the homepage and can only be updated by lotsofproduct.py
- Catalogs: These are sub categories of the Global catalogs and facilitate swift navigation of a large list of products.
- Products: All the products displayed by the application.
- Users: All registered users.

<b>API</b>

There are 3 JSON endpoints to enable external applications access to the app data:
1. Products JSON. Access all products within a catalog by specifying the "catalog_id" as an integer in the url:
    ~~~~
    /catalog/<int:catalog_id>/products/JSON
    ~~~~
2. Product JSON. Access a specific product by specifying the "id" as an integer in the url:
    ~~~~
    /product/<int:id>/JSON
    ~~~~
3. Catalogs JSON. Access all catalogs by calling the below url:
    ~~~~
    /catalogs/JSON
    ~~~~


