As mentioned in the previous video, there are two key pricing columns: **System Price** in Column F and **Offer Price** in Column G.

When a new offer is submitted, dynamic formulas are automatically applied to that row. These formulas calculate the **System Price**, which then generates an **Offer Price**.

Both values are influenced by the **Currency** in Column D and the **VAT Rate** in Column E.

This demo is based on a real-world system I built for a bicycle manufacturer in Poland, so I’ve kept the original currency setup. You’ll see prices displayed in **Polish złoty (PLN)** and **Euros (EUR)**, with PLN as the system’s primary operating currency.

Looking at the data here, we can see several offers for Poland-based customers — indicated by **PLN** as the currency and a **23% VAT rate**. There are also offers for German customers — using **EUR** with **19% VAT** — and for customers in Czechia, also paying in **EUR**, but with **21% VAT**. And it looks like there’s one Swiss customer, where **no VAT** is applied at all.

The **Currency** and **VAT Rate** are first defined by the salesperson in the **Customer** tab of the offer creation form — but they can also be edited directly in the sheet.

For example, if we change the currency for customer “Król” from **PLN** to **EUR**, the system automatically converts the bike price to Euros. That triggers an update to the **System Price**, using the relevant exchange rate, and the **Offer Price** is adjusted accordingly.
Currency conversion is handled using a **Google Finance formula**, which includes a date parameter. This allows the system to retrieve the historical exchange rate **based on the offer’s creation date**, ensuring the conversion reflects the rate at that specific time. This helps preserve pricing accuracy for Euro projects.

If the **VAT Rate** is updated on an offer, the **System Price** is recalculated first, followed by the **Offer Price**, which adjusts to reflect the new VAT.

Let’s take a closer look at how the **System Price** is calculated by examining a full order.

The **System Price** consists of several costs and estimates, which we’ll walk through now.

The majority of the **System Price** comes from the **estimated net cost of the configuration** — that’s the total cost of all the parts and accessories required to assemble the bike. We can get a detailed view of this configuration by expanding this column group, which reveals all the offer data.

The formula here fetches the cost of each component listed in the configuration. If we take a look at it, you’ll see the relevant data spans columns **AC to BX**. The data from these columns is collected and references imported data from the **Inventory & Parts Management** spreadsheet—specifically the **PARTS INDEX** sheet—where pricing is managed by the team and each item has a net price. The formula sums up the cost of all selected components and displays the total net value here.

Another key factor in the **System Price** is the **design and painting cost**, which you can see here under the blue headers. This reflects the cost of painting the frame and fork, based on the customer’s chosen colour scheme or design. To keep things simple in this demo, I’ve reduced the options to basic colours and simplified the pricing. In real life, custom bicycle companies often offer more elaborate and creative paintwork, as well as additional design services.

Next, we account for **labour estimates**, which cover time for frame preparation, assembly, and customer communication. These costs appear under the black headers and can be manually updated by the salesperson for more demanding or complex projects.

Lastly, we apply a **target net margin**, which is predefined for this bike type or product and is applied to the offer during form submission.

The paint cost, labour estimates, and margin can all be manually adjusted by the salesperson if needed. Any updates to these values will affect the overall pricing of the project.

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
