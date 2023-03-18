javascript:(function() {
    function simulateClick(element) {
        if (!element) {
            console.error('Element not found');
            return;
        }
        const event = new MouseEvent('click', {
            bubbles: true,
            cancelable: true,
            view: window
        });
        element.dispatchEvent(event);
    }

    function randomMultiplier() {
        return Math.random() * 0.33 + 1;
    }

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async function performActions() {
        try {
            const button1 = document.querySelector('the first button selector');
            const button2 = document.querySelector('the second button selector');

            if (!button1 || !button2) {
                console.error('One or more elements not found');
                return;
            }

            simulateClick(button1);
            await sleep(500 * randomMultiplier());

            simulateClick(button2);
            await sleep(500 * randomMultiplier());
        } catch (error) {
            console.error('Error performing actions:', error);
        }
    }

    async function main() {
        while (true) {
            await performActions();
            await sleep(1000); // Add sleep before retrying
        }
    }

    main();
})();
