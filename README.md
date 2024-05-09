Installation:
- Clone the repository
- Navigate to the project directory
- Install dependencies using pip
- Apply database migrations
- Run the development server


API Endpoints
Vendor Profile Management
- POST/api/vendor/: Create a new vendor
- GET/api/vendor/: List all vendors
- GET/api/vendors/<id>/: Retrieve a specific vendors details
- PUT/api/vendors/<id>/update/: Update a vendors details
- DELETE/api/vendors/<id>/delete/: Delete a vendor

Purchase Order Tracking
- POST/api/purchase_order/: Create a purchase_order
- GET/api/purchase_orders/: Retrieve a list of all purchase orders
- GET/api/purchase_order/<id>/: Retrieve details of a specific purchase order by id.
- PUT/api/purchase_order/<id>/update/: Update details of a specific purchase order by id.
- DELETE/api/purchase_order/<id>/delete/: Delete a specific purchase order by id.

Vendor Performance
- GET/api/vendors/<id>/performance/: Retrieve a vendor's performance metrics 
