$(document).ready(()=>{
    const animatedElements = $('.animated-element')
    var waypoints = animatedElements.waypoint(function() {
        animatedElements.addClass('animated')
        animatedElements.addClass('fadeIn')
    },{ offset: '100%' })
})

