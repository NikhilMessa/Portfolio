//Items What we Offer AnimationS
function itemSlideInOutAnimation() {
    const items = document.querySelectorAll('.main-container .item');
    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const index = Array.from(items).indexOf(entry.target);
          if (index % 2 === 0) {
            entry.target.classList.add('animate-left-to-right');
          } else {
            entry.target.classList.add('animate-right-to-left');
          }
          entry.target.style.opacity = '1';
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    items.forEach(item => {
      observer.observe(item);
    });
  }
  document.addEventListener("DOMContentLoaded", itemSlideInOutAnimation);

// FAQ Left Image Animation
function triggerImageAnimationOnScroll() {
    const imgElement = document.querySelector('.img-to-animate');
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'img-anim-left 1.3s forwards cubic-bezier(0.645, 0.045, 0.355, 1)';
                entry.target.style.opacity = '1';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    observer.observe(imgElement);
}
document.addEventListener("DOMContentLoaded", triggerImageAnimationOnScroll);




  
  
  
  
  


