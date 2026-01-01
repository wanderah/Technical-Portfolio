/*  This JavaScript code snippet uses the jQuery library to add five distinct, 
    common interactivity and dynamic features to the GreenLeaf Garden website. 
    All the code is contained within the $(document).ready(function() { ... }); 
    block, ensuring it runs only after the full webpage structure (DOM) is loaded.
*/ 

// script.js

$(document).ready(function() {
    
    // --- 1. Dynamic Greeting ---
    if ($('#main-greeting').length) {
        function getGreeting() {
            const hour = new Date().getHours();
            if (hour < 12) {
                return "Good Morning, Welcome!";
            } else if (hour < 18) {
                return "Good Afternoon, Welcome!";
            } else {
                return "Good Evening, Welcome!";
            }
        }
        $('#main-greeting').text(getGreeting());
    }

    // --- 2. CTA Reveal (Animated Reveal) ---
    $('#volunteer-cta').click(function() {
        $('#signup-widget').slideToggle(400); 
    });
    
    // --- 3. Hover Effect ---
    $('#events ul li').hover(
        function() { // Mouse enter
            $(this).css('background-color', '#fff0d1');
        },
        function() { // Mouse leave
            $(this).css('background-color', 'transparent');
        }
    );

    // --- 4. Slideshow Functionality  ---
    let slideIndex = 0;
    showSlides();

    function showSlides() {
        let i;
        let slides = $(".slide");
        
        // Hide all slides
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        
        // Increment slide index and loop back if it exceeds the number of slides
        slideIndex++;
        if (slideIndex > slides.length) {slideIndex = 1}
        
        // Display the current slide and start the fading animation (CSS handles the 'fade' animation)
        slides[slideIndex - 1].style.display = "block";
        
        // Change image every 5 seconds (5000 milliseconds)
        setTimeout(showSlides, 5000); 
    }
    
    // --- 5. Client-Side Form Validation (About Page) ---
    $('#volunteer-form').submit(function(e) {
        e.preventDefault(); 
        let isValid = true;

        // Name Validation
        const name = $('#name').val().trim();
        if (name.length < 3) {
            $('#name-error').slideDown().css('display', 'block');
            $('#name').css('border-color', 'red');
            isValid = false;
        } else {
            $('#name-error').slideUp();
            $('#name').css('border-color', '#ddd');
        }

        // Email Validation
        const email = $('#email').val().trim();
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            $('#email-error').slideDown().css('display', 'block');
            $('#email').css('border-color', 'red');
            isValid = false;
        } else {
            $('#email-error').slideUp();
            $('#email').css('border-color', '#ddd');
        }

        // Consent Checkbox Validation
        if (!$('#consent-share').is(':checked')) {
            $('#consent-error').slideDown().css('display', 'block');
            isValid = false;
        } else {
            $('#consent-error').slideUp();
        }

        if (isValid) {
            alert("Application submitted successfully! (In a real application, data would be sent to a server.)");
        }
    });
});