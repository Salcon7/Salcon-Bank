// Smooth scrolling to the footer for "Contact Us"
document.querySelector('.nav-button[href="#lets-connect"]').addEventListener('click', (e) => {
    e.preventDefault(); // Prevent default link behavior
    document.getElementById('lets-connect').scrollIntoView({ behavior: 'smooth' });
});
particlesJS("particles-js", {
    particles: {
        number: { value: 100 },
        color: { value: "#ffffff" },
        shape: { type: "circle" },
        opacity: { value: 0.7 },
        size: { value: 3 },
        move: { speed: 2, direction: "none", out_mode: "bounce" },
        line_linked: { enable: true, distance: 120, color: "#ffffff", opacity: 0.5 }
    }
});
