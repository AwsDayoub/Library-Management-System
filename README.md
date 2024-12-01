

# Library Management System Module

## Overview
The **Library Management System** module provides tools to manage books, authors, and categories in Odoo. It includes features like ISBN validation, user roles, and wizards for adding books.

---

## Installation Instructions
1. **Dependencies**: Ensure your Odoo instance is installed and running.
2. **Download Module**:
   - Clone or download the module code into your custom addons directory. Example:  
     ```bash
     git clone --depth=1 https://github.com/AwsDayoub/Library-Management-System.git /path/to/odoo/custom_addons/library_management_system
     ```
3. **Activate Developer Mode**:
   - Log in to Odoo, go to **Settings**, and enable **Developer Mode**.
4. **Install the Module**:
   - Navigate to **Apps**, click the **Update App List** button.
   - Search for "Library Management System" and click **Install**.
5. **Security**:
   - Add users to the appropriate groups:
     - **Library Manager**: Full control over the library module.
     - **Librarian**: Read-only access with limited permissions.

---

## ISBN Validation
This module includes ISBN-13 validation for books to ensure that all entered ISBNs comply with the standard format. If an ISBN is invalid, a warning message will appear, and the record will not be saved.

### Rules for ISBN-13 Validation:
1. **Length**: Must be exactly **13 digits**.
2. **Content**: All characters must be numeric (0–9).
3. **Checksum Algorithm**:
   - Multiply every second digit by 3 and leave the other digits unchanged.
   - Add all these values together.
   - The total must be divisible by 10.

### Examples of Valid ISBNs:
- ✅ `9780306406157`
- ✅ `9783161484100`
- ✅ `9780140449136`



## Contact
For issues or feature requests, contact awsdayoub1@gmail.com
