<template>

    <div style="padding: 20px;">
        <div>
            <h1>Register</h1>
        </div>
        <div style="padding: 20px;" class="mt-0 mb-5">
            <div class="text-left row mb-3">
                <div class="col-md-4">
                    <label class="mb-2 sr-only" for="inline-form-input-name">Customer_id</label>
                    <b-form-input v-model="Customer_id" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
                        placeholder=""></b-form-input>
                </div>
                <div class="col-md-4">
                    <label class="mb-2 sr-only" for="inline-form-input-name">Customer_name</label>
                    <b-form-input v-model="Customer_name" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
                        placeholder=""></b-form-input>
                </div>
                <div class="col-md-4">
                    <label class="mb-2 sr-only" for="inline-form-input-name">Phonenumber</label>
                    <b-form-input id="inline-form-input-name" v-model="Phonenumber" class="mb-2 mr-sm-2 mb-sm-0"
                        placeholder=""></b-form-input>
                </div>
                <div class="col-md-4">
                    <label class="mb-2 sr-only" for="inline-form-input-name">Email</label>
                    <b-form-input id="inline-form-input-name" v-model="Email" class="mb-2 mr-sm-2 mb-sm-0"
                        placeholder=""></b-form-input>
                </div>
            </div>
            <b-button variant="success" @click="addCustomer">Add Customer</b-button>
        </div>
        <table class="table table-hover table-bordered" id="example">
            <thead>
                <tr>
                    <th>Customer_id</th>
                    <th>Customer_name</th>
                    <th>Phonenumber</th>
                    <th>Email</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="Customer in Customers" :key="Customer.Customer_id">
                    <td>{{ Customer.Customer_id }}</td>
                    <td>{{ Customer.Customer_name }}</td>
                    <td>{{ Customer.Phonenumber }}</td>
                    <td>{{ Customer.Email }}</td>
                    <td><b-button @click="editCustomer(Customer)">edit</b-button> <b-button variant="danger"
                            @click="deleteCustomer(Customer_id)">del</b-button></td>
                </tr>
            </tbody>
        </table>
        <!-- Modal Edit-->
        <b-modal ref="myModalRef" title="Chang Data Customer" hide-footer>
            <div style="padding: 20px;">
                <div class="text-left row mb-3">
                    <div class="col-md-4">
                        <label class="mb-2 sr-only" for="inline-form-input-name">Customer_id</label>
                        <b-form-input v-model="Customer_idEdit" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
                            placeholder="Customer id"></b-form-input>
                    </div>
                    <div class="col-md-4">
                        <label class="mb-2 sr-only" for="inline-form-input-name">Customer_name</label>
                        <b-form-input id="inline-form-input-name" v-model="Customer_nameEdit"
                            class="mb-2 mr-sm-2 mb-sm-0" placeholder="Customer name"></b-form-input>
                    </div>
                    <div class="col-md-4">
                        <label class="mb-2 sr-only" for="inline-form-input-name">Phonenumber</label>
                        <b-form-input id="inline-form-input-name" v-model="PhonenumberEdit" class="mb-2 mr-sm-2 mb-sm-0"
                            placeholder="Customer Phonenumber"></b-form-input>
                    </div>
                    <div class="col-md-4">
                        <label class="mb-2 sr-only" for="inline-form-input-name">Email</label>
                        <b-form-input id="inline-form-input-name" v-model="EmailEdit" class="mb-2 mr-sm-2 mb-sm-0"
                            placeholder="Customer Email"></b-form-input>
                    </div>
                </div>
                <b-button variant="success" @click="updateCustomer">Update Customer</b-button>
            </div>
        </b-modal>
        <!-- Modal Edit-->
    </div>
</template>

<script>
export default {
    name: 'Customerpage',
    data() {
        return {
            Customers: [],
            Customer_id: '',
            Customer_name: '',
            Phonenumber: '',
            Email: '',
            // //Edit
            // productIDEdit: '',
            // productNameEdit: '',
            // productDescEdit: '',
            // productPriceEdit: 0,
            Customer_idEdit: '',
            Customer_nameEdit: '',
            PhonenumberEdit: '',
            EmailEdit: ''
        }
    },
    mounted() {
        // this.getAPI()
        this.getCustomer()
        // this.axios
        //     .get("http://localhost:8001/get_all_product/")
        //     .then((res) => {
        //         console.log(res)
        //     })
    },
    methods: {
        // getAPI(){
        //     this.axios
        //     .get("http://localhost:8001/get_all_product/")
        //     .then((res) => {
        //     console.log(res)
        //     })
        // },
        // เปิด Modal
        showModal() {
            this.$refs.myModalRef.show()
        },
        // ปิด Modal
        hideModal() {
            this.$refs.myModalRef.hide()
        },
        async getCustomer() {
            try {
                const response = await this.axios(`http://localhost:8001/get_all_Customer/`)
                if (response.status == 200) {
                    console.log(response.data)
                    this.Customers = response.data
                } else {
                    throw { response }
                }
            } catch (error) {
                console.log(error)
            }
        },
        async addCustomer() {
            let bodyJson = {
                "Customer_id": this.Customer_id,
                "Customer_name": this.Customer_name,
                "Phonenumber": this.Phonenumber,
                "Email": this.Email
            }
            try {
                const response = await this.axios.post(
                    "http://localhost:8001/create_Customer/",
                    bodyJson
                );
                if (response.status === 201) {
                    console.log(response)
                    alert('Add successfully')
                    //this.getCustomer()
                    this.$router.push('/AddedCustomerPage');
                } else {
                    throw { response }
                }
            } catch (error) {
                console.log(error)
            }
        },
        async editCustomer(Customer) {
            console.log(Customer)
            this.Customer_idEdit = Customer.Customer_id
            this.Customer_nameEdit = Customer.Customer_name
            this.PhonenumberEdit = Customer.Phonenumber
            this.EmailEdit = Customer.Email
            this.showModal()
        },
        async updateCustomer() {
            let bodyJson = {
                "Customer_id": this.Customer_idEdit,
                "Customer_name": this.Customer_nameEdit,
                "Phonenumber": this.PhonenumberEdit,
                "Email": this.EmailEdit
            }
            try {
                const response = await this.axios.put(
                    `http://localhost:8001/update_Customer/${this.Customer_idEdit}`,
                    bodyJson
                );
                if (response.status === 200) {
                    console.log(response)
                    alert('Update successfully')
                    this.hideModal()
                    this.getCustomer()
                } else {
                    throw { response }
                }
            } catch (error) {
                console.log(error)
            }
        },
        async deleteCustomer(Customer_id) {
            const confirmed = window.confirm('คุณต้องการลบข้อมูลลูกค้านี้หรือไม่?');
            if (confirmed) {
                try {
                    const response = await this.axios.delete(`http://localhost:8001/delete_Customer/${Customer_id}`);
                    if (response.status === 200) {
                        alert('Customer deleted successfully');
                        this.getCustomer();
                    } else {
                        throw { response };
                    }
                } catch (error) {
                    console.error('Error deleting customer:', error);
                }
            }
        }



    }
}
</script>