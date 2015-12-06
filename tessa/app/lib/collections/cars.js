Cars = new Mongo.Collection('cars');

if (Meteor.isServer) {
  Cars.allow({
    insert: function (userId, doc) {
      return true;
    },

    update: function (userId, doc, fieldNames, modifier) {
      return true;
    },

    remove: function (userId, doc) {
      return true;
    }
  });
}

Cars.attachSchema(new SimpleSchema({
  name: {
    type: String,
    label: "Name",
    max: 100
  },
  age: {
    type: Number,
    label: "Age",
    optional: false
  },
  yearofdeath: {
    type: Number,
    label: "Date of Death",
    optional: false
  },
  ethnicity: {
    type: String,
    label: "Family and Friends",
    //allowedValues: ['Chinese', 'Malay', 'Indian', 'Others'],
    max: 10000
  },
  religion: {
    type: String,
    label: "Religion",
    optional: true
  },
  postalcode: {
    type: Number,
    label: "Postal Code",
    optional: true
  }
}));
