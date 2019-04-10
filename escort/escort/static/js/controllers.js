angular.module('Escort.controllers', []).
controller('watchController', function($scope, $http) {
    console.log("Watch Module Loaded");
    var vm = this; 

    vm.firefighters = []; 
    vm.gasReadings = [];
    vm.tempReadings = [];
    vm.gasOffset = 0; 
    vm.tempOffset = 0; 

    vm.initModule = function(){
        get('/api/firefighters',function(data){
            vm.firefighters = data.data.firefighters;
            loop(); 
        });
    };

    vm.getGasReadings = function(){
        console.log("Fetching gas readings.");
        get('/api/gas_reading?offset='+vm.gasOffset,function(data){
            vm.gasReadings = data.data.gas_readings;
            vm.gasOffset += vm.gasReadings.length;
        });
    };

    vm.getTempReadings = function(){
        console.log("Fetching temp readings.");
        get('/api/temp_reading?offset='+vm.tempOffset,function(data){
            vm.tempReadings = data.data.temp_readings;
            vm.tempOffset += vm.tempReadings.length;
        });
    };

    var loop = function(){
        setTimeout(function () {
            vm.getGasReadings();
            vm.getTempReadings();
            loop()
        }, 9000);
    };

    var post = function(url, data, callback){
        $http({
            url: url,
            method: "POST",
            data: data,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function (data, status, headers, config) {
            callback(data.data);
        }).error(function (data, status, headers, config) {
            callback(data);
        });
    };

    var get = function(url, callback){
        $http.get(url).then(function (data) {
            callback(data.data);
        });
    };

});