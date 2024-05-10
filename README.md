The Vendor Management System (VMS) aims to facilitate the management and tracking of vendor-related activities, including purchase orders, vendor performance, and historical metrics. The key components of the system are:

1. Views (`views.py`):
   - `VendorView`: Manages creating, editing, listing, deleting, and viewing vendors.
   - `AddUserApiView`: Handles the creation of users.
   - `LoginApiView`: Handles user login and generates JWT tokens.
   - `PurchaseOrderView`: Manages creating, editing, listing, deleting, viewing, and updating the status of purchase orders.
   - `VendorPerformanceView`: provides a performance metric for a vendor.
   - `AcknowledgePurchaseOrderView`: acknowledges the purchase order.

2. Models (`models.py`):
   - `Vendor`: Represents a vendor.
   - `User`: Represents a user.
   - `PurchaseOrder`: Represents a purchase order.
   - `HistoricalPerformance`: Represents a record of historical performance.

3. URLs (`urls.py`):
   - Defines the API endpoints for adding, editing, listing, deleting, and viewing vendors; creating, editing, listing, deleting, viewing, and updating the status of purchase orders; recording performance metrics for a vendor; and acknowledging purchase orders.

API Contracts

**POST /addUser**
----
  Add user in the system.
* **URL Params**  
  None
* **Data Params**  
{
    "email": "rupali@gmail.com",
    "name": "Rupali",
    "mobile": "8872396530",
    "password": "Rupali@1234"
}
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "message": "User added successfully",
    "data": {
        "id": 3,
        "email": "rupali@gmail.com",
        "name": "Rupali",
        "mobile": "8872396530"
    }
}
```

**POST /login**
----
  Login user in the system.
* **URL Params**  
  None
* **Data Params**  
{
    "email": "rupali@gmail.com",
    "password": "Rupali@1234"
}
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "user_id": 2,
    "email": "rupali@gmail.com",
    "name": "Rupali",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwODI1MDMyNSwiaWF0IjoxNzA4MTYzOTI1LCJqdGkiOiJhMjdmNjEyMWQzZWY0ZmY4YmY4MzY4Y2Y5YTk2OThmOCIsInVzZXJfaWQiOjJ9.vcUo3C0tEJCGSmXD4V6qQwTpBlDYVV7WGPVsjxJ_ki0",
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4MTY2OTI1LCJpYXQiOjE3MDgxNjM5MjUsImp0aSI6ImVhN2JiMzI5ZjYzNDRmNDI4ODY5YjA0NDY1OWI3YzcxIiwidXNlcl9pZCI6Mn0.QAqwuehDViyzt66m8fP9O1VN6MuW7xLGksH5IQSj-7M"
}
```

**POST /vendors**
----
  Create a vendor.
* **URL Params**  
  None
* **Data Params**  
{
  "name": "Rupali Aadtiya", 
  "contact_details": "8871396530",
  "address": "Indore"
}
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 201  
  **Content:**  
```
{
    "message": "Vendor created successfully!",
    "data": {
        "id": 3,
        "name": "Rupali Aadtiya",
        "contact_details": "8871396530",
        "address": "Indore",
        "vendor_code": "VEN-XTZ",
        "created_at": "2024-05-10T05:06:42.734522Z",
        "updated_at": "2024-05-10T05:06:42.734793Z"
    }
}
```

**GET /vendors**
----
  List of vendors.
* **URL Params**  
  None
* **Data Params**  
  None
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "message": "List of vendors retrieved successfully.",
    "data": [
        {
            "id": 3,
            "name": "Rupali Aadtiya",
            "contact_details": "8871396530",
            "address": "Indore",
            "vendor_code": "VEN-XTZ",
            "created_at": "2024-05-10T05:06:42.734522Z",
            "updated_at": "2024-05-10T05:06:42.734793Z"
        }
    ]
}
```

**GET /vendors/{id}**
----
  Retrieve details of vendor.
* **URL Params**  
    *Required:* `id=[integer]`
* **Data Params**  
None
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "message": "Vendor details retrieved successfully.",
    "data": {
        "id": 3,
        "name": "Rupali Aadtiya",
        "contact_details": "8871396530",
        "address": "Indore",
        "vendor_code": "VEN-XTZ",
        "created_at": "2024-05-10T05:06:42.734522Z",
        "updated_at": "2024-05-10T05:06:42.734793Z"
    }
}
```

**GET /vendors/{id}**
----
  Delete a vendor.
* **URL Params**  
    *Required:* `id=[integer]`
* **Data Params**  
None
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 204
  **Content:**  
```
{
    "message": "Vendor deleted successfully."
}
```

**PUT /vendors/{id}**
----
  Update a vendor.
* **URL Params**  
    *Required:* `id=[integer]`
* **Data Params**  
{
  "name": "Rupali Aadtiya", 
  "contact_details": "8871396530",
  "address": "Indore"
}
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "message": "Vendor details updated successfully.",
    "data": {
        "id": 3,
        "name": "Rupali Aadtiya",
        "contact_details": "8871396530",
        "address": "Indore",
        "vendor_code": "VEN-XTZ",
        "created_at": "2024-05-10T05:06:42.734522Z",
        "updated_at": "2024-05-10T05:06:42.734793Z"
    }
}
```
**GET /purchase_orders/{id}/acknowledge/**
----
  Acknowledge purchase order.
* **URL Params**  
    *Required:* `id=[integer]`
* **Data Params**  
None
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 200
  **Content:**  
```
{
    "message": "Purchase order acknowledged successfully"
}
```