# Facebook Group Post Remover Bookmarklet

This bookmarklet is designed to help you remove comments and posts from groups in your Facebook activity log in an automated fashion.

## How to use

1. Go to Facebook and navigate to **Settings & Privacy**.
2. Click on **Activity Log**.
3. Select the **Group** filter from the left sidebar.
4. Locate the following buttons on the page: the "Action options" button (3-dot button) and the "Delete" menu item.
5. Right-click on the "Action options" button, then click **Inspect** to open the browser's developer tools. The corresponding HTML element should be highlighted.
6. Right-click on the highlighted element and choose **Copy** > **Copy selector (JS)**.
7. Replace the `button1` value in the `bookmarklet.js` code with the copied selector.
8. Repeat steps 5-7 for the "Delete" menu item, updating the `button2` value.
9. Open the browser console (right-click anywhere on the page, click **Inspect**, and then click on the **Console** tab).
10. Copy the entire modified code from `bookmarklet.js` and paste it into the console.
11. Press **Enter** to start the process.

The bookmarklet will automatically click on the necessary buttons to remove comments and posts from groups in your activity log. It will continue to do so indefinitely until you stop it or close the browser.

## Troubleshooting

If the script doesn't work, it's possible that the paths for the buttons have changed. You'll need to update the button selectors in the `bookmarklet.js` file following the same steps mentioned in the "How to use" section.

## Notes

This bookmarklet is not affiliated with or endorsed by Facebook. Use it at your own risk. The code is provided "as is" with no guarantees or warranties. Always double-check the button selectors before running the script, as changes to Facebook's layout or code may affect its functionality.
