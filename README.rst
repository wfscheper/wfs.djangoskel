Introduction
============

wfs.djangoskel is a fork of the fez.djangoskel project.

fez.djangoskelprovides paster templates for creating Django
projects and applications as eggs. Five templates are currently 
provided.

This fork rewrites the django_project template to provide a django
project that is better configured for deployment (or at least I think
so). 


Usage
=====

Install wfs.djangoskel using easy_install. This should also install
paster as a dependency. You should then be able to see five new
templates available::

  $ paster create --list-templates
  Available templates:
    basic_package:             A basic setuptools-enabled package
    django_app:                Template for a basic Django reusable application
    django_buildout:           A plain Django buildout    
    django_namespace_app:      Template for a namespaced Django reusable application
    django_namespace_project:  Template for a namespaced Django project
    django_project:            Template for a Django project
    paste_deploy:              A web application deployed through paste.deploy

You may create an initial Django buildout using the django_buildout template::

  paster create -t django_buildout
  
This will create bootstrap.py, buildout.cfg and devel.cfg files. You should edit
the buildout files to your needs.
  
Create a Django project using the django_project template::

  paster create -t django_project

Answer the questions that paster asks, and it will create a full
Django project with a template settings file and urls.py.

Applications are created in a similar way::

  paster create -t django_app

Projects created with these templates do not have namespace packages: that is,
you will find a directory created with the name of the package you specified
which contains all the usual egg stuff, and the module will be under that 
directory.

If you wish to create a namespaced package (similar, for example, to this 
package: fez.djangoskel) then you should use the django_namespace_app and
django_namespace_project templates. Both work in the same way.

When creating eggs based on django_namespace_app or django_namespace_project,
paster will ask you for three pieces of information:

- Project name
  - This should be the full dotted name of the package eg. foo.bar
- Namespace package
  - This is the top-level namespace package, eg. foo
- Package name
  - This is the name of the lower-level module, eg. bar
  
This will give you a directory layout like this::

  ./foo.bar
    /foo
        /bar
          
Your code will most likely be going under bar; this is where models.py, urls.py
etc. will be created.


Difference from Django's own templates
======================================

Django provides its own 'template' app and project generation. 
Why use these templates?

- The primary motivation is that the projects and apps generated
  by these templates are eggs. This means that they can be uploaded
  to PyPI, and other developers will be able to easy_install them.
  
- These templates all provide skeleton documentation in the form
  of HISTORY.txt and README.txt files.
  
- The application template also provides a lot more plumbing to get 
  you started writing tests: a tests module, test settings (which can
  be invoked using python manage.py test --settings=project.settings)
  and test URLConfs and settings that the test client can use.
  
Difference from fez.djangoskel templates
========================================

fez.djangoskel focuses on project deployment through python eggs, and
does not provide any web server configuration.
Why use these templates?

- Builtin deployment via fabric, rsync and virtualenv

- builtin deployment options:
  - apache + apache mod_wsgi
  - nginx + apache mod_wsgi
  - nginx + gunicorn

- Separate configurations for staging and production
