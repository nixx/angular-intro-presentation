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

* Hva er et utviklingsmiljø?

* Kort om teknologiene

  - Hva er stabilt?

  - Hva er ustabilt?

  - Hvorfor ikke Maven?

* Serverside JavaScript

  - Vi skal se på en mockserver

* Bruk av verktøy for å sette opp AngularJS skjellett

  - Gjennomgang av filer

* Konsepter i AngularJS

* Oppgaver

  - Alternativ 1: Todoliste

  - Alternativ 2: Aurora-tjenester

* Integrering med mock REST-tjeneste

  - Hente data

  - Opprette data

  - Oppdatere data

* Integrering med Maven-prosjekter

----

Oppsett av utviklingsmaskin
=================
  - Aurora utviklerimage
  - Editor (anbefaler Sublime)
  - Node, NPM, Git

 https://aurora/wiki/display/utf/Bootstrapping+av+JavaScript-applikasjon

----

Andre kjekke verktøy
====================

* Chrome: Postman. Anbefales!

* Firefox: RESTClient, men er buggy

----

Kort om teknologiene
====================

* Node

* Avhengigheter

* Byggeverktøy

----

Last ned REST-tjenesten
=======================

.. code::

    $ git clone https://github.com/nixx/express-todo-list.git


----

Filer
=====

* App.js

* Gruntfile.js

* Katalog app

* package.json

----

Start, og utforsk med Postman
=============================

* GET
* PUT
* POST

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


Oppbygging
==========

* app/scripts

* app/views

* test/spec/

* dist

----

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


* Lag en fil, userinfo.js. Legg til i index.html

* Lag en kontroller, UserInfoCtrl i riktig modul

* Legg navn på scope

* Editer main.html, og legg til navnet der

.. code:: html

    <div ng-controller="UserInfoCtrl">
    <span>{{name}}</span>
    </div>

.. code:: js

    angular.module('angularApp')
        .controller('UserInfoCtrl', function($scope) {
            $scope.navn = "En variabel";
        });

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

