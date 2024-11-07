<template>
    <div>
        <h1>Reservation</h1>
        <table class="table table-hover table-bordered" id="example">
            <thead>
                <tr>
                    <th>Booking_id</th>
                    <th>Firstdate</th>
                    <th>Lastdate</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="Reservation in Reservations" :key="Reservation.Booking_id">
                    <td>{{ Reservation.Booking_id }}</td>
                    <td>{{ Reservation.Firstdate }}</td>
                    <td>{{ Reservation.Lastdate }}</td>
                    <td>
                        <b-button variant="danger" @click="deleteReservation(Reservation.Booking_id)">del</b-button>
                    </td>
                </tr>
            </tbody>
        </table>
        <table class="table table-hover table-bordered" id="example">
            <thead>
                <tr>
                    <th>Customer_id</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="Customer in Customers" :key="Customer.Customer_id">
                    <td>{{ Customer.Customer_id }}</td>
                    <td>
                        <b-button variant="danger" @click="deleteCustomer(Customer.Customer_id)">del</b-button>
                    </td>
                </tr>
            </tbody>
        </table>
        <div></div>
        <table class="table table-hover table-bordered" id="example">
            <thead>
                <tr>
                    <th>location_id</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="ProgramTour in ProgramTours" :key="ProgramTour.location_id">
                    <td>{{ ProgramTour.location_id }}</td>
                    <td>
                        <b-button variant="danger" @click="deleteProgramTour(ProgramTour.location_id)">del</b-button>
                    </td>
                </tr>
            </tbody>
        </table>
        <table class="table table-hover table-bordered" id="example">
            <thead>
                <tr>
                    <th>Guide_id</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="Guide in Guides" :key="Guide.Guide_id">
                    <td>{{ Guide.Guide_id }}</td>
                    <td><b-button variant="danger" @click="deleteGuide(Guide.Guide_id)">del</b-button></td>

                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'Reservationpage',

    data() {
        return {
            Customers: [],
            Customer_id: '',
            //Edit
            Customer_idEdit: '',

            Guides: [],
            Guide_id: '',
            //Edit
            Guide_idEdit: '',

            ProgramTours: [],
            location_id: '',
            //Edit
            location_idEdit: '',

            Reservations: [],
            Booking_id: '',
            Firstdate: '',
            Lastdate: '',
            //Edit
            Booking_idEdit: '',
            FirstdateEdit: '',
            LastdateEdit: ''

        }
    },
    mounted() {
        this.getCustomer()
        this.getProgramTour()
        this.getGuide()
        this.getReservation()
    },
    methods: {
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
            this.showModal()
        },
        async updateCustomer() {
            let bodyJson = {
                "Customer_id": this.Customer_idEdit,
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
        },

        async getProgramTour() {
            try {
                const response = await this.axios(`http://localhost:8001/get_all_ProgramTour/`)
                if (response.status == 200) {
                    console.log(response.data)
                    this.ProgramTours = response.data
                } else {
                    throw { response }
                }
            } catch (error) {
                console.log(error)
            }
        },
        async addProgramTour() {
            let bodyJson = {
                "location_id": this.location_id,

            }
            try {
                const response = await this.axios.post(
                    "http://localhost:8001/create_ProgramTour/",
                    bodyJson
                );
                if (response.status === 201) {
                    console.log(response)
                    alert('Add successfully')
                    this.getProgramTour()
                } else {
                    throw { response }
                }
            } catch (error) {
                console.log(error)
            }
        },
        async editProgramTour(ProgramTour) {
            console.log(ProgramTour)
            this.location_idEdit = ProgramTour.location_id

            this.showModal()
        },
        async updateProgramTour() {
            let bodyJson = {
                "location_id": this.location_idEdit,

            }
            try {
                const response = await this.axios.put(
                    `http://localhost:8001/update_ProgramTour/${this.location_idEdit}`,
                    bodyJson
                );
                if (response.status === 200) {
                    console.log(response)
                    alert('Update successfully')
                    this.hideModal()
                    this.getProgramTour()
                } else {
                    throw { response }
                }
            } catch (error) {
                console.log(error)
            }
        },
        async deleteProgramTour(location_id) {
            const confirmed = window.confirm('คุณต้องการลบข้อมูลการท่องเที่ยวนี้หรือไม่?');
            if (confirmed) {
                try {
                    const response = await this.axios.delete(`http://localhost:8001/delete_ProgramTour/${location_id}`);
                    if (response.status === 200) {
                        alert('ProgramTour deleted successfully');
                        this.getProgramTour();
                    } else {
                        throw { response };
                    }
                } catch (error) {
                    console.error('Error deleting programTour:', error);
                }
            }
        },

        async getGuide() {
            try {
                const response = await this.axios(`http://localhost:8001/get_all_Guide/`)
                if (response.status == 200) {
                    console.log(response.data)
                    this.Guides = response.data
                } else {
                    throw { response }
                }
            } catch (error) {
                console.log(error)
            }
        },
        async addGuide() {
            let bodyJson = {
                "Guide_id": this.Guide_id,

            }
            try {
                const response = await this.axios.post(
                    "http://localhost:8001/create_Guide/",
                    bodyJson
                );
                if (response.status === 201) {
                    console.log(response)
                    alert('Add successfully')
                    //this.getGuide()
                    this.$router.push('/AddedCustomerPage')
                } else {
                    throw { response }
                }
            } catch (error) {
                console.log(error)
            }
        },
        async editGuide(Guide) {
            console.log(Guide)
            this.Guide_idEdit = Guide.Guide_id
            this.showModal()
        },
        async updateGuide() {
            let bodyJson = {
                "Guide_id": this.Guide_idEdit,
            }
            try {
                const response = await this.axios.put(
                    `http://localhost:8001/update_Guide/${this.Guide_idEdit}`,
                    bodyJson
                );
                if (response.status === 200) {
                    console.log(response)
                    alert('Update successfully')
                    this.hideModal()
                    this.getGuide()
                } else {
                    throw { response }
                }
            } catch (error) {
                console.log(error)
            }
        },
        async deleteGuide(Guide_id) {
            const confirmed = window.confirm('คุณต้องการลบข้อมูลไกด์นี้หรือไม่?');
            if (confirmed) {
                try {
                    const response = await this.axios.delete(`http://localhost:8001/delete_Guide/${Guide_id}`);
                    if (response.status === 200) {
                        alert('Guide deleted successfully');
                        this.getGuide();
                    } else {
                        throw { response };
                    }
                } catch (error) {
                    console.error('Error deleting guide:', error);
                }
            }
        },
        async getReservation() {
            try {
                const response = await this.axios(`http://localhost:8001/get_all_Reservation/`)
                if (response.status == 200) {
                    console.log(response.data)
                    this.Reservations = response.data
                } else {
                    throw { response }
                }
            } catch (error) {
                console.log(error)
            }
        },
        async addReservation() {
            let bodyJson = {
                "Booking_id": this.Booking_id,
                "Firstdate": this.Firstdate,
                "Lastdate": this.Lastdate
            }
            try {
                const response = await this.axios.post(
                    "http://localhost:8001/create_Reservation/",
                    bodyJson
                );
                if (response.status === 201) {
                    console.log(response)
                    alert('Add successfully')
                    this.getReservation()
                } else {
                    throw { response }
                }
            } catch (error) {
                console.log(error)
            }
        },
        async editReservation(Reservation) {
            console.log(Reservation)
            this.Booking_idEdit = Reservation.Booking_id
            this.FirstdateEdit = Reservation.Firstdate
            this.LastdateEdit = Reservation.Lastdate
            this.showModal()
        },
        async updateReservation() {
            let bodyJson = {
                "Booking_id": this.Booking_idEdit,
                "Firstdate": this.FirstdateEdit,
                "Lastdate": this.LastdateEdit
            }
            try {
                const response = await this.axios.put(
                    `http://localhost:8001/update_Reservation/${this.Booking_idEdit}`,
                    bodyJson
                );
                if (response.status === 200) {
                    console.log(response)
                    alert('Update successfully')
                    this.hideModal()
                    this.getReservation()
                } else {
                    throw { response }
                }
            } catch (error) {
                console.log(error)
            }
        },
        async deleteReservation(Booking_id) {
            const confirmed = window.confirm('Are you sure you want to delete this reservation?');
            if (confirmed) {
                try {
                    const response = await this.axios.delete(`http://localhost:8001/delete_Reservation/${Booking_id}`);
                    if (response.status === 200) {
                        alert('Reservation deleted successfully');
                        this.getReservation();
                    } else {
                        throw { response };
                    }
                } catch (error) {
                    console.error('Error deleting reservation:', error);
                }
            }
        }


    }
}
</script>


<style>
/* CSS styling ตามความเหมาะสม */
</style>