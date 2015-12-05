Router.configure({
  layoutTemplate: 'MasterLayout',
  loadingTemplate: 'Loading',
  notFoundTemplate: 'NotFound'
});


Router.route('/', {
  name: 'home',
  controller: 'HomeController',
  where: 'client'
});

Router.route('/records/create', {
  name: 'createCar',
  controller: 'CarsController',
  action: 'create',
  where: 'client'
});

Router.route('/records', {
  name: 'carsList',
  controller: 'CarsController',
  action: 'list',
  where: 'client'
});