var myApp = angular.module('Escort', [
    'Escort.controllers'
]);

myApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});