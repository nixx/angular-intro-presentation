:title: JavaScript intro

*JavaScript*
=========================
HANDS ON
========

.. image:: img/tech.png

----

Agenda
======

* Oppsett av utviklingsmiljø

* Kort om utviklingsmiljø

* Oppsett av AngularJS skjelett

* Oppgave

* AngularJS basics

  - Routing

  - Controllere

  - Testing

  - Templating

* Angular oppgaver

* Oppsett av en mock REST-tjeneste

* Oppgaver med REST-tjeneste

* Oppgaver med integrering med mock REST-tjeneste

  - Hente data

  - Opprette data

  - Oppdatere data

----

Oppsett av maskin
=================
  - Aurora utviklerimage
  - Editor (anbefaler Sublime)
  - Node, NPM, Git

----

Andre kjekke verktøy
====================

* Chrome: Postman. Anbefales!

* Firefox: RESTClient, men er buggy

----

Hva er utviklingsmiljøet?
=========================

* JSHint

* Kjøring av tester

* Baking

* Minify

* Pakketering

----

Node.js / Node
==============

.. image:: img/nodejs.png

----

NPM
===

.. image:: img/npm.png

----

Grunt
=====

.. image:: img/grunt-logo.png

----

Bower
=====

.. image:: img/bower.png

----

Yeoman
======

.. image:: img/yeoman.png

----

I Maven-verdenen
================

* Node.js = Java VM

* NPM = Pakkemanager / Avhengigheter (apt-get / gem / pip / yum)

* NPM (package.json) når man bruker Grunt = pluginDependencies i pom.xml

* Grunt = Maven + goal / Ant

* Bower (bower.json) = Dependencies i pom.xml

* Yeoman = mvn archetype:generate

----

Men hvordan lage en webapplikasjon?
===================================

----

.. image:: img/AngularJS.png

----

AngularJS
=========

* Lag en ny mappe

* npm install yo

* Kjør yo

* Velg Angular generator

* bower install, npm i

* grunt serve

----

Code
====

* package.json

* Gruntfile.js

* bower.json

----

Oppbygging
==========

* app/scripts

* app/views

* test/spec/

* dist

----

Oppgave
========

* Kjør "grunt serve" i et vindu

* Editer app/views/main.html, skriv inn noe tekst

* Lagre, og se oppdatering i browseren

Terminologi
===========

* MVVM, MVC, MVP

* Router

* View

 - Det brukeren ser (DOM)

* Template

 - Et HTML fragment

 - Lastes dynamisk

 - Toveis binding

* Controller

  - Kobling mellom View og annen kode

  - Eksponerer data gjennom $scope

  - Har ikke tilgang til DOM

* Directive

  - Gjør DOM-manipulering, enten direkte eller vha templates

  - ng-view, ng-repeat, ng-click

* Scope

  - Kontekst som inneholder modellen

* Data binding

----

Angular moduler
===============

.. code:: js

    angular.module('Modulnavn', ['Avhengighet']);

    angular.module('Modulnavn')
        .controller('ControllerNavn', function($scope, $avhengighet) {
            $scope.navn = "En variabel";
        });

----

Last ned skjelett
==================

* git clone https://github.com/nixx/angular-course.git

* Inneholder løsninger. Ferdig oppsett av proxy.

____

Oppgave 1: Navn på innlogget bruker
===================================

* Lag en fil, userinfo.js

* Lag en kontroller, UserInfoCtrl i riktig modul

* Legg navn på scope

* Editer main.html, og legg til navnet der

.. code:: html

    <div ng-controller="UserInfoCtrl">
    <span>{{name}}</span>
    </div>

.. code:: js

    angular.module('Modulnavn')
        .controller('UserInfoCtrl', function($scope) {
            $scope.navn = "En variabel";
        });

----

Oppgave 1b: To veis binding
===========================

.. code:: html

    <div ng-controller="UserInfoCtrl">
        <span>{{name}}</span><input ng-model="name"/>
    <div>


----

Oppgave 2: Lag en ny route
==========================

* Editer app.js

* Legg til en route til "/todos"

* Lag tilhørende view og controller

* Lag en enkel liste i controlleren

.. code:: js

    $scope.todos = [{title: 'Twilight Sparkle'}, {title: 'Applejack'}, {title: 'Rarity'}];

* List opp listen i view

.. code:: html

    <ul ng-repeat="t in todos">
        <li>{{t.title}}</li>
    </ul>

----

Hva med serverside?
===================

----

Last ned og start REST-tjenesten
================================

.. code::

    $ git clone https://github.com/nixx/express-todo-list.git
    $ npm i
    $ node app.js

----


Start, og utforsk med Postman
=============================

* GET
* PUT
* POST

----

Oppgave 3: Lag en service
=========================

* Lag et TodoRepository i en egen .js fil.

* Legg til avhengigheten i app.js

* Ta inn avhengigheten i controlleren

.. code:: js

    angular.module('Service', ['ngResource'])
        .factory('TodoRepository', function($resource) {
            var todo = $resource('/api/todo/:todoId', {todoId: '@todoId'});
            return {
                find: function() {
                    return todo.query();
                },
                get: function(id) {
                    return todo.get({id: id});
                }
            };
        };

----

Oppgave 3b: Hva med test?
=========================

* Lag en test til controlleren

----

.. code:: js

  'use strict';

  describe('TodoRepository test', function () {

    // Last modulen
    beforeEach(module('services'));

    var resource = {};
    var todoRepository;

    beforeEach(function() {
      resource.query = jasmine.createSpy('query spy').andReturn({});
      resource.get = jasmine.createSpy('get spy').andReturn({});
      module(function($provide){
        $provide.factory('$resource', function(){
          return function() {
            return resource;
          };
        });
      });

      inject(function(_todoRepository_) {
        todoRepository = _todoRepository_;
      });
    });

    it('should call query on resource when called with find', function() {
      todoRepository.find();
      expect(resource.query).toHaveBeenCalled();
    });

    it('should call get on resource when called with get', function() {
      todoRepository.get(1);
      expect(resource.get).toHaveBeenCalledWith({todoId: 1});
    });

  });

----

Oppgave 4: Lag route og controller for å se detaljer
====================================================

* Legg til en route til "/todo/:id"

* Lag view og controller

* Ta inn $routeParams som avhengighet til controlleren ($routeParams.{urlParam})

----

Oppgave 5: Lag route og controller for å lage nye
=================================================

* Legg til en route til "/todo/new"

* Lag view og controller

* Se Angular $resource doc for hvordan man integrerer i TodoRepository

----

Oppgave 6: Lag route og controller for å oppdatere
==================================================

----

Ekstraoppgave: Lag funksjonalitet for sletting, og lag sletteknapp
===================================================================
