// Mobile menu toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    // Add toggle button to DOM
    const toggleButton = document.createElement('button');
    toggleButton.className = 'sidebar-toggle';
    toggleButton.innerHTML = '<i class="fas fa-bars"></i>';
    document.body.appendChild(toggleButton);
    console.log('Toggle button added to DOM');
    // Toggle sidebar on button click
    toggleButton.addEventListener('click', function() {
        const sidebar = document.querySelector('.sidebar');
         sidebar.classList.toggle('active');
        document.body.classList.toggle('sidebar-open');
    });
    
    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', function(e) {
        const sidebar = document.querySelector('.sidebar');
        const toggleButton = document.querySelector('.sidebar-toggle');
        
        if (window.innerWidth <= 768 && 
            !sidebar.contains(e.target) && 
            !toggleButton.contains(e.target) && 
             sidebar.classList.contains('active')) {
            // sidebar.classList.remove('active');
            document.body.classList.remove('sidebar-open');
        }
    });
    
    // Handle window resize
    window.addEventListener('resize', function() {
        const sidebar = document.querySelector('.sidebar');
        if (window.innerWidth > 768 && sidebar.classList.contains('active')) {
            // sidebar.classList.remove('active');
            document.body.classList.remove('sidebar-open');
        }
    });
    
    // Add overlay for mobile
    const overlay = document.createElement('div');
    overlay.className = 'sidebar-overlay';
    document.body.appendChild(overlay);
    
    overlay.addEventListener('click', function() {
        const sidebar = document.querySelector('.sidebar');
        //sidebar.classList.remove('active');
        document.body.classList.remove('sidebar-open');
    });
});