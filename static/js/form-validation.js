/* Add validation to contact form */
$(document).ready(function () {
    $('#contact-form').validate({
        rules: {
            name: {
                required: true,
            },
            email: {
                required: true,
                email: true,
            },
            subject: {
                required: true,
            },
            message: {
                required: true,
            }
        }
    });
});
