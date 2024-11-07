<template>
  <div style="padding: 20px;">
    <div>
      <h1>Booking</h1>
    </div>
    <div style="padding: 20px;" class="mt-0 mb-5">
      <div class="text-left row mb-3">
        <div class="col-md-4">
          <label class="mb-2 sr-only" for="inline-form-input-name">Booking_id</label>
          <b-form-input v-model="Booking_id" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
            placeholder=""></b-form-input>
        </div>
        <div class="col-md-4">
          <label class="mb-2 sr-only" for="inline-form-input-name">Firstdate</label>
          <b-form-input v-model="Firstdate" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
            placeholder=""></b-form-input>
        </div>
        <div class="col-md-4">
          <label class="mb-2 sr-only" for="inline-form-input-name">Lastdate</label>
          <b-form-input v-model="Lastdate" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
            placeholder=""></b-form-input>
        </div>
      </div>
      <b-button variant="success" @click="addReservation">Add Reservation</b-button>
    </div>
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
            <b-button @click="editReservation(Reservation)">edit</b-button>
            <b-button variant="danger" @click="deleteReservation(Reservation.Booking_id)">del</b-button>
          </td>
        </tr>
      </tbody>
    </table>
    <!-- Modal Edit-->
    <b-modal ref="myModalRef" title="Change Reservation Data" hide-footer>
      <div style="padding: 20px;">
        <div class="text-left row mb-3">
          <div class="col-md-4">
            <label class="mb-2 sr-only" for="inline-form-input-name">Booking_id</label>
            <b-form-input v-model="Booking_idEdit" id="inline-form-input-name" class="mb-2 mr-sm-2 mb-sm-0"
              placeholder="Booking id"></b-form-input>
          </div>
          <div class="col-md-4">
            <label class="mb-2 sr-only" for="inline-form-input-name">Firstdate</label>
            <b-form-input id="inline-form-input-name" v-model="FirstdateEdit" class="mb-2 mr-sm-2 mb-sm-0"
              placeholder="Firstdate"></b-form-input>
          </div>
          <div class="col-md-4">
            <label class="mb-2 sr-only" for="inline-form-input-name">Lastdate</label>
            <b-form-input id="inline-form-input-name" v-model="LastdateEdit" class="mb-2 mr-sm-2 mb-sm-0"
              placeholder="Lastdate"></b-form-input>
          </div>
        </div>
        <b-button variant="success" @click="updateReservation">Update Reservation</b-button>
      </div>
    </b-modal>
    <!-- Modal Edit-->
  </div>
</template>

<script>
export default {
  name: 'Reservation',
  data() {
    return {
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
    this.getReservation()
  },
  methods: {
    // Open Modal
    showModal() {
      this.$refs.myModalRef.show()
    },
    // Close Modal
    hideModal() {
      this.$refs.myModalRef.hide()
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