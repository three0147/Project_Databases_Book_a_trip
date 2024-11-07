
<template>

    <div style="padding: 20px;">
        <div>
            <h1>Guide</h1>
        </div>
        <div style="padding: 20px;" class="mt-0 mb-5">
            <div class="text-left row mb-3">
                <div class="col-md-4">
                    <label class="mb-2 sr-only" for="inline-form-input-name">Guide_id</label>
                    <b-form-input v-model="Guide_id" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
                        placeholder=""></b-form-input>
                </div>
                <div class="col-md-4">
                    <label class="mb-2 sr-only" for="inline-form-input-name">Email</label>
                    <b-form-input v-model="Email" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
                        placeholder=""></b-form-input>
                </div>
                <div class="col-md-4">
                    <label class="mb-2 sr-only" for="inline-form-input-name">Languages</label>
                    <b-form-input v-model="Languages" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
                        placeholder=""></b-form-input>
                </div>
            </div>
            <b-button variant="success" @click="addGuide">Add Guide</b-button>
        </div>
        <table class="table table-hover table-bordered" id="example">
            <thead>
                <tr>
                    <th>Guide_id</th>
                    <th>Email</th>
                    <th>Languages</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="Guide in Guides" :key="Guide.Guide_id">
                    <td>{{ Guide.Guide_id }}</td>
                    <td>{{ Guide.Email }}</td>
                    <td>{{ Guide.Languages }}</td>
                    <td><b-button @click="editGuide(Guide)">edit</b-button> <b-button variant="danger"
                            @click="deleteGuide(Guide.Guide_id)">del</b-button></td>

                </tr>
            </tbody>
        </table>
        <!-- Modal Edit-->
        <b-modal ref="myModalRef" title="Chang Data Guide" hide-footer>
            <div style="padding: 20px;">
                <div class="text-left row mb-3">
                    <div class="col-md-4">
                        <label class="mb-2 sr-only" for="inline-form-input-name">Guide_id</label>
                        <b-form-input v-model="Guide_idEdit" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
                            placeholder="location id"></b-form-input>
                    </div>
                    <div class="col-md-4">
                        <label class="mb-2 sr-only" for="inline-form-input-name">Email</label>
                        <b-form-input id="inline-form-input-name" v-model="EmailEdit"
                            class="mb-2 mr-sm-2 mb-sm-0" placeholder="location name"></b-form-input>
                    </div>
                    <div class="col-md-4">
                        <label class="mb-2 sr-only" for="inline-form-input-name">Languages</label>
                        <b-form-input id="inline-form-input-name" v-model="LanguagesEdit"
                            class="mb-2 mr-sm-2 mb-sm-0" placeholder="location name"></b-form-input>
                    </div>
                </div>
                <b-button variant="success" @click="updateGuide">Update Guide</b-button>
            </div>
        </b-modal>
        <!-- Modal Edit-->
    </div>
</template>

<script>
export default {
    name: 'Guide',
    data() {
        return {
            Guides: [],
            Guide_id: '',
            Email: '',
            Languages: '',
            // //Edit
            // productIDEdit: '',
            // productNameEdit: '',
            // productDescEdit: '',
            // productPriceEdit: 0,
            Guide_idEdit: '',
            EmailEdit: '',
            LanguagesEdit: ''
        }
    },
    mounted() {
        // this.getAPI()
        this.getGuide()
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
                "Email": this.Email,
                "Languages": this.Languages
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
            this.EmailEdit = Guide.Email
            this.LanguagesEdit = Guide.Languages
            this.showModal()
        },
        async updateGuide() {
            let bodyJson = {
                "Guide_id": this.Guide_idEdit,
                "Email": this.EmailEdit,
                "Languages": this.LanguagesEdit
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
        }



    }
}
</script>
