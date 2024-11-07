
<template>

    <div style="padding: 20px;">
        <div>
            <h1>ProgramTour</h1>
        </div>
        <div style="padding: 20px;" class="mt-0 mb-5">
            <div class="text-left row mb-3">
                <div class="col-md-4">
                    <label class="mb-2 sr-only" for="inline-form-input-name">location_id</label>
                    <b-form-input v-model="location_id" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
                        placeholder=""></b-form-input>
                </div>
                <div class="col-md-4">
                    <label class="mb-2 sr-only" for="inline-form-input-name">location_Name</label>
                    <b-form-input v-model="location_Name" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
                        placeholder=""></b-form-input>
                </div>
            </div>
            <b-button variant="success" @click="addProgramTour">Add ProgramTour</b-button>
        </div>
        <table class="table table-hover table-bordered" id="example">
            <thead>
                <tr>
                    <th>location_id</th>
                    <th>location_Name</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="ProgramTour in ProgramTours" :key="ProgramTour.location_id">
                    <td>{{ ProgramTour.location_id }}</td>
                    <td>{{ ProgramTour.location_Name }}</td>
                    <td><b-button @click="editProgramTour(ProgramTour)">edit</b-button> <b-button variant="danger"
                            @click="deleteProgramTour(location_id)">del</b-button></td>
                </tr>
            </tbody>
        </table>
        <!-- Modal Edit-->
        <b-modal ref="myModalRef" title="Chang Data ProgramTour" hide-footer>
            <div style="padding: 20px;">
                <div class="text-left row mb-3">
                    <div class="col-md-4">
                        <label class="mb-2 sr-only" for="inline-form-input-name">location_id</label>
                        <b-form-input v-model="location_idEdit" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
                            placeholder="location id"></b-form-input>
                    </div>
                    <div class="col-md-4">
                        <label class="mb-2 sr-only" for="inline-form-input-name">location_Name</label>
                        <b-form-input id="inline-form-input-name" v-model="location_NameEdit"
                            class="mb-2 mr-sm-2 mb-sm-0" placeholder="location name"></b-form-input>
                    </div>
                </div>
                <b-button variant="success" @click="updateProgramTour">Update ProgramTour</b-button>
            </div>
        </b-modal>
        <!-- Modal Edit-->
    </div>
</template>

<script>
export default {
    name: 'ProgramTour',
    data() {
        return {
            ProgramTours: [],
            location_id: '',
            location_Name: '',
            // //Edit
            // productIDEdit: '',
            // productNameEdit: '',
            // productDescEdit: '',
            // productPriceEdit: 0,
            location_idEdit: '',
            location_NameEdit: ''
        }
    },
    mounted() {
        // this.getAPI()
        this.getProgramTour()
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
                "location_Name": this.location_Name
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
            this.location_NameEdit = ProgramTour.location_Name
            this.showModal()
        },
        async updateProgramTour() {
            let bodyJson = {
                "location_id": this.location_idEdit,
                "location_Name": this.location_NameEdit
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
        }



    }
    
}
</script>
