document.addEventListener('DOMContentLoaded', function () {
    // Function to toggle the visibility of the delivery address section
    function toggleDeliveryAddress() {
        // Assuming the delivery options are radio buttons with name 'carrier_id'
        const deliveryOptions = document.querySelectorAll('input[name="carrier_id"]');
        // Assuming the delivery address section has the class 'o_website_sale_shipping_address'
        const deliveryAddressSection = document.querySelector('.o_website_sale_shipping_address');

        if (!deliveryOptions.length || !deliveryAddressSection) {
            // Elements not found, do nothing
            return;
        }

        let hideAddress = false;
        deliveryOptions.forEach(function(option) {
            // Assuming the "Sur place" option can be identified by its label
            const label = document.querySelector('label[for="' + option.id + '"]');
            if (option.checked && label && label.innerText.includes('Sur place')) {
                hideAddress = true;
            }
        });

        if (hideAddress) {
            deliveryAddressSection.style.display = 'none';
        } else {
            deliveryAddressSection.style.display = 'block';
        }
    }

    // Initial check on page load
    toggleDeliveryAddress();

    // Add event listeners to delivery option radio buttons
    const deliveryOptionInputs = document.querySelectorAll('input[name="carrier_id"]');
    deliveryOptionInputs.forEach(function(input) {
        input.addEventListener('change', toggleDeliveryAddress);
    });
});
