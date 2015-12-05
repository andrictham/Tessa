/*****************************************************************************/
/* Home: Event Handlers */
/*****************************************************************************/
Template.Home.events({
});

/*****************************************************************************/
/* Home: Helpers */
/*****************************************************************************/
Template.Home.helpers({
});

/*****************************************************************************/
/* Home: Lifecycle Hooks */
/*****************************************************************************/
Template.Home.onCreated(function () {
});

Template.Home.onRendered(function () {

	$(document).foundation();

	$(".tabs-panel").on('click','a', function(){
    $(this).toggleClass('success').siblings().removeClass('success');
 	})


});

Template.Home.onDestroyed(function () {
});
