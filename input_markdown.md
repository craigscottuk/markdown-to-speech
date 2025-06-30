Once an offer has been configured, we can generate a formal **Offer Document** — a customer-facing PDF that provides a clear, professional summary of the proposed bike build.

These documents can be created in either English or Polish. The customer’s language preference is set during the offer creation process — either through the offer creation form, or later by editing the customer’s data in the **Customer** tab of the Project Manager, or directly in the **OFFERS** tab of the main spreadsheet.

Let’s take a look at an example that’s already been generated.

If we click on a cell under the **Surname / Project** column — for example, here with **Klein** — we can see the customer’s name appears as a hyperlink. Hovering over it shows a preview and a link to the attached PDF. Clicking it opens the document that was created and linked to this offer.

In the top-right corner, we can see key customer and order details — including the customer’s surname, offer ID, creation date, and the team member who generated the file. Below that, the document lists the design details, configuration, pricing, accessories, and payment information. This is an important document that confirms what’s been agreed between the company and the customer — so it’s essential that all details are correct and the pricing is accurate.

There are two ways to generate offer documents, depending on the salesperson’s workflow and what’s needed.

The first method is from the **OFFERS** sheet — ideal for generating multiple documents at once.

I’ve added another new offer to the system using the form. This project — titled **Scott** — was submitted with English selected as the preferred language in the **Customer** tab. We’ll also generate a document for **Król**, which is set to Polish.

I’m happy with the configurations for both and confident the pricing is correct, so it’s time to generate the documents. To do that, we open the **Create** menu in the main toolbar and select **Generate Sales Offer Docs**.

This runs a script that checks each row in the OFFERS sheet to see whether a document link already exists. If there’s no link, the system generates a new PDF and inserts the document link into the **Surname / Project** column for each offer — making it easy to access from the main spreadsheet. This avoids overwriting any existing documents and allows multiple offers to be processed in one go.

You’ll notice the **Surname / Project** cells for both new offers are now underlined, showing that hyperlinks have been added. That means the script has generated documents for both. Let’s check them. This one for **Scott** is in English… and the one for **Król**, as expected, is in Polish.
