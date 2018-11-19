// function pulled from https://stackoverflow.com/questions/1484506/random-color-generator
function getRandomColor() {
    let letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

$(window).on("load", function () {
    let titles = $(".post > h1");
    let posts = $(".post > p");

    titles.each(function(index) {
        $(this).css('color', getRandomColor());
    });

    posts.each(function(index) {
        $(this).css('color', getRandomColor());
    });
});