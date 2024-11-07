<template>
  <div id="app">
    <img alt="Vue logo" height="150px" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <SampleTable />
    <div>
      <!-- ส่วนเรียก Router -->
      <div>
        <div class="nav-link-container">
          <router-link :to="{ name: 'Company' }" class="nav-link">Home</router-link>
          <router-link :to="{ name: 'Customerpage' }" class="nav-link">Customerpage</router-link>
          <router-link :to="{ name: 'Reservationpage' }" class="nav-link">Reservationpage</router-link>
          <router-link :to="{ name: 'ProgramTour' }" class="nav-link">ProgramTourPage</router-link>
          <router-link :to="{ name: 'Guide' }" class="nav-link">GuidePage</router-link>
          <router-link :to="{ name: 'Booking' }" class="nav-link">BookingPage</router-link>
        </div>
      </div>
      <!-- ส่วนแสดงผลของ Router ที่เลือก หรือก็คือ body นั้นเอง -->
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
// import SampleTable from './components/SampleTable.vue';
// import HelloWorld from './components/HelloWorld.vue';

export default {
  name: 'App',
  // components: {
  //   HelloWorld,
  //   SampleTable
  // },
  // data() {
  //   return {}
  // },
}

</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
  margin-top: 60px;
}
.nav-link-container {
  display: flex;
  justify-content: space-around;
  border: 1px solid ghostwhite;
  padding: 10px;
}

.nav-link {
  text-decoration: none;
  color: black;
  padding: 5px 10px;
  border-radius: 5px;
}

.nav-link:hover {
  background-color: rgb(255, 255, 255);
}
</style>
