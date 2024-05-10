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

4. Signals (`signals.py`):
   - Defines all performance metric calculations that are performed in real-time.

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
**POST /purchase_orders**
----
  Purchase the order.
* **URL Params**  
  None
* **Data Params**  
{
  "vendor": 2, 
  "order_date": "2024-05-03T10:00:00Z",
  "items": [
    {
      "description": "Item A",
      "unit_price": 19.99,
      "quantity": 10
    },
    {
      "description": "Item B",
      "unit_price": 29.99,
      "quantity": 5
    }
  ],
  "quantity": 15
}
* **Headers**  
  Content-Type: application/json  
  Authorization: Bearer token
* **Success Response:**  
* **Code:** 201
  **Content:**  
```
{
    "message": "Purchase order created successfully!",
    "data": {
        "id": 6,
        "po_number": "PO-Z2V",
        "order_date": "2024-05-10T05:35:05.478922Z",
        "delivery_date": null,
        "items": [
            {
                "description": "Item A",
                "unit_price": 19.99,
                "quantity": 10
            },
            {
                "description": "Item B",
                "unit_price": 29.99,
                "quantity": 5
            }
        ],
        "quantity": 15,
        "status": "pending",
        "quality_rating": null,
        "issue_date": null,
        "acknowledgment_date": null,
        "created_at": "2024-05-10T05:35:05.478737Z",
        "updated_at": "2024-05-10T05:35:05.479056Z",
        "vendor": 2
    }
}
```
**GET /purchase_orders/?vendor_id={id}**
----
  Get purchase order list.
* **URL Params**  
    *Required:* `vendor_id=[integer]`
* **Data Params**  
None
* **Headers**  
  Content-Type: application/json  
  Authorization: Bearer token
* **Success Response:**  
* **Code:** 200
  **Content:**  
```
{
    "message": "List of purchase orders retrieved successfully!",
    "data": [
        {
            "id": 5,
            "po_number": "PO-1J8",
            "order_date": "2024-05-10T04:53:43.017785Z",
            "delivery_date": null,
            "items": [
                {
                    "quantity": 10,
                    "unit_price": 19.99,
                    "description": "Item A"
                },
                {
                    "quantity": 5,
                    "unit_price": 29.99,
                    "description": "Item B"
                }
            ],
            "quantity": 15,
            "status": "pending",
            "quality_rating": null,
            "issue_date": null,
            "acknowledgment_date": null,
            "created_at": "2024-05-10T04:53:43.017495Z",
            "updated_at": "2024-05-10T04:53:43.017940Z",
            "vendor": 2
        }
    ]
}
```
**GET /purchase_orders/{id}/**
----
  Get purchase order details.
* **URL Params**  
    *Required:* `id=[integer]`
* **Data Params**  
None
* **Headers**  
  Content-Type: application/json
  Authorization: Bearer token  
* **Success Response:**  
* **Code:** 200
  **Content:**  
```
{
    "message": "Purchase order details retrieved successfully!",
    "data": {
        "id": 5,
        "po_number": "PO-1J8",
        "order_date": "2024-05-10T04:53:43.017785Z",
        "delivery_date": null,
        "items": [
            {
                "quantity": 10,
                "unit_price": 19.99,
                "description": "Item A"
            },
            {
                "quantity": 5,
                "unit_price": 29.99,
                "description": "Item B"
            }
        ],
        "quantity": 15,
        "status": "pending",
        "quality_rating": null,
        "issue_date": null,
        "acknowledgment_date": null,
        "created_at": "2024-05-10T04:53:43.017495Z",
        "updated_at": "2024-05-10T04:53:43.017940Z",
        "vendor": 2
    }
}
```
**GET /purchase_orders/{id}**
----
  Delete a purchase order.
* **URL Params**  
    *Required:* `id=[integer]`
* **Data Params**  
None
* **Headers**  
  Content-Type: application/json 
  Authorization: Bearer token   
* **Success Response:**  
* **Code:** 204
  **Content:**  
```
{
    "message": "Purchase order deleted successfully."
}
```

**PUT /purchase_orders/{id}/**
----
  Update Purchase the order.
* **URL Params**  
  None
* **Data Params**  
{
  "vendor": 2, 
  "order_date": "2024-05-03T10:00:00Z",
  "items": [
    {
      "description": "Item A",
      "unit_price": 19.99,
      "quantity": 10
    },
    {
      "description": "Item B",
      "unit_price": 29.99,
      "quantity": 5
    }
  ],
  "quantity": 15,
  "delivery_date": "2024-06-09T10:00:00Z",
  "issue_date": "2024-06-09T10:00:00Z"

}

* **Headers**  
  Content-Type: application/json  
  Authorization: Bearer token
* **Success Response:**  
* **Code:** 200
  **Content:**  
```
{
    "message": "Purchase order details updated successfully.",
    "data": {
        "id": 6,
        "po_number": "PO-Z2V",
        "order_date": "2024-05-10T05:35:05.478922Z",
        "delivery_date": "2024-06-09T10:00:00Z",
        "items": [
            {
                "description": "Item A",
                "unit_price": 19.99,
                "quantity": 10
            },
            {
                "description": "Item B",
                "unit_price": 29.99,
                "quantity": 5
            }
        ],
        "quantity": 15,
        "status": "pending",
        "quality_rating": null,
        "issue_date": "2024-06-09T10:00:00Z",
        "acknowledgment_date": null,
        "created_at": "2024-05-10T05:35:05.478737Z",
        "updated_at": "2024-05-10T05:46:40.894321Z",
        "vendor": 2
    }
}
```
**PATCH /purchase_orders/{id}**
----
  Update a purchase order status.
* **URL Params**  
    *Required:* `id=[integer]`
* **Data Params**  
{
  "status": "completed" 
}
* **Headers**  
  Content-Type: application/json 
  Authorization: Bearer token   
* **Success Response:**  
* **Code:** 200
  **Content:**  
```
{
    "message": "PurchaseOrder status updated successfully"
}
```
**GET /vendors/{id}/performance/**
----
  Get vendor performance matrix.
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
    "message": "Vendor performance retrieved successfully.",
    "data": {
        "id": 2,
        "name": "Rupali Aadtiya",
        "contact_details": "8871396532",
        "address": "Indore",
        "vendor_code": "VEN-336",
        "on_time_delivery_rate": 1.0,
        "quality_rating_avg": 4.0,
        "average_response_time": -724.6962261183334,
        "fulfillment_rate": 1.0,
        "created_at": "2024-05-09T17:12:14.161814+00:00",
        "updated_at": "2024-05-10T05:52:13.836165+00:00"
    }
}
```