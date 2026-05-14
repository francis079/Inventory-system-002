// JavaScript for supermarket inventory system
document.querySelector('form').addEventListener('submit', function(e) {
    const name = document.querySelector('input[name="name"]').value;
    const category = document.querySelector('input[name="category"]').value;
    const quantity = document.querySelector('input[name="quantity"]').value;
    const price = document.querySelector('input[name="price"]').value;
    if (!name || !category || quantity <= 0 || price <= 0) {
        alert('Please enter valid item details.');
        e.preventDefault();
    }
});

// Add styling: focus effects for inputs
const inputs = document.querySelectorAll('input, textarea');
inputs.forEach(input => {
    input.addEventListener('focus', () => {
        input.style.borderColor = '#28a745';
        input.style.boxShadow = '0 0 5px rgba(40, 167, 69, 0.5)';
    });
    input.addEventListener('blur', () => {
        input.style.borderColor = '#ccc';
        input.style.boxShadow = 'none';
    });
});

// Fade-in effect for the inventory table
window.addEventListener('load', function() {
    const table = document.querySelector('table');
    if (table) {
        table.style.opacity = '0';
        table.style.transition = 'opacity 1s ease-in-out';
        setTimeout(() => table.style.opacity = '1', 200);
    }
});

// Search functionality
document.getElementById('search').addEventListener('input', function() {
    const query = this.value.toLowerCase();
    const rows = document.querySelectorAll('#inventory-table tbody tr');
    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(query) ? '' : 'none';
    });
});