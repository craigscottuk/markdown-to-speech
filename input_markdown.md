Let’s take a closer look at how the **System Price** is calculated by examining a full order.

The **System Price** consists of several costs and estimates, which we’ll walk through now.

The majority of the **System Price** comes from the **estimated net cost of the configuration** — that’s the total cost of all the parts and accessories required to assemble the bike. We can get a detailed view of this configuration by expanding this column group, which reveals all the offer data.

The formula here fetches the cost of each component listed in the configuration. If we take a look at it, you’ll see the relevant data spans columns **AC to BX**. The data from these columns is collected and references imported data from the **Inventory & Parts Management** spreadsheet—specifically the **PARTS INDEX** sheet—where pricing is managed by the team and each item has a net price. The formula sums up the cost of all selected components and displays the total net value here.

Another key factor in the **System Price** is the **design and painting cost**, shown here under the blue headers. This reflects the cost of painting the frame and fork, based on the customer’s selected colour scheme or design. For simplicity, the demo uses basic colour options and simplified pricing.

Next, we have **labour estimates**, which cover tasks like frame preparation, assembly, and customer communication. These appear under the black headers and can be manually updated by the salesperson for more complex or demanding projects.

Finally, a **target net margin** is applied — predefined for this bike type and added during form submission. This margin can also be manually adjusted if needed. Any changes to these values will affect the overall project pricing.

So just to summarise, the **System Price** includes:

- the target net margin
- labour for customer communication, preparation, and assembly
- the design and painting cost
- the estimated configuration cost
- and finally, VAT

If the customer’s preferred currency is PLN, the gross value is shown here in złoty. If Euros were set during submission, then the final price is converted using the exchange rate on the day the order was created.

Lastly, let’s take a look at the **Offer Price**, in Column G. This is the final price shown to the customer in the PDF offer document that the system generates and sends out. It’s based on the **System Price**, but rounded using predefined rules to create clean, retail-friendly figures.

For example:  
PLN prices are rounded up to end in **49 złoty** or **99 złoty**, while EUR prices are rounded up to end in **...9 €**.

These rounding rules are applied automatically. If the salesperson edits the configuration or changes the design and the **System Price** is recalculated, the **Offer Price** updates as well with a new rounded value.

However, the **Offer Price** can still be overridden manually by the sales team if a custom figure needs to be applied.

In the next video, we'll take a look at how we can make edits to an offer.
