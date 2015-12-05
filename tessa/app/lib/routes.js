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


Router.route('/input/create', {
  name: 'inputPerson',
  controller: 'InputController',
  action: 'create',
  where: 'client'
});