# Hobby Attic 2.0
Open index.html in a browser or upload the contents of this folder to your GitHub Pages repository root. Back up the old site first.

## Edit your catalogue
Edit products.json, then run `python update_catalog.py` in this folder and upload the changed files (including catalog.js and any new product folders). Alternatively edit catalog.js directly if you do not use Python, but keep products.json in sync. Use unique URL-safe IDs. Existing product pages load their details from catalog.js.

- image: main image path relative to site root.
- sizeImages: separate paths for 3, 4 and 5 inch photos. Empty uses main photo. Add your image files to images/ first.
- prices: numeric rupee amounts for each height. null means price on request. Existing referencePrice is the original listed price, not assigned to a height.
- draft: true means concept listing, cannot add to cart. Change to false after verifying details and availability.
- config.js: set showDrafts to false to hide concepts before public launch; enter your WhatsApp number with country code, digits only (no + or spaces).

Cart is saved locally in the customer's browser. Checkout sends an enquiry, not a payment. No backend, live inventory, delivery quotes or order tracking. Confirm all specifications and lamp size feasibility before publishing. Original photographs were converted to WebP; originals remain in your old ZIP.
