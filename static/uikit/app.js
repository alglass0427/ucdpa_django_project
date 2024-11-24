// Invoke Functions Call on Document Loaded
// document.addEventListener('DOMContentLoaded', function () {
//   hljs.highlightAll();
// });

// Invoke Functions Call on Document Loaded
// document.addEventListener('DOMContentLoaded', function () {
//   hljs.highlightAll();
// });


// let alertWrapper = document.querySelector('.alert');
// let alertClose = document.querySelector('.alert__close');

// console.log(alertWrapper);

// if (alertWrapper) {
//   alertClose.addEventListener('click', () => {
//     alertWrapper.style.display = 'none';
//     console.log('Clicked Close');
//   });
// }

document.addEventListener('DOMContentLoaded', function() {
    // Select all alert elements
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        const closeBtn = alert.querySelector('.alert__close');
        
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                alert.style.display = 'none';
                console.log('Clicked Close');
            });
        }
    });
});