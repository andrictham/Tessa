
Meteor.publish('tessa', function () {
  return Tessa.find();
});

Meteor.publish('cars', function () {
  return Cars.find();
});