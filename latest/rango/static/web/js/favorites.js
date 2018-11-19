function submitFavorite(event) {
    let num = event.target.id.split("-")[1];
    let text = $("#post-" + num).text();

    $.get("/add_favorite/" + text, function (data) {
        if (data.data) {
            alert('Quote #' + num + ' favorited successfully!')
        } else {
            alert('Quote #' + num + ' could not be favorited...')
        }  
    });

}

$(window).on("load", function () {
    let buttons = $(".btn");

    buttons.each(function (index) {
        $(this).on("click", submitFavorite);
    });
});