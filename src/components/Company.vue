<template>
    <div style="padding: 20px;">
        <div>
            <h1>Company</h1>
        </div>
        <table class="table table-hover table-bordered" id="example">
              <thead>
                  <tr>
                      <th>Company_Name</th>
                      <th>Total</th>
                  </tr>
              </thead>
              <tbody>
                  <tr v-for="company in companies" :key="company.Company_Name">
                      <td>{{ company.Company_Name }}</td>
                      <td>{{ company.Total }}</td>
                  </tr>
              </tbody>
          </table>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Company',
    data() {
        return {
            companies: [],
        }
    },
    mounted() {
        this.getCompany()
    },
    methods: {
        async getCompany() {
            try {
                const response = await this.axios.get('http://localhost:8001/get_all_Company/')
                if (response.status === 200) {
                    this.companies = response.data
                } else {
                    throw { response }
                }
            } catch (error) {
                console.log(error)
            }
        }
    }
  }
  </script>
  
  <style>
  body {
    background-color: rgb(228, 215, 171);
  }
  </style>
  