function submitLike(event) {
    let num = event.target.id.split("-")[1];

    $.get("/like_favorite/" + num, function (data) {
        if (data.data) {
            alert('Favorite #' + num + ' liked successfully!')
            window.location.reload(true);
        } else {
            alert('Favorite #' + num + ' could not be liked...')
        }  
    });

}

$(window).on("load", function () {
    let buttons = $(".btn");

    buttons.each(function (index) {
        $(this).on("click", submitLike);
    });
});