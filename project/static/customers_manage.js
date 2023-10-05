const customerApiUrl = 'http://127.0.0.1:5000/customers';  // Replace with your actual API endpoint
let customers = [];

const fetchCustomers = async () => {
    try {
        const response = await axios.get(customerApiUrl);
        customers = response.data;
        displayCustomers(customers);
    } catch (error) {
        console.error('Error fetching customers:', error);
    }
};

const displayCustomers = (customers) => {
    const customersTableBody = document.getElementById('customers-table-body');
    customersTableBody.innerHTML = '';

    customers.forEach(customer => {
        const row = `
            <tr>
                <td>${customer.id}</td>
                <td>${customer.name}</td>
                <td>${customer.city}</td>
                <td>${customer.age}</td>
                <td>
                    <button class="btn btn-danger btn-sm" onclick="deleteCustomer(${customer.id})">Delete</button>
                    <button class="btn btn-primary btn-sm ml-2" onclick="editCustomer(${customer.id})">Edit</button>
                </td>
            </tr>
        `;
        customersTableBody.innerHTML += row;
    });
};

const addCustomer = (event) => {
    event.preventDefault();

    const name = document.getElementById('addCustomerName').value;
    const city = document.getElementById('addCustomerCity').value;
    const age = document.getElementById('addCustomerAge').value;

    axios.post(customerApiUrl, {
        name,
        city,
        age
    })
    .then(response => {
        fetchCustomers(); // Refresh the customer list after adding
        $('#addCustomerModal').modal('hide');
    })
    .catch(error => console.error('Error adding customer:', error));
};

const deleteCustomer = (customerId) => {
    // Display confirmation dialog
    const isConfirmed = window.confirm("Are you sure you want to delete this customer?");

    // Check if the user confirmed
    if (isConfirmed) {
        axios.delete(`${customerApiUrl}/${customerId}`)
            .then(response => fetchCustomers())
            .catch(error => console.error('Error deleting customer:', error));
    }
};

const editCustomer = (customerId) => {
    const customer = customers.find(c => c.id === customerId);
    document.getElementById('editCustomerId').value = customer.id;
    document.getElementById('editCustomerName').value = customer.name;
    document.getElementById('editCustomerCity').value = customer.city;
    document.getElementById('editCustomerAge').value = customer.age;
    $('#editCustomerModal').modal('show');
};

const saveCustomerChanges = () => {
    const customerId = document.getElementById('editCustomerId').value;
    const name = document.getElementById('editCustomerName').value;
    const city = document.getElementById('editCustomerCity').value;
    const age = document.getElementById('editCustomerAge').value;

    axios.put(`${customerApiUrl}/${customerId}`, {
        name,
        city,
        age
    })
    .then(response => {
        fetchCustomers();
        $('#editCustomerModal').modal('hide');
    })
    .catch(error => console.error('Error updating customer:', error));
};

document.getElementById('addCustomerForm').addEventListener('submit', addCustomer);

fetchCustomers();
