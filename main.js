var slider_img = document.querySelector('.slider-img');
var images = ['alex.jpg', 'Max.jpg', 'dustin.jpg', 'charles.jpg', 'booby.jpg'];
var i = 0;

function prev() {
    // Wrap around to the last image if at the first image
    i = (i <= 0) ? images.length - 1 : i - 1;
    setImg(); // Call setImg to update the image
}

function next() {
    // Wrap around to the first image if at the last image
    i = (i >= images.length - 1) ? 0 : i + 1;
    setImg(); // Call setImg to update the image
}

function setImg() {
    slider_img.setAttribute('src', "images/" + images[i]); // Update the image source
}
