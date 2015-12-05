
Meteor.publish('tessa', function () {
  return Tessa.find();
});