$('#close-btn').on('click', function(){
    let newPostContainer = $('#post-container');
    newPostContainer.css('visibility', 'hidden')
});

$('#show-btn').on('click', function(){
    let newPostContainer = $('#post-container');
    newPostContainer.css('visibility', 'visible')
});