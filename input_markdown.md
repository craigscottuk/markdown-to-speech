We can open the **Parts & Inventory Management** spreadsheet from the system’s root folder.

This environment is where we catalogue all components used in production and process data to generate the system’s stock levels. It processes information both from within the file itself and from the **Offers & Production Management** spreadsheet.

The first sheet we land on is the **PARTS INDEX**. This is a master catalogue of all components, accessories, and services used across all builds. It’s the backbone of the system.

It’s structured into clearly defined, colour-coded sections, grouped by area of the bike:

- **Frames / Forks**
- **Drivetrain**
- **Wheels**
- **Cockpit**
- **Saddles / Seatposts / Pedals**
- **Accessories**
- **Services**

Each section expands to reveal the full list of components. Right now, we’re inside the **Drivetrain** section.

Sub-headings are styled with a lighter shade of the section colour, helping break up the content and making it easier to scan and navigate.

Every row within a sub-section represents a specific part used in that area of the bike. Let’s take a closer look at the **Cranksets** now.

For each item listed, we track key details across the following columns:

- **Item Name** – the full product name used to describe the component
- **Item Code** – the official product code assigned by the manufacturer
- The **Manufacturer**
- **Item Category** – the part category (e.g. crankset, bottom bracket, chainring)
- **Bike Type** – the type of build it’s typically used for (e.g. gravel, city)
- **Filtered By** – used for internal filtering and lookups throughout the system
- **Price (PLN, NET)** – the net price in Polish złoty. This is a key value used to calculate costs, generate offers, and flag missing parts

You’ll see we’ve listed multiple versions of each part — varying in tooth count, crank arm length, or model.

This sheet acts as the single source of truth for part pricing. Whenever a component is selected in a project, the system automatically references this index to pull in the correct net price. That ensures consistency across quoting, procurement, and real-time tracking of missing parts.
