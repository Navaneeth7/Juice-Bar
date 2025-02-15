document.addEventListener("DOMContentLoaded", () => {
    const scroller = document.querySelector('.scroller');

    // Duplicate images for a seamless infinite effect
    scroller.innerHTML += scroller.innerHTML;
    const images=document.querySelectorAll('.image-container');
    images.forEach(img => {
        img.addEventListener('mouseenter', () => {
            scroller.style.animationPlayState = 'paused';
        });
        img.addEventListener('mouseleave', () => {
            scroller.style.animationPlayState = 'running';
        });
    });
});