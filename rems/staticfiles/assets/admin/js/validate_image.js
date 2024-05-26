document.addEventListener('DOMContentLoaded', function () {
    const PropertyFrontPicInput = document.getElementById('front-image');
    const PropertyFrontPicPreview = document.getElementById('front-pic');

    const PropertySidePicInput = document.getElementById('side-image');
    const PropertySidePicPreview = document.getElementById('side-pic');

    const PropertyExtraPicInput = document.getElementById('extra-image');
    const PropertyExtraPicPreview = document.getElementById('extra-pic');

    const PropertyExtra2PicInput = document.getElementById('extra2-image');
    const PropertyExtra2PicPreview = document.getElementById('extra2-pic');

    PropertyFrontPicInput.addEventListener('change', function (event) {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {
            PropertyFrontPicPreview.src = e.target.result;
        };

        reader.readAsDataURL(file);
    });

    PropertySidePicInput.addEventListener('change', function (event) {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {
            PropertySidePicPreview.src = e.target.result;
        };

        reader.readAsDataURL(file);
    });

    PropertyExtraPicInput.addEventListener('change', function (event) {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {
            PropertyExtraPicPreview.src = e.target.result;
        };

        reader.readAsDataURL(file);
    });

    PropertyExtra2PicInput.addEventListener('change', function (event) {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {
            PropertyExtra2PicPreview.src = e.target.result;
        };

        reader.readAsDataURL(file);
    });

});