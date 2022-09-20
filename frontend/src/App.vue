<template>
  <div class="site-title">
    Physics PhD Locator
  </div>
  <div class="site-description">
    This website will obtain listings from several different websites
    commonly used to find PhD funding projects.
  </div>
  <div v-if="loading" class="loading">
    Loading PhD listings...
    <br />
    Takes about one to two minutes :)
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
    // if already cached then load from storage
    if (localStorage.jobs) {
      const now = Date.now();
      const lastAccess = Number(localStorage.lastAccess);
      const hoursAgo = (now - lastAccess) / 1000 / 60 / 60;
      if (hoursAgo < 12) {
        const jobs = JSON.parse(localStorage.jobs);
        this.jobs = jobs || [];
        this.loading = false;
      }
      return;
    }
    // fetch the jobs from API
    fetch(API)
      .then((response) => response.json())
      .then((data) => {
        this.jobs = data;
        this.loading = false;
        localStorage.jobs = JSON.stringify(data);
        localStorage.lastAccess = Date.now();
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
  background-image: url('./assets/rick_morty.png');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: bottom;
  background-size: 100% auto;
  height: 100%;
  width: 100%;
  margin: 0;
}

@media screen and (min-width: 800px) {
  body {
    background-size: 50% auto;
  }
}

.loading {
  text-align: center;
  position: absolute;
  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  text-align: center;
  top: 30%;
  -moz-transition: all 0.5s ease-in-out;
  -webkit-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  -moz-animation: blink normal 1.5s infinite ease-in-out;
  /* Firefox */
  -webkit-animation: blink normal 1.5s infinite ease-in-out;
  /* Webkit */
  -ms-animation: blink normal 1.5s infinite ease-in-out;
  /* IE */
  animation: blink normal 1.5s infinite ease-in-out;
  /* Opera */
}

.site-title {
  display: block;
  text-align: center;
  margin: 10px;
  font-weight: bold;
  font-size: 2em;
}

.site-description {
  max-width: 900px;
  padding: 0 10px;
  margin: 0 auto;
  text-align: center;
  margin-bottom: 10px;
}

@keyframes blink {
  0% {
    color: rgba(0, 0, 0, 1);
  }

  50% {
    color: rgba(0, 0, 0, 0.5);
  }

  100% {
    color: rgba(0, 0, 0, 1);
  }
}

@-webkit-keyframes blink {
  0% {
    color: rgba(0, 0, 0, 1);
  }

  50% {
    color: rgba(0, 0, 0, 0.5);
  }

  100% {
    color: rgba(0, 0, 0, 1);
  }
}
</style>
