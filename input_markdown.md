Let’s take a look at a document that’s already been generated.

If we click on a cell under the **Surname / Project** column — for example, here with **Klein** — we’ll see the customer’s name displayed as a hyperlink. Clicking it opens the offer document that was created and linked to this entry.

In the top-right corner, you’ll find key customer and order details — including the customer’s surname, offer ID, creation date, and the name of the team member who generated the file. Below that, the document outlines the design details, configuration and accessories, estimated timeframe, and finally, the bike price and payment information.

This document serves as a formal confirmation of what’s been agreed between the company and the customer — so it’s essential that all details are accurate and the pricing is correct.

There are two ways to generate offer documents, depending on the salesperson’s workflow and what’s needed.

The first method is done directly from the **OFFERS** sheet — ideal for generating multiple documents at once.

I’ve added a new offer to the system using the form, selecting English as the preferred language in the **Customer** tab before submitting. We’ll also generate a document for **Król**, whose offer is set to Polish.

I’m happy with the configurations for both and confident the pricing is correct, so it’s time to generate the documents. To do that, we open the **Create** menu in the main toolbar and select **Generate Sales Offer Docs**.

This runs a script that asks for confirmation, then checks each row in the **OFFERS** sheet to see whether a document already exists. If not, the system generates a new PDF and inserts the link into the **Surname / Project** column — making it easy for the team to access documents directly from the system. This method is ideal for batch-processing multiple offers at once.

You’ll notice that the **Surname / Project** cells for both new offers are now underlined, indicating that hyperlinks have been added. That means the script has successfully generated documents for both. Let’s take a look: this one for **Scott** is in English… and the one for **Król**, as expected, is in Polish.
