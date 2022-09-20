<template>
  <div v-if="loading" class="loading">
    Loading PhD listings :) ...
  </div>
  <ListingContainer v-else :jobs="jobs"/>
</template>

<script>
import ListingContainer from './components/ListingContainer.vue';

const API = process.env.VUE_APP_API_URL;

export default {
  name: 'App',
  components: {
    ListingContainer,
  },
  data() {
    return {
      jobs: [],
      loading: true,
    };
  },
  created() {
    fetch(API)
      .then((response) => {
        console.log(response);
        return response.json();
      })
      .then((data) => {
        this.jobs = data;
        this.loading = false;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  background-image: url('https://assets.stickpng.com/images/58f37747a4fa116215a92414.png');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: bottom;
  background-size: contain;
  height: 100%;
  width: 100%;
  margin: 0;
}
</style>
